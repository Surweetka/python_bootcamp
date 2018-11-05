def policz_znaki(napis, start="<", end=">"):
    ile_znakow = 0
    poziom = 0

    for znak in napis:
        ile_znakow += poziom
        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        else:
            ile_znakow += poziom

    return ile_znakow


def test_policz_znaki_bez_znacznikow():
    assert policz_znaki("ala ma kota a kot ma ale") == 0


def test_policz_znaki_jeden_poziom_zaglebienia_standardowe_znaczniki():
    assert policz_znaki("ala ma <kota> a kot ma ale") == 4


# def test_policz_znaki_jeden_poziom_zaglebienia_niestandardowe_znaczniki():
#     assert policz_znaki("ala [kota [a kot]] ma [ale]", "[", "]") == 18
#     assert policz_znaki("ala [kota [a kot]] ma [ale]", start="[", end="]") == 18


# def test_policz_znaki_satndardowe_znaczniki_wiele_poziomow():
#     assert policz_znaki("a <a<a<a>>>") == 6
