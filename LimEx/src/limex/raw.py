"""Order-preserving raw document entities."""

from dataclasses import dataclass, field
from typing import Optional

from .state import Value


@dataclass(slots=True)
class RawField:
    name: str
    value: Value[str]
    field_order: int
    source_path: Optional[str] = None


@dataclass(slots=True)
class RawRow:
    row_order: int
    fields: list[RawField] = field(default_factory=list)
    source_id: Optional[str] = None


@dataclass(slots=True)
class RawTable:
    name: str
    table_order: int
    fields: list[str] = field(default_factory=list)
    rows: list[RawRow] = field(default_factory=list)
    known: bool = False
    source_path: Optional[str] = None

    def add_row(self, row: RawRow) -> None:
        self.rows.append(row)

    def field_names(self) -> tuple[str, ...]:
        return tuple(self.fields)
