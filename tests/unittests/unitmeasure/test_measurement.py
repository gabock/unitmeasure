import pytest

import unitmeasure


def test_immutable():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    with pytest.raises(TypeError):
        measure.value = 40
    with pytest.raises(TypeError):
        measure.unit = unitmeasure.UnitDuration.minutes


def test_description():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    assert measure.description == "60 s"


def test_debug_description():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    assert measure.debugDescription == "60 s"


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitArea.squareMeters), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1, unit=unitmeasure.Unit("blah")), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), True),
])
def test_equal(lhs, rhs, expected):
    assert (lhs == rhs) == expected


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitArea.squareMeters), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1, unit=unitmeasure.Unit("blah")), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), False),
])
def test_not_equal(lhs, rhs, expected):
    assert (lhs != rhs) == expected


def test_converted_not_dimension():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah"))
    with pytest.raises(TypeError):
        measure.converted(unitmeasure.UnitDuration.seconds)


def test_converted_same_unit():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    assert measure.converted(
        unitmeasure.UnitDuration.seconds) == unitmeasure.Measurement(
            value=60, unit=unitmeasure.UnitDuration.seconds)


def test_converted_base_unit():
    measure = unitmeasure.Measurement(value=1,
                                      unit=unitmeasure.UnitDuration.minutes)
    assert measure.converted(
        unitmeasure.UnitDuration.seconds) == unitmeasure.Measurement(
            value=60, unit=unitmeasure.UnitDuration.seconds)


def test_converted():
    measure = unitmeasure.Measurement(value=1,
                                      unit=unitmeasure.UnitDuration.hours)
    assert measure.converted(
        unitmeasure.UnitDuration.minutes) == unitmeasure.Measurement(
            value=60, unit=unitmeasure.UnitDuration.minutes)


def test_convert():
    measure = unitmeasure.Measurement(value=1,
                                      unit=unitmeasure.UnitDuration.hours)
    measure.convert(unitmeasure.UnitDuration.minutes)
    assert measure == unitmeasure.Measurement(
        value=60, unit=unitmeasure.UnitDuration.minutes)
