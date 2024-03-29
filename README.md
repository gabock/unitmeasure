# unitmeasure: Swift units and measurement in Python

**unitmeasure** is a simple Python library that tries
to implement the features of Swift's [Units and Measurement
framework.](https://developer.apple.com/documentation/foundation/units_and_measurement)

With **unitmeasure**, you can label numeric quantities 
with physical dimensions and convert between related units.


## Contributing

For anyone looking to contribute, you can look at doing any of the following:
* Submit bugs and feature requests
* Review any documentation and create pull requests for anything from typos to new content.

## Installation

**unitmeasure** can be installed from PyPI:

```
pip install unitmeasure
```

## Overview

### Base available classes
   The basic available classes should match the classes found in swift.

* `Unit` - represents a unit that has a `symbol` to describe it.
* `Dimension` - subclass of `Unit` and has multiple child classes defining different dimensions.
* `Measurement` - Immutable. wraps a number with a unit. Supports comparison operators, addition and subtraction with another measurement, and multiplication and division with a scalar value.

### Supported Units
All supported units can be found in the units sub directory.
Any unit class can be imported directly from **unitmeasure**.

## Examples

> for more detailed usage see unit tests.

### Create a measurement
```python
import unitmeasure

dur = unitmeasure.Measurement(value=2,
                              unit=unitmeasure.UnitDuration.minutes)
print(dur)
```

### Convert a measurement
```python
import unitmeasure

dur = unitmeasure.Measurement(value=2,
                              unit=unitmeasure.UnitDuration.minutes)

dur.convert(unitmeasure.UnitDuration.seconds)
print(dur)
```

### Convert a measurement and return new object
```python
import unitmeasure

minutes = unitmeasure.Measurement(value=2,
                             unit=unitmeasure.UnitDuration.minutes)

seconds = minutes.converted(unitmeasure.UnitDuration.seconds)
print(minutes)
print(seconds)
```

### add measurements
```python
import unitmeasure

minutes = unitmeasure.Measurement(value=2,
                             unit=unitmeasure.UnitDuration.minutes)

seconds = minutes.converted(unitmeasure.UnitDuration.seconds)
# adding measurements will automagically convert the measurement  into its base unit.
print(minutes + seconds)
```

### Create a custom Unit
```python
import unitmeasure

customLengthUnit = unitmeasure.UnitLength(symbol="FLARB", coefficient=2.0)

customLength = Measurement(value=1, unit=customLengthUnit)

meters = customLength.converted(to: unitmeasure.UnitLength.meters)
```

### Converting to and from JSON

> NOTE: JSON struct should match swift's so it should be possible to import json data to/from swift.
```python
import unitmeasure

seconds = unitmeasure.Measurement(value=2,
                             unit=unitmeasure.UnitDuration.seconds)

with open("measurement.json", "w") as f:
    f.write(unitmeasure.to_json(seconds))

with open("measurement.json", "r") as f:
    # if a dimension is not specified you will end up with
    # a measurement that has a basic unit (only a symbol)
    loaded_measurement = unitmeasure.from_json(f.read(), dimension=unitmeasure.UnitDuration)
```
