from __future__ import annotations

from typing import Dict, List

from .models import ShadowRecord


class ShadowStore:
    def __init__(self) -> None:
        self._records: Dict[str, ShadowRecord] = {}

    def put(self, record: ShadowRecord) -> None:
        self._records[record.id] = record

    def get(self, shadow_id: str) -> ShadowRecord:
        return self._records[shadow_id]

    def by_parent(self, parent_id: str) -> List[ShadowRecord]:
        return [r for r in self._records.values() if r.parent_id == parent_id]

    def promote(self, shadow_id: str):
        return self.get(shadow_id).payload

    def expire(self, shadow_id: str) -> bool:
        record = self.get(shadow_id)
        if record.critical:
            return False
        del self._records[shadow_id]
        return True

    def __len__(self) -> int:
        return len(self._records)
