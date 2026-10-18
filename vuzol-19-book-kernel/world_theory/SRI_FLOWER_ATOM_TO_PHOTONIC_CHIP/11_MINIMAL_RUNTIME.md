# 11 — Мінімальний програмний контракт Sri Photonic Gate

## Пакет запиту

```yaml
measurement_request:
  wave_mode_candidates: [plus3, minus3]
  sensor_geometry: hex6
  phase_reference: available
  calibration_id: ref_001
  confidence_threshold: 0.99
  energy_budget_joule: 0.1  # демонстраційне значення, не специфікація чіпа
```

## Структура стану

```yaml
sri_state:
  input: complex_sensor_vector
  geometry: R_sensor
  structure_features: []
  flow_features: []
  resonance_features: []
  rule_checks: []
  memory_match: null
  observability_rank: null
  shadow_residual: null
  verdict: HOLD
```

## Псевдокод

```python
def sri_gate(measurement, geometry, reference, calibration):
    features = extract_wave_features(measurement)   # +3 structure/flow/resonance
    M = build_observation_matrix(geometry, reference)

    if matrix_rank(M) < required_rank(features):
        return {"verdict": "HOLD", "next": "new_phase_observation"}

    estimate = solve_calibrated_inverse(M, measurement, calibration)
    shadow = compare_with_reference(estimate, reference)
    if shadow.exceeds_limit:
        return {"verdict": "REWRITE", "next": "recalibrate_or_remeasure"}

    checks = sri_layers_14_10_10_8(estimate)       # логічний каскад, не фізичний закон
    if not checks.physical_constraints_ok:
        return {"verdict": "BLOCK"}
    if not checks.confident:
        return {"verdict": "HOLD", "next": "additional_measurement"}
    return {"verdict": "ALLOW", "state": estimate, "memory": checks.trace}
```

Функції наведені як **інтерфейсні контракти**, а не готові виконувані реалізації. Для реального тесту потрібна специфікація `extract_wave_features`, похибок, калібрування та чотирьох шарів Шрі.

## Основні критерії

- рішення має коректно давати `HOLD`, якщо `+3` і `−3` аліасуються на шести стовпах;
- після незалежного фазочутливого вимірювання може дати `ALLOW` лише за контрольованого шуму та калібрування;
- енергія в обліку включає лазер, фотоелектроніку, FPGA й тепловий контроль;
- додавання 14/10/10/8 має порівнюватися із простішим baseline.
