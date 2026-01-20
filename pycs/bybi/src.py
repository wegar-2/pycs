from pathlib import Path

from pycs.common import Encoding, ENCODING_TO_MAX_BITS_PER_CHARACTER

from bitarray import bitarray

__all__ = [
    "bitarray_to_binary_str",
    "encode_str_to_bitarray"
]


def encode_str_to_bitarray(s: str, encoding: Encoding) -> bitarray:
    s_enc: bytes = s.encode(encoding=encoding)
    bits_per_character: int = ENCODING_TO_MAX_BITS_PER_CHARACTER[encoding]
    ba: bitarray = bitarray(bits_per_character*len(s))
    for i, byte in enumerate(s_enc):
        ba[bits_per_character*i:bits_per_character*(i+1)] = bitarray(f"{byte:08b}")


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

    encode_str_to_bitarray(s="asdf qwerty śćęrt", encoding="utf8")

    print("halt!")
