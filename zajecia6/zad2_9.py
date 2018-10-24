produkty = {
    "pomidor": 3,
    "ziemniaki": 2,
    "cebula": 1.5,
    "piwo": 2.5
}
magazyn = {
    "pomidor": 10,
    "ziemniaki": 10,
    "cebula": 10,
    "piwo": 10
}

print("W naszym sklepie ofertujemy: ")
for produkt in produkty:
    print(f" - {produkt} - w cenie {produkty[produkt]} PLN")

sumarycznie = 0
koszyk = {}

print()
while True:
    komenda = input("""Wybierz opcje:
     [d] - dodaj do magazynu
     [k] - kup
     [z] - zakończ
     """)
    if komenda == "k":
        wybor_produktu = input("Który produkt chcesz kupić? (wpisz stop żeby zakończyć zakupy) ")
        if wybor_produktu == "stop":
            break
        if wybor_produktu in produkty:
            ile = input(f"Ile chcesz kupić [{wybor_produktu}]? ")
            if ile <= magazyn[wybor_produktu]:
                koszyk[wybor_produktu] = ile
            else:
                print(f"Przykro mi, nie mam tyle tego produktu! Pozostało [{magazyn}]")
            # cena = int(ile) * produkty[wybor_produktu]
            koszyk[wybor_produktu] = cena
        else:
            print("Sorry nie mam takiego produktu.")
    elif komenda == "d":
        co = input("Jaki produkt chcesz dodać? ")
        ile = input(f"Ile {co} chcesz dodać? ")
        magazyn[co] = magazyn[co] + ile
        if co not in produkty:
            cena = float(input(f"Jaka cena za {co}"))
            produkty[co] = cena
    elif komenda == "z":
        break
    # wybor_produktu = input("Który produkt chcesz kupić? (wpisz stop żeby zakończyć zakupy) ")
    # if wybor_produktu == "stop":
    #     break
    # if wybor_produktu in produkty:
    #     ile = input(f"Ile chcesz kupić [{wybor_produktu}]? ")
    #     if ile <= magazyn[wybor_produktu]:
    #         koszyk[wybor_produktu] = ile
    #     else:
    #         print(f"Przykro mi, nie mam tyle tego produktu! Pozostało [{magazyn}]")
    #     # cena = int(ile) * produkty[wybor_produktu]
    #     koszyk[wybor_produktu] = cena
    # else:
    #     print("Sorry nie mam takiego produktu.")

print()
print("-" * 40)

print("Twój rachunek: ")
for produkt in koszyk:
    cena = int(koszyk[produkt]) * produkty[produkt]
    print(f" - {produkt}: {koszyk[produkt]} PLN")
    sumarycznie += float(koszyk[produkt])
print("=" * 40)
print(f"Suma: {sumarycznie} PLN")
