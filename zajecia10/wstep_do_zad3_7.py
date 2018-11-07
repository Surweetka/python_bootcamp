lista = [1, 2, 3, 4, 5, 6]

# warunek jest taki, ze wieksze niz 3

out = [False, False, False, True, True, True]


def bigger_than_3(liczba):
    if liczba > 3:
        return True
    return False


def smaller_than_3(liczba):
    if liczba < 3:
        return True
    return False


def sprawdzam_czy_wieksze_niz_3(lista):
    out = []
    for element in lista:
        # if element > 3:
        #     out.append(True)
        # else:
        #     out.append(False)
        out.append(bigger_than_3(element))
    return out


def sprawdzam_czy(lista, warunek):
    for element in lista:
        out.append(warunek(element))
    return out


# x = lambda x: x == 5

assert sprawdzam_czy_wieksze_niz_3(lista) == out
assert sprawdzam_czy(lista, bigger_than_3) == out
# assert sprawdzam_czy(lista, lambda x: x == 5) == [False, False, False, False, True, False]