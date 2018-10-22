liczby = [5, 2, 1, 4, 3]
# indexy = [0, 1, 2, 3, 4]

# assert False
# assert True

min_ = liczby[0]
max_ = liczby[0]

for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_


print("Wartości: ", min_, max_)
print("Indexy: ", liczby.index(min_), liczby.index(max_))

x = liczby[2]
y = liczby[0]


for i in range(len(liczby)):
    print(liczby[i])

# assert liczby == [1, 2, 5, 4, 3]
