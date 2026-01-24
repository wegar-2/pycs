from bitarray import bitarray

from pycs.common.types import Encoding
from pycs.common.constants import ENCODING_TO_BITS_PER_CHARACTER


__all__ = [
    "decode_bitarray_str_repr",
    "decode_bitarray_symbol_repr",
    "encode_str_to_bitarray",
    "encode_symbol_to_bitarray"
]


def encode_symbol_to_bitarray(symbol: str, encoding: Encoding) -> bitarray:
    if len(symbol) != 1:
        raise ValueError(
            f"Passed string of length != 1 to symbol_to_bitarray: {symbol=}")
    encoding_size: int = ENCODING_TO_BITS_PER_CHARACTER[encoding]
    l_bytes: bytes = symbol.encode(encoding)
    ba: bitarray = bitarray([0] * 8 * len(l_bytes))
    for i, byte_ in enumerate(l_bytes):
        ba[8*i:8*(i+1)] = bitarray(f"{byte_:08b}")
    return bitarray([0] * (encoding_size - 8 * len(l_bytes)) + list(ba))


def decode_bitarray_symbol_repr(ba: bitarray, encoding: Encoding) -> str:
    bit_len_ = len(ba)
    if bit_len_ != (exp_bit_len := ENCODING_TO_BITS_PER_CHARACTER[encoding]):
        raise ValueError(
            f"Invalid length of the bitarrray: {bit_len_}; "
            f"expected bit length: {exp_bit_len}"
        )
    bytes_ = bytes([
        int("".join([str(x) for x in ba[8 * i:8 * (i + 1)]]), base=2)
        for i in range(bit_len_ // 8)
    ])
    return bytes_.lstrip(b"\00").decode(encoding)


def encode_str_to_bitarray(s: str, encoding: Encoding) -> bitarray:
    bits_per_character: int = ENCODING_TO_BITS_PER_CHARACTER[encoding]
    ba: bitarray = bitarray(bits_per_character*len(s))
    for i in range(len(s)):
        ba[bits_per_character*i:bits_per_character*(i+1)] = (
            encode_symbol_to_bitarray(symbol=s[i], encoding=encoding))
    return ba


def decode_bitarray_str_repr(ba: bitarray, encoding: Encoding) -> str:
    bit_len: int = len(ba)
    char_bit_len: int = ENCODING_TO_BITS_PER_CHARACTER[encoding]
    quot_len, remain_len = bit_len // char_bit_len, bit_len % char_bit_len
    if remain_len != 0:
        raise ValueError(
            f"Length of bitarray: {bit_len=:_} is inconsistent with the size "
            f"of the single char {char_bit_len=:_} - "
            f"yields {remain_len=:_}"
        )
    symbols: list[str] = []
    for i in range(quot_len):
        symbols.append(
            decode_bitarray_symbol_repr(
                ba=ba[char_bit_len*i:char_bit_len*(i+1)],
                encoding=encoding
            )
        )
    return "".join(symbols)
