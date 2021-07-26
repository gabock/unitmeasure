import dataclasses

import pytest

import unitmeasure

def test_immutable():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    with pytest.raises(dataclasses.FrozenInstanceError):
        measure.value = 40
    with pytest.raises(dataclasses.FrozenInstanceError):
        measure.unit = unitmeasure.UnitDuration.minutes