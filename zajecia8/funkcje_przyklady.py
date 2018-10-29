# def hellow():
#     return "Hello World"
#
#
# def hello2(name):
#     print(f"Hellow {name}")
#
#
# def hello3(name="World!"):
#     print(f"Hellow {name}")


def klon(imie, wiek=18, wzrost=181):
    print(f"Witaj {imie}")
    if wiek == 18 and wzrost == 181:
        print(f"Masz standardowe parametry.")
    else:
        print(f"Różnisz się od pozostałych.")
        print("Wiek:", wiek)
        print("Wzrost:", wzrost)

klon("Adam")

klon("Adam", 20, 162)


# def dodaj(a, b):
#     return a + b


# def test_dodaj_dwie_liczby():
#     assert dodaj(1 + 2) == 3
#
#
# def test_dodaj_dwa_napisy():
#     assert dodaj("1", "2") == "12"


# hellow()
# hello2("helow!")
# hello3()
# x = print("Co tam sporotwe swiry")
# print("x:", x)
# y = dir()
# print("y:", y)
#
# z = hellow()
# print(z)
#
# wynik = dodaj(10, 11)
# wynik2 = dodaj(1.1, 20.2)
# wynik3 = dodaj("a", "b")
#
# print(wynik, wynik2, wynik3)
