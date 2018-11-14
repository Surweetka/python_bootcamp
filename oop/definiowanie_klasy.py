# class Animal:
#     krolestwo = "Fauna"
#
#     def __init__(self, nazwa):
#         self.nazwa = nazwa
#
#
# a1 = Animal("Zyrafa")
# a2 = Animal("Mysz")
#
# print(a1.krolestwo)
# print(a2.krolestwo)
#
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
#
# class NaszaKlasa():
#     x = 4
#     y = 2
#
# obiekt = NaszaKlasa()
# obiekt2 = NaszaKlasa()
#
# obiekt2.x = 134

class Osoba():
    imie = "Jan"
    nazwisko = "Kowalski"

    def __init__(self, imie, nazwisko):
        print("No siema")
        self.imie = imie
        self.nazwisko = nazwisko


    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statyczna():
        print("Metoda statyczna")

obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "Mickiewicz")

obiekt.przedstaw_sie()
obiekt2.przedstaw_sie()
Osoba.metoda_statyczna()