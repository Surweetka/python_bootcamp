ile3_5 = 0
for x in range(0, 101):
    if x % 3 == 0:
        ile3_5 += 1

    elif x % 5 ==0:
        ile3_5 += 1

print(f"W przedziale 0-100 jest {ile3_5} liczb podzielnych przez 3 lub 5.")
