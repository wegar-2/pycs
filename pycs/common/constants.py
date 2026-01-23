from typing import Final

from pycs.common.types import Encoding


ENCODING_TO_BITS_PER_CHARACTER: dict[Encoding, int] = {
    "utf8": 32,
    "ascii": 8
}

POLISH_LETTERS: Final[str] = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"


GERMAN_LETTERS: Final[str] = "äöüÄÖÜß"
