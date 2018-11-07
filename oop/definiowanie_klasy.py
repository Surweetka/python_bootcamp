class Animal:
    krolestwo = "Fauna"

    def __init__(self, nazwa):
        self.nazwa = nazwa


a1 = Animal("Zyrafa")
a2 = Animal("Mysz")

print(a1.krolestwo)
print(a2.krolestwo)

# print(type(mysz))
#
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# Animal.krolestwo = "Flora"
#
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# zyrafa.krolestwo = "Fauna"
#
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)