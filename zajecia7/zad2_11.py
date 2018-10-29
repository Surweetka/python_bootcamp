# zakres = set(range(0, 100, 1))
# while True:
#     dodaj = input("Podaj liczby do dodania lub wpisz STOP żeby przerwać: ")
#     if dodaj == "STOP":
#         break

# podaj = ()
# liczby = set()
# parzyste = set(range(0, 100, 2))
# while podaj != "stop":
#     podaj = (input("Podaj liczby [stop]: "))
#     podaj = int(podaj)
#     liczby.add(podaj)
# zgodnosc = 0
# for i in liczby:
#     if i in liczby:
#         zgodnosc += 1
#
# print(zgodnosc)

liczby = set()

while True:
    komenda = input("Podaj liczbę lub wpisz K by zakończyć ")
    if komenda.lower() == "k":
        break
    else:
        liczba = int(komenda)
        liczby.add(liczba)

print(f"Unikalnych liczb: {len(liczby)}")
liczby_parzyste = set(range(0, 100, 2))
