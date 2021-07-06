import pytest

import unitmeasure

def test_unit_symbol():
    unit = unitmeasure.Unit("s")
    assert unit.symbol == "s"

@pytest.mark.parametrize("unit1, unit2, expected", [
    (unitmeasure.Unit("s"), unitmeasure.Unit("s"), True),
    (unitmeasure.Unit("s"), unitmeasure.Unit("a"), False),
    (unitmeasure.Unit("s"), "s", False),
])
def test_is_equal(unit1, unit2, expected):
    assert (unit1 == unit2) == expected
