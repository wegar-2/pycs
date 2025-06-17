from typing import Annotated, TypeAlias
from annotated_types import Ge, Gt


NonNegInt: TypeAlias = Annotated[int, Ge(0)]
PosInt: TypeAlias = Annotated[int, Gt(0)]
