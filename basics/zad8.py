dl = float(input("Podaj długość opakowania: "))
szer = float(input("Podaj szerokość opakowania: "))
wys = float(input("Podaj wysokość opakowania: "))

obj = dl * szer * wys
print(f"Objętość opakowania to: {obj} cm^3")

print(f"Czy objętość większa od 1 litra? {obj > 1000}")
