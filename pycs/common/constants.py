from pycs.common.types import Encoding


ENCODING_TO_BITS_PER_CHARACTER: dict[Encoding, int] = {
    "utf8": 32,
    "ascii": 8
}
