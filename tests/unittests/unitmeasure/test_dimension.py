import pytest

import unitmeasure

def test_unit_symbol():
    dimension = unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1))
    assert dimension.symbol == "s"
    assert dimension.converter == unitmeasure.converters.UnitConverterLinear(1)

@pytest.mark.parametrize("unit1, unit2, expected", [
    (unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)), unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)), True),
    (unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)), unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(2)), False),
    (unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)), unitmeasure.Dimension("a", unitmeasure.converters.UnitConverterLinear(1)), False),
    (unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)), "s", False),
])
def test_is_equal(unit1, unit2, expected):
    assert (unit1 == unit2) == expected

def test_base_unit():
    with pytest.raises(NotImplementedError):
        unitmeasure.Dimension("s", unitmeasure.converters.UnitConverterLinear(1)).baseUnit()