from pycs.nt.common import (
    symbol_at_base,
    get_nn_len_at_base,
    to_base
)


def test_get_nn_len_at_base2():
    assert get_nn_len_at_base(n=11, b=2) == 4
    assert get_nn_len_at_base(n=191, b=2) == int(191).bit_length()


def test_get_nn_len_at_base3():
    assert get_nn_len_at_base(n=11, b=3) == 3


def test_get_nn_len_at_base10():
    assert get_nn_len_at_base(n=11, b=10) == 2
    assert get_nn_len_at_base(n=191, b=10) == 3
    assert get_nn_len_at_base(n=3290, b=10) == 4


def test_get_nn_len_at_base17():
    assert get_nn_len_at_base(n=191, b=10) == 3
    assert get_nn_len_at_base(n=17**4, b=10) == 5


def test_get_ith_last_remainder_of_number_repr_at_base2():
    nn_str: str = "101011"
    nn_str_rev: str = nn_str[::-1]
    nn: int = int(nn_str, 2)
    for i in range(len(nn_str)):
        assert (
                nn_str_rev[i] ==
                symbol_at_base(nn, 2, i + 1)
        )


def test_get_ith_last_remainder_of_number_repr_at_base3():
    nn_str: str = "121202"
    nn_str_rev: str = nn_str[::-1]
    nn: int = int(nn_str, base=3)
    for i in range(len(nn_str)):
        assert (
                nn_str_rev[i] ==
                symbol_at_base(nn, 3, i + 1)
        )


def test_get_ith_last_remainder_of_number_repr_at_base10():
    nn_str: str = "653911"
    nn_str_rev: str = nn_str[::-1]
    nn: int = int(nn_str)
    for i in range(len(nn_str)):
        assert (
                nn_str_rev[i] ==
                symbol_at_base(nn, 10, i + 1)
        )


def test_get_ith_last_remainder_of_number_repr_at_base17():
    nn_str: str = "GFEDCB12"
    nn_str_rev: str = nn_str[::-1]
    nn: int = (
        2 * 17**0 +
        1 * 17**1 +
        11 * 17**2 +
        12 * 17**3 +
        13 * 17**4 +
        14 * 17**5 +
        15 * 17**6 +
        16 * 17**7
    )
    for i in range(len(nn_str)):
        assert (
                nn_str_rev[i] ==
                symbol_at_base(nn, 17, i + 1)
        )


def test_get_ith_last_remainder_of_number_repr_



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
    assert to_base(n=10, r=17) == "A"
    assert to_base(n=16, r=17) == "G"
    assert to_base(n=17, r=17) == "10"
    assert to_base(n=17**2, r=17) == "100"
