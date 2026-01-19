from pathlib import Path

from pycs.common import Encoding

from bitarray import bitarray

__all__ = [
    "str_to_bitarray"
]


def str_to_bitarray(s: str, encoding: Encoding) -> bitarray:
    s_enc: bytes = s.encode(encoding=encoding)
    ba: bitarray = bitarray(8*len(s_enc))
    for i, byte in enumerate(s_enc):
        ba[8*i:8*(i+1)] = bitarray(f"{byte:08b}")
    return ba


def encode_file_as(
        source_file: Path,
        target_file: Path,
        source_enc: Encoding,
        target_enc: Encoding
) -> None:
    pass


def binary_encode_file() -> None:
    pass


if __name__ == "__main__":
    res = str_to_bitarray(s="a", encoding="ascii")

    print("halt! ")
