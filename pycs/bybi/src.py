from pathlib import Path

from pycs.common.types import Encoding
from pycs.common.constants import ENCODING_TO_BITS_PER_CHARACTER

from bitarray import bitarray

__all__ = [
    "bitarray_to_binary_str",
    "encode_str_to_bitarray",
    "encode_symbol_to_bitarray"
]


def encode_symbol_to_bitarray(symbol: str, encoding: Encoding) -> bitarray:
    if len(symbol) != 1:
        raise ValueError(
            f"Passed string of length != 1 to symbol_to_bitarray: {symbol=}")
    encoding_size: int = ENCODING_TO_BITS_PER_CHARACTER[encoding]
    l_bytes: bytes = symbol.encode(encoding)
    ba: bitarray = bitarray([0] * encoding_size)
    for i, byte_ in enumerate(l_bytes):
        ba[8*i:8*(i+1)] = bitarray(bin(byte_)[2:])
    return bitarray([0] * (encoding_size - 8 * len(l_bytes)) + list(ba))


def encode_str_to_bitarray(s: str, encoding: Encoding) -> bitarray:
    bits_per_character: int = ENCODING_TO_BITS_PER_CHARACTER[encoding]
    ba: bitarray = bitarray(bits_per_character*len(s))
    for i in range(len(s)):
        ba[bits_per_character*i:bits_per_character*(i+1)] = (
            encode_symbol_to_bitarray(symbol=s[i], encoding=encoding))
    return ba


def decode_bitarray_to_str(ba: bitarray, encoding: Encoding) -> str:
    pass


def bitarray_to_binary_str(ba: bitarray) -> str:
    return "".join([str(x) for x in ba])


def file_to_binary_str(
    source_file: Path,
    target_file: Path,
    source_enc: Encoding,
    target_enc: Encoding
):
    pass


if __name__ == "__main__":
    print("halt!")
