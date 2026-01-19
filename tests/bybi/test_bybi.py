from pycs.bybi.src import str_to_bitarray
from string import ascii_letters
from bitarray import bitarray


def test_str_to_bitarray():
    a_bits = str_to_bitarray(s="a", encoding="ascii")
    assert a_bits == bitarray("")


def test_str_to_bitarray_on_ascii():
    pass


def test_str_to_bitarray_on_text():
    pass
