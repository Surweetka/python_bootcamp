import json

try:
    with open('pracownicy.json', 'r') as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

wybor = input("Co chcesz zrobić? [d - dodaj, w - wypisz]   ")
if wybor == "d":
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownicy.append({'imie': imie, 'nazwisko': nazwisko, 'rok_urodzenia': rok_urodzenia, 'pensja': pensja})
    with open('pracownicy.json', 'w')as plik:
        json.dump(pracownicy, plik)
if wybor == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"{(nr)} {p(imie)} {p(nazwisko)} - wiek: {p(rok_urodzenia)}, pensja: {p(pensja)} PLN")
