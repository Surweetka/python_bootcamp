napis = str(input("Podaj napis z <>: "))
znaki = 0
licz = False

for x in napis:
    if x == "<":
        licz = True
    elif x == ">":
        break
    elif licz == True:
        znaki += 1
print(f"W nawiasie <> znajduje się {znaki} znaków")
