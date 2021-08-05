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


def test_to_str():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    assert str(measure) == "60 s"

def test_repr():
    measure = unitmeasure.Measurement(value=60,
                                      unit=unitmeasure.UnitDuration.seconds)
    assert measure.__repr__() == "Measurement<UnitDuration>"


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

def test_iadd():
    m  = unitmeasure.Measurement(value=10, unit=unitmeasure.UnitDuration.seconds)
    m += unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.minutes)
    assert m.value == 70
    assert m.unit == unitmeasure.UnitDuration.seconds


def test_radd_scalar():
    # radd is only ever called if the operand on the left side does not support the addition.
    # so we should raise an error we aren't adding measurements together.
    with pytest.raises(TypeError):
        m = 3 + unitmeasure.Measurement(value=10,
                                        unit=unitmeasure.UnitDuration.seconds)


def test_sub_same_units():
    m1 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.hours)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.hours)
    m3 = m1 - m2
    assert m3.value == 0
    assert m3.unit == unitmeasure.UnitDuration.hours


def test_sub_same_dimension():
    m1 = unitmeasure.Measurement(value=10,
                                 unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.minutes)
    m3 = m1 - m2
    assert m3.value == -50
    assert m3.unit == unitmeasure.UnitDuration.seconds

def test_isub():
    m = unitmeasure.Measurement(value=10,
                                 unit=unitmeasure.UnitDuration.seconds)
    m -= unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.minutes)
    assert m.value == -50
    assert m.unit == unitmeasure.UnitDuration.seconds


def test_sub_different_dimension():
    m1 = unitmeasure.Measurement(value=10,
                                 unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitLength.meters)
    with pytest.raises(TypeError):
        m3 = m1 - m2


def test_sub_scalar():
    with pytest.raises(TypeError):
        m3 = unitmeasure.Measurement(value=10,
                                     unit=unitmeasure.UnitDuration.seconds) - 3


def test_rsub_scalar():
    # rsub is only ever called if the operand on the left side does not support the addition.
    # so we should raise an error we aren't adding measurements together.
    with pytest.raises(TypeError):
        m = 3 - unitmeasure.Measurement(value=10,
                                        unit=unitmeasure.UnitDuration.seconds)


def test_mul():
    assert unitmeasure.Measurement(
        value=10,
        unit=unitmeasure.UnitDuration.seconds) * 3 == unitmeasure.Measurement(
            value=30, unit=unitmeasure.UnitDuration.seconds)

def test_imul():
    m = unitmeasure.Measurement(value=10, unit=unitmeasure.UnitDuration.seconds)
    m *= 3
    assert m == unitmeasure.Measurement(value=30, unit=unitmeasure.UnitDuration.seconds)


def test_rmul():
    assert 3 * unitmeasure.Measurement(
        value=10,
        unit=unitmeasure.UnitDuration.seconds) == unitmeasure.Measurement(
            value=30, unit=unitmeasure.UnitDuration.seconds)


def test_mul_two_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=10,
            unit=unitmeasure.UnitDuration.seconds) * unitmeasure.Measurement(
                value=10, unit=unitmeasure.UnitDuration.seconds)


def test_truediv():
    assert unitmeasure.Measurement(
        value=5,
        unit=unitmeasure.UnitDuration.seconds) / 2 == unitmeasure.Measurement(
            value=2.5, unit=unitmeasure.UnitDuration.seconds)

def test_itruediv():
    m = unitmeasure.Measurement(value=5, unit=unitmeasure.UnitDuration.seconds)
    m /= 2
    assert m == unitmeasure.Measurement(value=2.5, unit=unitmeasure.UnitDuration.seconds)

def test_rtruediv():
    assert 3 / unitmeasure.Measurement(
        value=4,
        unit=unitmeasure.UnitDuration.seconds) == unitmeasure.Measurement(
            value=0.75, unit=unitmeasure.UnitDuration.seconds)


def test_truediv_two_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=10,
            unit=unitmeasure.UnitDuration.seconds) / unitmeasure.Measurement(
                value=10, unit=unitmeasure.UnitDuration.seconds)


def test_floordiv():
    assert unitmeasure.Measurement(
        value=5,
        unit=unitmeasure.UnitDuration.seconds) // 2 == unitmeasure.Measurement(
            value=2, unit=unitmeasure.UnitDuration.seconds)


def test_rfloordiv():
    assert 3 // unitmeasure.Measurement(
        value=4,
        unit=unitmeasure.UnitDuration.seconds) == unitmeasure.Measurement(
            value=0, unit=unitmeasure.UnitDuration.seconds)

def test_ifloordiv():
    m = unitmeasure.Measurement(value=5, unit=unitmeasure.UnitDuration.seconds)
    m //= 2
    assert m == unitmeasure.Measurement(value=2, unit=unitmeasure.UnitDuration.seconds)


def test_floordiv_two_dimensions():
    with pytest.raises(TypeError):
        unitmeasure.Measurement(
            value=10,
            unit=unitmeasure.UnitDuration.seconds) // unitmeasure.Measurement(
                value=10, unit=unitmeasure.UnitDuration.seconds)

def test_hash_simple():
    m = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    d = {m: "hello there"}
    assert m is m
    assert m == m
    assert d[m] == "hello there"

def test_hash_new_obj_lookup():
    m = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    d = {m: "hello there"}
    assert m is not m2
    assert m == m2
    assert d[m2] == "hello there"

def test_hash_same_if_converted():
    m = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=1, unit=unitmeasure.UnitDuration.minutes)
    d = {m: "hello there"}
    assert m == m2
    assert d[m2] == "hello there"

def test_hash_keyerror_different_values():
    m = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=6, unit=unitmeasure.UnitDuration.seconds)
    d = {m: "hello there"}
    assert m is not m2
    assert m != m2
    with pytest.raises(KeyError):
        d[m2]

def test_hash_keyerror_different_unit():
    m = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.minutes)
    d = {m: "hello there"}
    assert m is not m2
    assert m != m2
    with pytest.raises(KeyError):
        d[m2]

def test_hash_keyerror_different_dim():
    m = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitDuration.seconds)
    m2 = unitmeasure.Measurement(value=3, unit=unitmeasure.UnitLength.feet)
    d = {m: "hello there"}
    assert m is not m2
    assert m != m2
    with pytest.raises(KeyError):
        d[m2]