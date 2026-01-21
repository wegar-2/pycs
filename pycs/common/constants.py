from pycs.common.types import Encoding


ENCODING_TO_MAX_BITS_PER_CHARACTER: dict[Encoding, int] = {
    "utf8": 32,
    "ascii": 7
}
