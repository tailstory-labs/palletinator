"""Output data model for built pallets."""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Cell(BaseModel):
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

    model_config = ConfigDict(frozen=True)

    value: str
    extras: dict[str, Any] = Field(default_factory=dict)


class Column(BaseModel):
    """A column on a pallet side, with cells ordered top-to-bottom."""

    model_config = ConfigDict(frozen=True)

    number: int
    cells: list[Cell]


class Side(BaseModel):
    """A side of a pallet, with columns ordered left-to-right by column number."""

    model_config = ConfigDict(frozen=True)

    number: int
    columns: list[Column]


class Pallet(BaseModel):
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

    model_config = ConfigDict(frozen=True)

    sides: list[Side]
    extras: dict[str, Any] = Field(default_factory=dict)
