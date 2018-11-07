def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            out.extend(splaszcz(element))
            # for el in wynik:
            #     out.append(el)
        else:
            out.append(element)
    return out


def test_splaszcz_niezagniezdzona_lista():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]


def test_splaszcz_jedno_zagniezdzenie():
    lista = [1, [2, 3]]
    assert splaszcz(lista) == [1, 2, 3]


def test_splaszcz_zagniezdzona_lista():
    lista = [1, 2, 3, [4, 5, [6]], 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]

# assert isinstance(lista[0], int)  # 1
# assert isinstance(lista[3], int)  # [4, 5, [6]]
