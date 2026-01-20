from typing import Annotated, Literal, TypeAlias, Union

from annotated_types import Ge, Gt


NonNegInt: TypeAlias = Annotated[int, Ge(0)]
PosInt: TypeAlias = Annotated[int, Gt(0)]
Encoding: TypeAlias = Literal["utf8", "ascii"]

NumeralSystem = Literal["binary", "decimal"]

Number: TypeAlias = Union[int, float]

Immutable: TypeAlias = Union[int, str, bool, bytes, tuple]

ENCODING_TO_MAX_BITS_PER_CHARACTER: dict[Encoding, int] = {
    "utf8": 32,
    "ascii": 7
}
