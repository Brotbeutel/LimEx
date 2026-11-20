"""Explicit source-value state handling."""

from dataclasses import dataclass
from enum import Enum
from typing import Generic, Optional, TypeVar


class ValueState(str, Enum):
    MISSING = "missing"
    EMPTY = "empty"
    VALUE = "value"
    DELETED = "deleted"


T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Value(Generic[T]):
    """A value with source presence independent of its Python value."""

    state: ValueState
    raw: Optional[T] = None

    def __post_init__(self) -> None:
        if self.state in (ValueState.MISSING, ValueState.DELETED) and self.raw is not None:
            raise ValueError(f"{self.state.value} values cannot contain raw content")
        if self.state == ValueState.EMPTY and self.raw not in ("", b""):
            raise ValueError("empty values must contain an empty string")
        if self.state == ValueState.VALUE and self.raw is None:
            raise ValueError("value state requires raw content")

    @classmethod
    def missing(cls) -> "Value[T]":
        return cls(ValueState.MISSING)

    @classmethod
    def empty(cls) -> "Value[str]":
        return cls(ValueState.EMPTY, "")

    @classmethod
    def value(cls, raw: T) -> "Value[T]":
        if raw is None:
            raise ValueError("use missing() or empty() for absent content")
        if raw == "":
            return cls.empty()
        return cls(ValueState.VALUE, raw)

    @classmethod
    def deleted(cls) -> "Value[T]":
        return cls(ValueState.DELETED)
