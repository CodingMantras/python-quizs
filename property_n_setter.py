class Total:
    def __init__(self):
        # private attribute
        self._amount = None

    # Built-in @property decorator makes usage of
    # getter and setters easier.
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        # Just an example use case, not necessary to implement.
        if val < 0:
            raise ValueError("Amount can't be lower than zero(0)")
        self._amount = val


v1 = Total()
v1.amount = 30
print(v1.amount)    # Output: 30

v2 = Total()
v2.amount = -5
# Raise value error
