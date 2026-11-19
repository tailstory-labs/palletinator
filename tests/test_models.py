"""Tests for the pydantic data models."""

import pytest
from pydantic import BaseModel, ValidationError

from palletinator import Cell, CellPlacement, Pallet, build_pallet


def test_pallet_json_round_trip() -> None:
    pallet = build_pallet(
        [
            CellPlacement(value="A", sides=[1, 2], columns=[1], extras={"code": "K1"}),
            CellPlacement(value="B", sides=[1], columns=[1, 2], extras={"code": "K2"}),
        ],
        extras={"order_id": "PZ-1", "required_count": 4},
    )

    assert Pallet.model_validate_json(pallet.model_dump_json()) == pallet


def test_cell_placement_json_round_trip() -> None:
    placement = CellPlacement(value="A", sides=[1, 3], columns=[2], extras={"code": "K1"})
    assert CellPlacement.model_validate_json(placement.model_dump_json()) == placement


@pytest.mark.parametrize(
    ("model", "field", "value"),
    [
        (Cell(value="X"), "value", "Y"),
        (Pallet(sides=[]), "sides", []),
        (CellPlacement(value="X", sides=[1], columns=[1]), "value", "Y"),
    ],
)
def test_models_are_frozen(model: BaseModel, field: str, value: object) -> None:
    with pytest.raises(ValidationError):
        setattr(model, field, value)


def test_frozen_models_still_allow_in_place_extras_mutation() -> None:
    pallet = Pallet(sides=[], extras={})
    pallet.extras["k"] = "v"
    assert pallet.extras == {"k": "v"}
