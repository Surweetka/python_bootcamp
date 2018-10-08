# To jest komentarz
"""
Utwórz zmienne a i b, przypisz im jakieś wartości liczbowe

Utwórz zmienną
pole_prostokata i przypisz do niej formułę liczącą te pole

Wypisz na wyjście standardowe tekst np:
Pole prostokąta o bokach: 2, 3 wynosi: 6

Wypisz też na konsoli tekst dokładnie taki jak poniżej
"To jest tekst w cudzysłowiu"

ctrl + / bierze zaznaczone w komentarz


"""
# a = 3
# b = 4
# pole_prostokata = a * b
# print("Pole prostokąta o bokach: "+str(a)+", "+str(b)+" wynosi: "+str(pole_prostokata))
# print(f"Pole prostokąta o bokach: {a}, {b} wynosi: {pole_prostokata}")
# print('"To jest tekst w cudzysłowiu"')
# print("""To
#  jest
#   wielolinijkowy
#    tekst""")


a = int(input("Podaj bok a "))
b = int(input("Podaj bok b "))
pole_prostokata = a * b
print(f"Pole prostokąta o bokach {a}, {b} wynosi: {pole_prostokata}")
