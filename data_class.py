from dataclasses import dataclass, field

# We can solve this in two ways:

# First Method: replace the default field value with a call to the provided field() function.


@dataclass
class Ford:
    models: list = field(default_factory=list)


vehicle = Ford()
vehicle.models += ["F-150", "Mustang"]
print(vehicle)

# Second Method: As default_factory must be a zero-argument callable,
# it will be called when a default value is needed for this field.
# Here default_factory is not a 0-argument callable but a list,
# which is generating error. So, we can use lambda here.


@dataclass
class Ford:
    models: list = field(default_factory=lambda: ["F-150", "Mustang"])


vehicle = Ford()
print(vehicle)
