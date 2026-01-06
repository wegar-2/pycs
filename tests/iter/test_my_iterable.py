from pycs.iter.my_iterable import MyIterable


def test_my_iterable():
    data = [1, 5, 2, 908, 43, 555]
    myi = MyIterable(data=data)

    data_recovered = []
    for x in myi:
        data_recovered.append(x)

    assert data == data_recovered
