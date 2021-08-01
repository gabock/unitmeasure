import pytest

import unitmeasure
from unitmeasure.units.duration import UnitDuration


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


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=45, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=30, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), False),
])
def test_lt(lhs, rhs, expected):
    assert (lhs < rhs) == expected


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=45, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=30, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), True),
])
def test_le(lhs, rhs, expected):
    assert (lhs <= rhs) == expected


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=45, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=30, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), False),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), False),
])
def test_gt(lhs, rhs, expected):
    assert (lhs > rhs) == expected


@pytest.mark.parametrize("lhs, rhs, expected", [
    (unitmeasure.Measurement(value=45, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=60,
                             unit=unitmeasure.UnitDuration.seconds), False),
    (unitmeasure.Measurement(value=120, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=1,
                             unit=unitmeasure.UnitDuration.minutes), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds),
     unitmeasure.Measurement(value=45,
                             unit=unitmeasure.UnitDuration.seconds), True),
    (unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")),
     unitmeasure.Measurement(value=60, unit=unitmeasure.Unit("blah")), True),
])
def test_ge(lhs, rhs, expected):
    assert (lhs >= rhs) == expected


def test_lt_non_equal_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=60,
            unit=unitmeasure.UnitDuration.seconds) < unitmeasure.Measurement(
                value=1, unit=unitmeasure.Unit("blah"))


def test_le_non_equal_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=60,
            unit=unitmeasure.UnitDuration.seconds) <= unitmeasure.Measurement(
                value=1, unit=unitmeasure.Unit("blah"))


def test_gt_non_equal_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=60,
            unit=unitmeasure.UnitDuration.seconds) > unitmeasure.Measurement(
                value=1, unit=unitmeasure.Unit("blah"))


def test_ge_non_equal_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=60,
            unit=unitmeasure.UnitDuration.seconds) >= unitmeasure.Measurement(
                value=1, unit=unitmeasure.Unit("blah"))


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


def test_add_same_units():
    m1 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.hours)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.hours)
    m3 = m1 + m2
    assert m3.value == 2
    assert m3.unit == unitmeasure.UnitDuration.hours


def test_add_same_dimension():
    m1 = unitmeasure.Measurement(value=10,
                                 unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.minutes)
    m3 = m1 + m2
    assert m3.value == 70
    assert m3.unit == unitmeasure.UnitDuration.seconds


def test_add_different_dimension():
    m1 = unitmeasure.Measurement(value=10,
                                 unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitLength.meters)
    with pytest.raises(TypeError):
        m3 = m1 + m2


def test_add_scalar():
    with pytest.raises(TypeError):
        m3 = unitmeasure.Measurement(value=10,
                                     unit=unitmeasure.UnitDuration.seconds) + 3

def test_radd_scalar():
    # radd is only ever called if the operand on the left side does not support the addition.
    # so we should raise an error we aren't adding measurements together.
    with pytest.raises(TypeError):
        m = 3 + unitmeasure.Measurement(value=10, unit=unitmeasure.UnitDuration.seconds)