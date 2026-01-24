from math import log, floor

from pycs.common.constants import REMAINDER_TO_SYMBOL_MAP
from pycs.common.types import Radix

__all__ = [
    "get_nn_len_at_base",
    "to_base"
]


def _validate_is_nn(n: int) -> None:
    if not n >= 0 and isinstance(n, int):
        raise ValueError(f"{n=} is not a natural number! ")


def _validate_radix(r: Radix) -> None:
    if r not in REMAINDER_TO_SYMBOL_MAP:
        raise ValueError(f"Radix {r=} is not allowed! ")


def get_nn_len_at_base(n: int, radix: Radix = 2) -> int:
    return floor(log(n, radix)) + 1


def to_base(n: int, radix: Radix) -> str:
    _validate_is_nn(n)
    _validate_radix(radix)
    str_rep: list[str] = []
    base_power_counter: int = 1
    base_power_bound: int = get_nn_len_at_base(n, radix)
    num: int = n
    while base_power_counter < base_power_bound:
        remainder: int = num % radix
        str_rep.append(REMAINDER_TO_SYMBOL_MAP[remainder])
        num = num // radix
        base_power_counter += 1
    return "".join(str_rep[::-1])
