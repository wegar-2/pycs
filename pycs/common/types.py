from typing import Annotated, Literal, TypeAlias, Union

from annotated_types import Ge, Gt


NonNegInt: TypeAlias = Annotated[int, Ge(0)]
PosInt: TypeAlias = Annotated[int, Gt(0)]
Encoding: TypeAlias = Literal["utf8", "ascii"]

NumeralSystem = Literal["binary", "decimal"]

Number: TypeAlias = Union[int, float]

Immutable: TypeAlias = Union[int, str, bool, bytes, tuple]

Base: TypeAlias = Literal[
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35,
]
