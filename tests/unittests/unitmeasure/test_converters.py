import pytest

import unitmeasure


class TestCaseBaseConverter(object):
    def test_unit_converter_base(self):
        unit_converter = unitmeasure.converters.UnitConverter()
        # While this test is very simple, it is here to ensure that these
        # methods are maintained as the interface for a unit converter
        assert unit_converter.baseUnitValue(5) == 5
        assert unit_converter.value(10) == 10


class TestCaseLinearConverter(object):

    @pytest.mark.parametrize("value, coef, constant, expected", [
        (2, 4, 0, 8),
        (5, 5, 2, 27),
        (4, 1, 6, 10),
    ])
    def test_base_unit(self, value, coef, constant, expected):
        unit_converter = unitmeasure.converters.UnitConverterLinear(coef, constant)
        assert unit_converter.baseUnitValue(value) == expected

    @pytest.mark.parametrize("base_value, coef, constant, expected", [
        (10, 2, 0, 5),
        (10, 2, 2, 4),
        (10, 1, 5, 5),
    ])
    def test_value(self, base_value, coef, constant, expected):
        unit_converter = unitmeasure.converters.UnitConverterLinear(coef, constant)
        assert unit_converter.value(base_value) == expected

    def test_base_constant(self):
        unit_converter = unitmeasure.converters.UnitConverterLinear(10)
        assert unit_converter.constant == 0

    @pytest.mark.parametrize("converter1, converter2, expected", [
        (unitmeasure.converters.UnitConverterLinear(10), unitmeasure.converters.UnitConverterLinear(10), True),
        (unitmeasure.converters.UnitConverterLinear(10), unitmeasure.converters.UnitConverterLinear(10, 5), False),
        (unitmeasure.converters.UnitConverterLinear(10, 5), unitmeasure.converters.UnitConverterLinear(10, 5), True),
        (unitmeasure.converters.UnitConverterLinear(10), 10, False)
    ])
    def test_equals(self, converter1, converter2, expected):
        assert (converter1 == converter2) == expected
        