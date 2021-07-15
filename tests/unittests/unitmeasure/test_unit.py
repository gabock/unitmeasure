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


class TestCaseUnitElectricCharge(object):

    @pytest.mark.parametrize("prop, symbol", [("coulombs", "C"),
                                              ("megaampereHours", "MAh"),
                                              ("kiloampereHours", "kAh"),
                                              ("ampereHours", "Ah"),
                                              ("milliampereHours", "mAh"),
                                              ("microampereHours", "µAh")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitElectricCharge, prop)
        assert accel.symbol == symbol


class TestCaseUnitElectricPotentialDifference(object):

    @pytest.mark.parametrize("prop, symbol", [("megavolts", "MV"),
                                              ("kilovolts", "kV"),
                                              ("volts", "V"),
                                              ("millivolts", "mV"),
                                              ("microvolts", "µV")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitElectricPotentialDifference, prop)
        assert accel.symbol == symbol


class TestCaseUnitElectricResistance(object):

    @pytest.mark.parametrize("prop, symbol", [("megaohms", "MΩ"),
                                              ("kiloohms", "kΩ"), ("ohms", "Ω"),
                                              ("milliohms", "mΩ"),
                                              ("microohms", "µΩ")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitElectricResistance, prop)
        assert accel.symbol == symbol


class TestCaseUnitEnergy(object):

    @pytest.mark.parametrize("prop, symbol", [("kilojoules", "kJ"),
                                              ("joules", "J"),
                                              ("kilocalories", "kCal"),
                                              ("calories", "cal"),
                                              ("kilowattHours", "kWh")])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitEnergy, prop)
        assert accel.symbol == symbol


class TestCaseUnitFrequency(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("terahertz", "THz"),
        ("gigahertz", "GHz"),
        ("megahertz", "MHz"),
        ("kilohertz", "kHz"),
        ("hertz", "Hz"),
        (
            "millihertz",
            "mHz",
        ),
        (
            "microhertz",
            "µHz",
        ),
        ("nanohertz", "nHz"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitFrequency, prop)
        assert accel.symbol == symbol


class TestCaseUnitFuelEfficiency(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("litersPer100Kilometers", "L/100km"),
        ("milesPerImperialGallon", "mpg"),
        ("milesPerGallon", "mpg"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitFuelEfficiency, prop)
        assert accel.symbol == symbol


class TestCaseUnitLength(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("megameters", "Mm"),
        ("kilometers", "km"),
        ("hectometers", "hm"),
        ("decameters", "dam"),
        ("meters", "m"),
        ("decimeters", "dm"),
        ("centimeters", "cm"),
        ("millimeters", "mm"),
        ("micrometers", "µm"),
        ("nanometers", "nm"),
        ("picometers", "pm"),
        ("inches", "in"),
        ("feet", "ft"),
        ("yards", "yd"),
        ("miles", "mi"),
        ("scandinavianMiles", "smi"),
        ("lightyears", "ly"),
        ("nauticalMiles", "NM"),
        ("fathoms", "ftm"),
        ("furlongs", "fur"),
        ("astronomicalUnits", "ua"),
        ("parsecs", "pc"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitLength, prop)
        assert accel.symbol == symbol


class TestCaseUnitIlluminance(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("lux", "lx"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitIlluminance, prop)
        assert accel.symbol == symbol


class TestCaseUnitMass(object):

    @pytest.mark.parametrize("prop, symbol", [
        ("kilograms", "kg"),
        ("grams", "g"),
        ("decigrams", "dg"),
        ("centigrams", "cg"),
        ("milligrams", "mg"),
        ("micrograms", "µg"),
        ("nanograms", "ng"),
        ("picograms", "pg"),
        ("ounces", "oz"),
        ("pounds", "lb"),
        ("stones", "st"),
        ("metricTons", "t"),
        ("shortTons", "ton"),
        ("carats", "ct"),
        ("ouncesTroy", "oz t"),
        ("slugs", "slug"),
    ])
    def test_symbol(self, prop, symbol):
        accel = getattr(unitmeasure.UnitMass, prop)
        assert accel.symbol == symbol
