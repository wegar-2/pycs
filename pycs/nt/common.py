from math import log, floor

from pycs.common.constants import REMAINDER_TO_SYMBOL_MAP
from pycs.common.types import Base

__all__ = [
    "get_nn_len_at_base",
    "digit_at_base",
    "symbol_at_base",
    "to_base"
]

_GET_NN_LEN_AT_BASE: dict[tuple[int, Base], int] = {}


def _validate_is_nn(n: int) -> None:
    if not n >= 0 and isinstance(n, int):
        raise ValueError(f"{n=} is not a natural number! ")


def _validate_base(b: Base) -> None:
    if b not in REMAINDER_TO_SYMBOL_MAP:
        raise ValueError(f"Base {b=} is not allowed! ")


def get_nn_len_at_base(n: int, b: Base = 2, cache_call: bool = False) -> int:
    if (n, b) in _GET_NN_LEN_AT_BASE:
        return _GET_NN_LEN_AT_BASE[(n, b)]
    res = floor(log(n, b)) + 1
    if cache_call:
        _GET_NN_LEN_AT_BASE[(n, b)] = res
    return res


def digit_at_base(n: int, b: Base, i: int) -> int:
    return (n // (b ** (i - 1))) % b


def symbol_at_base(n: int, b: Base, i: int) -> str:
    return REMAINDER_TO_SYMBOL_MAP[digit_at_base(n, b, i)]


def to_base(n: int, r: Base) -> str:
    _validate_is_nn(n)
    _validate_base(r)
    str_rep: list[str] = []
    base_power_counter: int = 1
    base_power_bound: int = get_nn_len_at_base(n, r)
    num: int = n
    while base_power_counter <= base_power_bound:
        remainder: int = num % r
        str_rep.append(REMAINDER_TO_SYMBOL_MAP[remainder])
        num = num // r
        base_power_counter += 1
    return "".join(str_rep[::-1])
