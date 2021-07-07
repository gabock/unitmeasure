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


class TestCaseUnitAcceleration(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("metersPerSecondSquared", "m/s²"),
        ("gravity", "g"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitAcceleration, prop)
        assert accel.symbol == symbol


class TestCaseUnitAngle(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("degrees", "°"),
        ("arcMinutes", "ʹ"),
        ("arcSeconds", "ʹʹ"),
        ("radians", "rad"),
        ("gradians", "grad"),
        ("revolutions", "rev"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitAngle, prop)
        assert accel.symbol == symbol


class TestCaseUnitArea(object):

    @pytest.mark.parametrize("prop, symbol", [("squareMegameters", "Mm²"),
                                              ("squareKilometers", "km²"),
                                              ("squareMeters", "m²"),
                                              ("squareCentimeters", "cm²"),
                                              ("squareMillimeters", "mm²"),
                                              ("squareMicrometers", "µm²"),
                                              ("squareNanometers", "nm²"),
                                              ("squareInches", "in²"),
                                              ("squareFeet", "ft²"),
                                              ("squareYards", "yd²"),
                                              ("squareMiles", "mi²"),
                                              ("acres", "ac"), ("ares", "a"),
                                              ("hectares", "ha")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitArea, prop)
        assert accel.symbol == symbol
