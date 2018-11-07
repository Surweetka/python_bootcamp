# data = [1, 2, 3, 4, 5, 6, 7]
#
#
# def przytnij(data):
#     out = []
#     for element in data:
#         if element > 3 and element <= 6:
#             out.append(element)
#         return out
#
#
# def test_tnij_liste():
#     data = [1, 2, 3, 4, 5, 6, 7]
#     start = lambda x: x > 3
#     stop = lambda x: x == 6
#
#
# def test_tnij_3_do_6():
#     assert przytnij(data) == [3, 4, 5]

def przytnij(data, start, stop):
    result = []
    dodwac_do_listy = False
    for element in data:
        if start(element):
            dodwac_do_listy = True
        if dodwac_do_listy:
            result.append(element)
        if stop(element):
            break

    return result


def test_przytnij():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    ) == [4, 5, 6]
