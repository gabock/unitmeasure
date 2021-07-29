import pytest

import unitmeasure

def test_immutable():
    measure = unitmeasure.Measurement(value=60, unit=unitmeasure.UnitDuration.seconds)
    with pytest.raises(TypeError):
        measure.value = 40
    with pytest.raises(TypeError):
        measure.unit = unitmeasure.UnitDuration.minutes