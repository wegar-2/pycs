from pycs.bybi.src import str_to_bitarray
from string import ascii_letters
from bitarray import bitarray


def test_str_to_bitarray():
    a_bits = str_to_bitarray(s="a", encoding="ascii")
    assert a_bits == bitarray("01100001")


def test_str_to_bitarray_on_ascii():
    for l in ascii_letters:
        assert str_to_bitarray(l, "ascii") == bitarray(
            bin(ord(l))[2:].rjust(8, "0"))
