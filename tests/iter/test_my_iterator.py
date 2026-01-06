from pycs.iter.my_iterator import MyData


def test_my_iterator():
    data = ["q", 908, 34.12, True, "abbbab", 5, 3, 2]
    my_data = MyData(data)

    data_recovered = []
    for el in my_data:
        data_recovered.append(el)

    assert data == data_recovered
    