

class UnitConverter(object):
    """Describe how to convert a unit to and from the base unit of its dimension.

    The methods of this class define the interface for performing conversions
    to and from the base unit of a unit's dimension.

    The default implementation simply returns the value.
    Methods are implemented differently depending on the type of conversion.

    When creating a custom unit converter, BOTH methods must be implemented to 
    define the conversion to and from a value in terms of a unit.
    """
    def baseUnitValue(self, fromValue):
        """This method takes a value in terms of a unit and returns the corresponding value in terms of the base unit.
        """
        return fromValue

    def value(self, fromBasUnitValue):
        """This method takes in a value in terms of the base unit and returns the equialent value in terms of the unit.
        """
        return fromBasUnitValue


class Unit(object):

    def __init__(self, symbol):
        self.symbol = symbol

