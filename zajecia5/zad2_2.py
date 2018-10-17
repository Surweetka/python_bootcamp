zbior = []

while len(zbior) < 10:
    x = input("Podaj liczbę: ")
    if x == "k":
        break
    liczba = int(x)
    zbior.append(liczba)

if len(zbior) == 0:
    print("Nie podano danych!")
else:
    srednia = sum(zbior) / len(zbior)
    print(f"Średnia to: {srednia}")
