# Otworzenie pliku do odczytu

with open("nwm/input.txt") as f:
    for linia in f:
        if len(linia) > 600:
            print(linia)

# tryb do odczytu

with open("info.txt", "w", encoding="utf8") as f:
    for i in range(10):

        f.write("Jakiś tekst\n")

with open("info.txt", "a", encoding="utf8") as f:
    f.write("Inny tekst")

f = open("nwm/input.txt")

f.close()

# print(f.read())
