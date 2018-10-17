from random import randint

x = randint(1, 10)
y = randint(1, 10)
skarbX = randint(1, 10)
skarbY = randint(1, 10)
print(f"{skarbX}, {skarbY}")
while x < 10 or y < 10 or x < 1 or y < 1:
    print(f"Pozycja gracza: [{x}, {y}]")
    r = str(input("Podaj kierunek ruchu [W A S D]: "))

    minKrokowPrzed = abs(skarbX - x) + abs(skarbY - y)

    if r == "w":
        y += 1
    elif r == "s":
        y -= 1
    elif r == "a":
        x -= 1
    elif r == "d":
        x += 1

    wskazowka = randint(1, 5)
    if wskazowka != 3:


    minKrokowPo = abs(skarbX - x) + abs(skarbY - y)

    if minKrokowPrzed > minKrokowPo:
        print("Zbliżasz się.")

    if minKrokowPrzed < minKrokowPo:
        print("Oddalasz się.")

    if x < 1 or x > 10 or y < 1 or y > 10:
        print("Spadłeś z planszy. Koniec gry.")
        break
    if minKrokowPo == 0:
        print("Brawo znalazłeś skarb!")
        break
