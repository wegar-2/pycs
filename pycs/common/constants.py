from string import ascii_uppercase
from typing import Final

from pycs.common.types import Encoding

__all__ = [
    "ENCODING_TO_BITS_PER_CHARACTER",
    "GERMAN_LETTERS",
    "POLISH_LETTERS",
    "REMAINDER_TO_SYMBOL_MAP"
]


ENCODING_TO_BITS_PER_CHARACTER: dict[Encoding, int] = {
    "utf8": 32,
    "ascii": 8
}

POLISH_LETTERS: Final[str] = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"


GERMAN_LETTERS: Final[str] = "äöüÄÖÜß"


_REMAINDER_TO_SYMBOL_MAP_DECIMAL: dict[int, str] = {
    i: str(i) for i in range(2, 11, 1)
}


_REMAINDER_TO_SYMBOL_MAP_ABOVE_DECIMAL: dict[int, str] = {
    i: x for i, x in enumerate(ascii_uppercase, start=11)
}


REMAINDER_TO_SYMBOL_MAP: dict[int, str] = {
    **_REMAINDER_TO_SYMBOL_MAP_DECIMAL,
    **_REMAINDER_TO_SYMBOL_MAP_ABOVE_DECIMAL
}
