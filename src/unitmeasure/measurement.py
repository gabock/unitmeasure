
from unitmeasure.unit import Unit


class Measurement(object):
    
    __slots__ = ["unit", "value"]

    def __init__(self, value, unit):
        super().__setattr__("value", value)
        super().__setattr__("unit", unit)

    def __setattr__(self, *args):
        raise TypeError("'Measurement' object doesn't support item assignment")

    def __delattr__(self, *args):
        raise TypeError("'Measurement' object doesn't support item deletion")