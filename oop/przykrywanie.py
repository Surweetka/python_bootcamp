class Square:
    def __init__(self, a):
        self.a = a
        self.field = self.a ** 2

    def __add__(self, other):
        print(isinstance(other, Square))
        return self.field + other.field

    def __mul__(self, other):
        # print(isinstance(other, Square))
        return self.field * other.field

    def add_fields(self, other):
        return self.field + other.field


kw1 = Square(2)
kw2 = Square(3)

print(kw1.field)
print(kw2.field)
print(dir(kw1))
print(kw1.add_fields(kw2))

# + - __add__
# - - __sub__
# * - __mul__
# / - __div__

assert kw1 + kw2 == 13
assert kw1.__add__(kw2) == 13

print(isinstance(kw1, Square))