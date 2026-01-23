from bitarray import bitarray
from pycs.common.constants import GERMAN_LETTERS, POLISH_LETTERS

from pycs.bybi.src import (
    bitarray_to_binary_str,
    encode_symbol_to_bitarray,
    decode_bitarray_symbol_repr
)


def test_bitarray_to_binary_str():
    assert bitarray_to_binary_str(ba=bitarray([0, 1, 0, 0, 1, 0, 1])) == "0100101"


def test_symbol_to_bitarray_on_ascii_symbol():
    symbol: str = "q"
    symbol_ba: bitarray = encode_symbol_to_bitarray(symbol=symbol, encoding="ascii")
    assert ord(symbol) == int("".join([str(x) for x in symbol_ba]), base=2)


def test_encode_decode_symbol_ascii():
    t_ba: bitarray = encode_symbol_to_bitarray(symbol="t", encoding="ascii")
    t_recov: str = decode_bitarray_symbol_repr(ba=t_ba, encoding="ascii")
    assert len(t_recov) == 1
    assert "t" == t_recov


def test_encode_decode_symbol_utf8():
    polish_a_ba: bitarray = encode_symbol_to_bitarray(symbol="ą", encoding="utf8")
    polish_a_recov: str = decode_bitarray_symbol_repr(ba=polish_a_ba, encoding="utf8")
    assert "ą" == polish_a_recov


def test_encode_decode_polish_alphabet_utf8():
    for letter in POLISH_LETTERS:
        letter_ba: bitarray = encode_symbol_to_bitarray(letter, "utf8")
        letter_recov: str = decode_bitarray_symbol_repr(letter_ba, "utf8")
        assert len(letter_recov) == 1
        assert letter_recov == letter


def test_encode_decode_german_alphabet_utf9():
    for letter in GERMAN_LETTERS:
        letter_ba: bitarray = encode_symbol_to_bitarray(letter, "utf8")
        letter_recov: str = decode_bitarray_symbol_repr(letter_ba, "utf8")
        assert len(letter_recov) == 1
        assert letter_recov == letter
