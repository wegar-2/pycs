from typing import Annotated, Literal, TypeAlias, Union

from annotated_types import Ge, Gt


NonNegInt: TypeAlias = Annotated[int, Ge(0)]
PosInt: TypeAlias = Annotated[int, Gt(0)]
Encoding: TypeAlias = Literal["utf8", "ascii"]

NumeralSystem = Literal["binary", "decimal"]

Number: TypeAlias = Union[int, float]