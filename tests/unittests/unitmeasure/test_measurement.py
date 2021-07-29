import pytest

import unitmeasure

def test_immutable():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    with pytest.raises(TypeError):
        measure.value = 40
    with pytest.raises(TypeError):
        measure.unit = unitmeasure.UnitDuration.minutes

def test_description():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    assert measure.description == "60 s"

def test_debug_description():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    assert measure.debugDescription == "60 s"