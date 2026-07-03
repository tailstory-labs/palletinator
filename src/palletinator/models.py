"""Output data model for built pallets."""

from typing import Any

from pydantic import BaseModel, Field


class Cell(BaseModel, frozen=True):
    """A single cell within a pallet column.

    Attributes
    ----------
    value
        The value displayed in the cell.
    extras
        Open-ended metadata bag for caller-defined fields.

    Notes
    -----
    Serializable to and from JSON with pydantic's built-ins:
    ``cell.model_dump_json()`` and ``Cell.model_validate_json(data)``.
    """

    value: str
    extras: dict[str, Any] = Field(default_factory=dict)


class Column(BaseModel, frozen=True):
    """A column on a pallet side, with cells ordered top-to-bottom."""

    number: int
    cells: list[Cell]


class Side(BaseModel, frozen=True):
    """A side of a pallet, with columns ordered left-to-right by column number."""

    number: int
    columns: list[Column]


class Pallet(BaseModel, frozen=True):
    """A fully-resolved pallet build.

    Attributes
    ----------
    sides
        Sides on the pallet, ordered by side number.
    extras
        Open-ended metadata bag for caller-defined fields.

    Notes
    -----
    Serializable to and from JSON with pydantic's built-ins:
    ``pallet.model_dump_json()`` and ``Pallet.model_validate_json(data)``.
    """

    sides: list[Side]
    extras: dict[str, Any] = Field(default_factory=dict)
