znalezione_max = None
znalezione_min = None
# None jest wartością różną do dowolnej liczby

while True:
    wejscie = input("Podaj liczbe: ")

    if (wejscie == "koniec"):
        break

    x = int(wejscie)
    if znalezione_max is None or x > znalezione_max:
        znalezione_max = x
    if znalezione_min is None or x < znalezione_min:
        znalezione_min = x

if znalezione_max is None:
    print("Nie wprowadzono danych")
else:
    print(f"max: {znalezione_max} min: {znalezione_min}")
