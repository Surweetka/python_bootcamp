a = float(input("Podaj liczbę: "))
b = (a>10)
c = (a<=15)
d = ((a%2)==0)
print(f"Większa od 10: {b}")
print(f"Mniejsza równa 15: {c}")
print(f"Podzielna przez 2: {d}")

print(f"Podzielna przez 3 i większa od 10: {a%3 == 0 and a > 10}")
print(f"Większa od 10 lub podzielna przez 5: {a > 10 or a%5 == 0}")
