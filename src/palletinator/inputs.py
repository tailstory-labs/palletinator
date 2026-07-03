"""Input types for the pallet builder."""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class CellPlacement(BaseModel):
    """Specification for where a cell goes on a pallet build.

    Attributes
    ----------
    value
        The value displayed in the resulting cell.
    sides
        Side numbers the cell appears on.
    columns
        Column numbers (within each side) the cell appears in.
    extras
        Open-ended metadata bag for caller-defined fields. A copy is
        attached to every emitted ``Cell`` so callers can mutate per-cell
        state without cross-talk.

    Notes
    -----
    Serializable to and from JSON with pydantic's built-ins:
    ``placement.model_dump_json()`` and ``CellPlacement.model_validate_json(data)``.
    """

    model_config = ConfigDict(frozen=True)

    value: str
    sides: list[int]
    columns: list[int]
    extras: dict[str, Any] = Field(default_factory=dict)
