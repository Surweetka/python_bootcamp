lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0

# print(*lista1, sep="  ")

# for i in lista1:
#     print(f"{i:3}", end="")
# print()
# while x < 10:
#     for i in lista1:
#         print(lista1[i], lista1[0] * i, lista1[1] * i, lista1[2] * i, lista1[3] * i, lista1[4] * i, lista1[5] * i,
#               lista1[6] * i, lista1[7] * i, lista1[8] * i, lista1[9] * i)
#         x += 1

print("   ", end="")
for x in range(10):
    print(f"{x:3}", end="")

print()
print()

for x in range(10):
    print(x, end="  ")
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()
