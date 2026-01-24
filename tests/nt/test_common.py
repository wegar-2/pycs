from pycs.nt.common import (
    get_ith_last_remainder_of_number_repr,
    get_nn_len_at_base,
    to_base
)


def test_get_nn_len_at_base2():
    assert get_nn_len_at_base(n=11, radix=2) == 4
    assert get_nn_len_at_base(n=191, radix=2) == int(191).bit_length()


def test_get_nn_len_at_base3():
    assert get_nn_len_at_base(n=11, radix=3) == 3


def test_get_nn_len_at_base10():
    assert get_nn_len_at_base(n=11, radix=10) == 2
    assert get_nn_len_at_base(n=191, radix=10) == 3
    assert get_nn_len_at_base(n=3290, radix=10) == 4


def test_get_nn_len_at_base17():
    assert get_nn_len_at_base(n=191, radix=10) == 3
    assert get_nn_len_at_base(n=17**4, radix=10) == 5


def test_get_ith_last_remainder_of_number_repr_at_base2():
    # nn_str: str = "101011"
    # nn: int = int(nn_str, 2)
    # for i in range(len(nn_str) - 1, -1, -1):
    #     assert nn_str[i]
    pass


def test_get_ith_last_remainder_of_number_repr_at_base3():
    pass


def test_get_ith_last_remainder_of_number_repr_at_base10():
    pass


def test_get_ith_last_remainder_of_number_repr_at_base17():
    pass


def test_to_base2():
    assert to_base(n=11, r=2) == "1011"
    assert to_base(n=32, r=2) == "100000"


def test_to_base3():
    assert to_base(n=3, r=3) == "10"
    assert to_base(n=9, r=3) == "100"
    assert to_base(n=17, r=3) == "122"
    assert to_base(n=81, r=3) == "10000"


def test_to_base10():
    assert to_base(n=11, r=10) == "11"
    assert to_base(n=32, r=10) == "32"
    assert to_base(n=99999, r=10) == "99999"
    assert to_base(n=3290, r=10) == "3290"


def test_to_base17():
    pass
