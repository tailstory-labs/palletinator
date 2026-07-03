# Pallet-inator

A library for building structured pallet data.

Describe where each cell goes with `CellPlacement`s, and `build_pallet` assembles them
into a `Pallet` of sides, columns, and cells — sorted by number, with cells kept in
placement order. The engine performs no I/O and applies no business rules: callers
decide where each cell goes and what extra metadata it carries. Every `Cell` and
`Pallet` has an open-ended `extras` bag for caller-defined fields, so domain-specific
data rides along without the library needing to know about it.

## Usage

```python
from palletinator import CellPlacement, build_pallet

placements = [
    CellPlacement(value="A-1", sides=[1, 2], columns=[1], extras={"design": "D-100"}),
    CellPlacement(value="A-2", sides=[1, 2], columns=[1], extras={"design": "D-101"}),
    CellPlacement(value="B-1", sides=[1], columns=[2], extras={"design": "D-200"}),
]

pallet = build_pallet(placements, extras={"order_id": "PZ-1", "required_count": 4})

for side in pallet.sides:
    for column in side.columns:
        for cell in column.cells:
            print(side.number, column.number, cell.value, cell.extras)
```

## JSON serialization

All models are [pydantic](https://docs.pydantic.dev/) models, so serialization comes
built in — no custom methods:

```python
data = pallet.model_dump_json()
restored = Pallet.model_validate_json(data)
assert restored == pallet
```

---

Here's a pallet-pus (get it?)

![palletpus](https://raw.githubusercontent.com/impressdesigns/palletinator/main/docs/static/palletpus.jpeg "Palletpus")
