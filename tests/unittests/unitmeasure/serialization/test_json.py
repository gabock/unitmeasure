import decimal
import json
import pytest

import unitmeasure
from unitmeasure import dimension
from unitmeasure.units.duration import UnitDuration


class TestCaseToJSON(object):

    def test_basic(self):
        measure = unitmeasure.Measurement(value=60,
                                          unit=unitmeasure.UnitDuration.seconds)
        jmeasure = unitmeasure.to_json(measure)
        expected = json.dumps(
            {
                "unit": {
                    "symbol": "s",
                    "converter": {
                        "coefficient": 1.0,
                        "constant": 0
                    }
                },
                "value": 60
            },
            indent=4)
        assert jmeasure == expected

    def test_float_value(self):
        measure = unitmeasure.Measurement(value=60.5,
                                          unit=unitmeasure.UnitDuration.seconds)
        jmeasure = unitmeasure.to_json(measure)
        expected = json.dumps(
            {
                "unit": {
                    "symbol": "s",
                    "converter": {
                        "coefficient": 1.0,
                        "constant": 0
                    }
                },
                "value": 60.5
            },
            indent=4)
        assert jmeasure == expected

    def test_decimal(self):
        measure = unitmeasure.Measurement(value=decimal.Decimal(60),
                                          unit=unitmeasure.UnitDuration.seconds)
        jmeasure = unitmeasure.to_json(measure)
        expected = json.dumps(
            {
                "unit": {
                    "symbol": "s",
                    "converter": {
                        "coefficient": 1.0,
                        "constant": 0
                    }
                },
                "value": 60.0
            },
            indent=4)
        assert jmeasure == expected

    def test_basic_unit(self):
        measure = unitmeasure.Measurement(value=decimal.Decimal(60),
                                          unit=unitmeasure.Unit("s"))
        jmeasure = unitmeasure.to_json(measure)
        expected = json.dumps({
            "unit": {
                "symbol": "s",
            },
            "value": 60.0
        },
                              indent=4)
        assert jmeasure == expected

    def test_UnitConverterReciprocal(self):
        measure = unitmeasure.Measurement(
            value=decimal.Decimal(60),
            unit=unitmeasure.UnitFuelEfficiency.milesPerGallon)
        jmeasure = unitmeasure.to_json(measure)
        expected = json.dumps(
            {
                "unit": {
                    "symbol": "mpg",
                    "converter": {
                        "reciprocal": 235.215
                    }
                },
                "value": 60.0
            },
            indent=4)
        assert jmeasure == expected


class TestCaseFromJSON(object):

    def test_unit_not_given(self):
        data = json.dumps(
            {
                "unit": {
                    "symbol": "s",
                    "converter": {
                        "coefficient": 1.0,
                        "constant": 0
                    }
                },
                "value": 60
            },
            indent=4)
        measure = unitmeasure.from_json(data)
        assert measure == unitmeasure.Measurement(value=60,
                                                  unit=unitmeasure.Unit("s"))

    def test_unit_given(self):
        data = json.dumps(
            {
                "unit": {
                    "symbol": "s",
                    "converter": {
                        "coefficient": 1.0,
                        "constant": 0
                    }
                },
                "value": 60
            },
            indent=4)
        measure = unitmeasure.from_json(data,
                                        dimension=unitmeasure.UnitDuration)
        assert measure == unitmeasure.Measurement(
            value=60, unit=unitmeasure.UnitDuration.seconds)

    def test_UnitConverterReciprocal(self):
        data = json.dumps(
            {
                "unit": {
                    "symbol": "mpg",
                    "converter": {
                        "reciprocal": 235.215
                    }
                },
                "value": 60.0
            },
            indent=4)
        measure = unitmeasure.from_json(
            data, dimension=unitmeasure.UnitFuelEfficiency)
        assert measure == unitmeasure.Measurement(
            value=60, unit=unitmeasure.UnitFuelEfficiency.milesPerGallon)
