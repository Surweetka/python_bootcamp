# napis = "Ala ma kota D".lower()
# print(napis[0])
# print("d" in napis)
# print("D" in napis)
#
# for litera in napis:
#     print(litera.upper(), end="")

napis = str(input("Podaj słowo lub zdanie: "))
napis = napis.lower()
samogloski = ["a", "e", "i", "o", "u", "y"]

x = 0

for litera in napis:
    if litera in samogloski:
        x += 1
print(f"W napisie jest {x} samogłosek")
