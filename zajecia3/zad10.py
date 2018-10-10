a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = input("Podaj rodzaj operacji: ")
if c == "+":
    w = a + b
elif c == "-":
    w = a - b
elif c == "*":
    w = a * b
elif c == "/":
    if b == 0:
        w = ("Nie można tego obliczyć.")
    if b != 0:
        w = a / b

d = (f"Wynik to {w}.")
print(d)
