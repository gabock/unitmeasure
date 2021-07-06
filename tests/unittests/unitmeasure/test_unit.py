import pytest

import unitmeasure

def test_unit_symbol():
    unit = unitmeasure.Unit("s")
    assert unit.symbol == "s"