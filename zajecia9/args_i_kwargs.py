# def foo(pierwszy, *reszta):
#     # print("pierwszy: ", pierwszy)
#     # print("reszta: ", reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#     return pierwszy
#
#
# print(foo(1))
# print(foo(1, 2))
# print(foo(1, 2, 5, 10, 15))
#
# reszta = [1, 2, 5, 10, 15]
# print(*reszta)
#
#
# def druga_funkcja(**slownik):
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "Żaden warunek nie był spełniony."
#
# print(druga_funkcja())
# druga_funkcja(a=2)
# druga_funkcja(a=2, b=2, c=3, d=4)
# druga_funkcja(a=2, b=2, c=3, d=4, zosia=5, adas=15)
#
#
# co_na_co = {
#     "Ala": "Kot",
#     "kota": "Alę"
# }
#
#
# "Ala ma kota" -> "Kot ma Alę"
#
# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#
#     return jakis_tekst
#
#
# print(zamien("Ala ma kota", Ala="Kot", kota="Alę"))
# print(zamien("Ala ma kota", ma="bije"))
# print(zamien("Ala ma kota", **co_na_co))
#
# slownik = dict(a=1, b=2, ma="bije")
# print(slownik)

napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajecia z $przedmiot zostały odwołane"

zmien = {
    "$produkt": "Samochod",
    "$cena": "20000",
    "$przedmiot": "Fizyki"
}


def formatuj(napis, **zmien):
    for klucz in zmien:
        napis = napis.replace("$" + klucz, zmien[klucz])
    print(napis)
    return napis


assert formatuj(napis, produkt="Samochod", cena="20000") == "Ten Samochod kosztuje 20000"
assert formatuj(napis2, przedmiot="Fizyki") == "Zajecia z Fizyki zostały odwołane"
