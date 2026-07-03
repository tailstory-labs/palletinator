"""Tests for the pydantic data models."""

import pytest
from pydantic import ValidationError

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


def test_cell_is_frozen() -> None:
    cell = Cell(value="X")
    with pytest.raises(ValidationError):
        cell.value = "Y"


def test_pallet_is_frozen() -> None:
    pallet = Pallet(sides=[])
    with pytest.raises(ValidationError):
        pallet.sides = []


def test_cell_placement_is_frozen() -> None:
    placement = CellPlacement(value="X", sides=[1], columns=[1])
    with pytest.raises(ValidationError):
        placement.value = "Y"


def test_frozen_models_still_allow_in_place_extras_mutation() -> None:
    pallet = Pallet(sides=[], extras={})
    pallet.extras["k"] = "v"
    assert pallet.extras == {"k": "v"}
