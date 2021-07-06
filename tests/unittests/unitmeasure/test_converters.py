import pytest

import unitmeasure

def test_unit_converter_base():
    unit_converter = unitmeasure.converters.UnitConverter()
    # While this test is very simple, it is here to ensure that these
    # methods are maintained as the interface for a unit converter
    assert unit_converter.baseUnitValue(5) == 5
    assert unit_converter.value(10) == 10