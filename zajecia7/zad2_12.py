lista = [5, 3, 4, 1, 2]

print("Liczby przed: ", lista)

for indeks_pods in range(len(lista)):
    indeks_min_wart = indeks_pods
    for indeks_ogona in range(indeks_pods + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wart]:
            indeks_min_wart = indeks_ogona
    # value_temp = lista[indeks_min_wart]
    # lista[indeks_min_wart] = lista[indeks_pods]
    # lista[indeks_pods] = value_temp

    lista[indeks_min_wart], lista[indeks_pods] = lista[indeks_pods], lista[indeks_min_wart]

print("Liczby po: ", lista)
assert lista == [1, 2, 3, 4, 5]
