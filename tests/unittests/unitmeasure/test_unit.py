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


class TestCaseUnitConcentrationMass(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("gramsPerLiter", "g/L"),
        ("milligramsPerDeciliter", "mg/dL"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitConcentrationMass, prop)
        assert accel.symbol == symbol

    def test_millimolesPerLiter_symbol(self):
        assert unitmeasure.UnitConcentrationMass.millimolesPerLiter(
            2).symbol == "mmol/L"


class TestCaseUnitDispersion(object):

    @pytest.mark.parametrize("prop, symbol", [("partsPerMillion", "ppm")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitDispersion, prop)
        assert accel.symbol == symbol


class TestCaseUnitDuration(object):

    @pytest.mark.parametrize("prop, symbol", [("seconds", "s"),
                                              ("minutes", "m"), ("hours", "h")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitDuration, prop)
        assert accel.symbol == symbol
