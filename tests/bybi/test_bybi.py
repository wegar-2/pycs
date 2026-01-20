from pycs.bybi.src import encode_str_to_bitarray, bitarray_to_binary_str
from string import ascii_letters
from bitarray import bitarray


def test_str_to_bitarray():
    a_bits = encode_str_to_bitarray(s="a", encoding="ascii")
    assert a_bits == bitarray("01100001")


def test_str_to_bitarray_on_ascii():
    for l in ascii_letters:
        assert encode_str_to_bitarray(l, "ascii") == bitarray(
            bin(ord(l))[2:].rjust(8, "0"))


def test_bitarray_to_binary_str():
    assert bitarray_to_binary_str(ba=bitarray([0, 1, 0, 0, 1, 0, 1])) == "0100101"
