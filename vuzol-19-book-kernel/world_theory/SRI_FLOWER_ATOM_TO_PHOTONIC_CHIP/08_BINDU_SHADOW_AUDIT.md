# 08 — Shadow / Bindu: спостережуваність і відмова від хибної впевненості

## Схема станів

```text
OBSERVE → ESTIMATE → CONFIDENCE CHECK
             │
             ├─ enough evidence → VALIDATE → ALLOW / BLOCK
             │
             └─ ambiguous → HOLD → CHANGE OBSERVATION → RE-MEASURE
                                                 │
                                      compare with independent reference
                                                 │
                                            REWRITE / ALLOW
```

## Shadow Ledger

Фіксувати мінімальний набір:

```yaml
shadow_record:
  input_id: experiment_case
  model_id: calibration_revision
  geometry_id: sensor_layout
  hypothesis_set: [mode_plus3, mode_minus3]
  observability_rank: 1
  calibration_drift: unknown
  uncertainty: high
  reason: aliasing_or_insufficient_reference
  verdict: HOLD
  next_action: additional_phase_measurement
```

## Визначення точного verdict

- `ALLOW`: підтверджені дані та пройдений контроль потрібних інваріантів.
- `HOLD`: сигнали неоднозначні, датчики не спостерігають потрібні компоненти або відсутній еталон.
- `BLOCK`: несумісність з фізичними законами або небезпечна недопустима дія.
- `REWRITE`: переглянути модель/сенсорний план після нових даних; не підміняти факти.

## Типова помилка

«Після повороту сенсорів картинка змінилася — це була помилка приладу». **Ні:** справжній фізичний сигнал теж може бути орієнтаційно залежним. Потрібна спільна модель сигналу й вимірювання з незалежною перевіркою.

## Типова помилка 2

«Сильна інтерференція = правильна відповідь». **Ні:** інтерференція демонструє узгодженість фаз, а не істинність класифікації. Клас і достовірність перевіряють незалежним еталоном.
