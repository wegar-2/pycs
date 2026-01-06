import math
from typing import Final

from pycs.common.types import NumeralSystem, Number


def make_input_sizes(
        exponents: list[Number] | None = None,
        ns: NumeralSystem = "decimal"
) -> list[int]:

    system_to_base: Final[dict[NumeralSystem, int]] = {
        "binary": 2,
        "decimal": 10
    }

    if exponents is None:
        if ns == "decimal":
            exponents = [0, 1, 2, 2.5, 3, 3.33, 3.67, 4]
        else:
            exponents = [0, 1, 2, 5, 8, 10, 12, 14]

    return [math.floor(system_to_base[ns]**e) for e in exponents]


def do_repeated_runs():
    pass
