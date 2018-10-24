napis = input("Podaj napis: ")
napis = napis.lower()

liczniki = {}
for znaki in napis:
    if znaki != " ":
        liczniki[znaki] = liczniki.get(znaki, 0) + 1

print(liczniki)
