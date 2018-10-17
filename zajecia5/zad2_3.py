lista = [1, -3, 9, 10, 15, 3, -2, 5, -4]
dodatnie = 0
ujemne = 0

for x in lista:
    if x < 0:
        ujemne += 1
    elif x > 0:
        dodatnie +=1

print(f"Ilość liczb dodatnich: {dodatnie}")
print(f"Ilość liczb ujemnych: {ujemne}")
