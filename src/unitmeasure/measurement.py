
from dataclasses import dataclass

from unitmeasure.unit import Unit

@dataclass(frozen=True)
class Measurement(object):
    value: float
    unit: Unit