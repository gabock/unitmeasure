from unitmeasure import dimension
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

    @property
    def description(self):
        return f"{self.value} {self.unit.symbol}"

    @property
    def debugDescription(self):
        return f"{self.value} {self.unit.symbol}"

    def converted(self, otherUnit):
        """Returns a new measurement createdby converting to the provided unit.

        Args:
            otherUnit: a unit of the same `Dimension`

        Returns: 
            A converted measurement
        """
        if not isinstance(self.unit, dimension.Dimension):
            raise TypeError(
                "unit must be a Dimension to be able to convert between the kinds of units in a dimension"
            )
        if self.unit == otherUnit:
            return Measurement(self.value, self.unit)
        value_in_base = self.unit.converter.baseUnitValue(self.value)
        if otherUnit == self.unit.baseUnit():
            return Measurement(value_in_base, otherUnit)
        other_value_from_base = otherUnit.converter.value(value_in_base)
        return Measurement(other_value_from_base, otherUnit)

    def convert(self, otherUnit):
        temp = self.converted(otherUnit)
        super().__setattr__("value", temp.value)
        super().__setattr__("unit", temp.unit)

    def __eq__(self, other):
        if self.unit == other.unit:
            return self.value == other.value
        if isinstance(self.unit, dimension.Dimension) and isinstance(
                other.unit, dimension.Dimension):
            if self.unit.baseUnit() == other.unit.baseUnit():
                lhs_value_in_base = self.unit.converter.baseUnitValue(
                    self.value)
                rhs_value_in_base = other.unit.converter.baseUnitValue(
                    other.value)
                return lhs_value_in_base == rhs_value_in_base
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.debugDescription

    def __str__(self):
        return self.__repr__()
