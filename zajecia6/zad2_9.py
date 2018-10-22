produkty = {
    "pomidor": 5,
    "ziemniaki": 8,
    "cebula": 3
}

print("W naszym sklepie ofertujemy: ")

for produkt in cenakg:
    print(f" - {cenakg} - w cenie {produkty[cenakg]} PLN")

print()
wybor_produktu = input("Który produkt chcesz kupić? ")
ile = input(f"Ile chcesz kupić [{wybor_produktu}]")
cena