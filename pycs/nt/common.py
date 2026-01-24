from math import log, floor

from pycs.common.constants import REMAINDER_TO_SYMBOL_MAP
from pycs.common.types import Radix

__all__ = [
    "get_nn_len_at_base",
    "get_ith_last_digit_of_number_repr",
    "to_base"
]

_GET_NN_LEN_AT_BASE: dict[tuple[int, Radix], int] = {}


def _validate_is_nn(n: int) -> None:
    if not n >= 0 and isinstance(n, int):
        raise ValueError(f"{n=} is not a natural number! ")


def _validate_radix(r: Radix) -> None:
    if r not in REMAINDER_TO_SYMBOL_MAP:
        raise ValueError(f"Radix {r=} is not allowed! ")


def get_nn_len_at_base(
        n: int,
        radix: Radix = 2,
        cache_call: bool = False
) -> int:
    if (n, radix) in _GET_NN_LEN_AT_BASE:
        return _GET_NN_LEN_AT_BASE[(n, radix)]
    res = floor(log(n, radix)) + 1
    if cache_call:
        _GET_NN_LEN_AT_BASE[(n, radix)] = res
    return res


def get_ith_last_digit_of_number_repr(n: int, r: Radix, i: int) -> int:
    if i > (base_repr_len := get_nn_len_at_base(n, r)):
        raise ValueError(
            f"Representation of {n=:_} at base {r=} is {base_repr_len},"
            f"whereas {i}-th digit from the ends has been requested! "
        )
    return n % r**i


def to_base(n: int, r: Radix) -> str:
    _validate_is_nn(n)
    _validate_radix(r)
    str_rep: list[str] = []
    base_power_counter: int = 1
    base_power_bound: int = get_nn_len_at_base(n, r)
    num: int = n
    while base_power_counter < base_power_bound:
        remainder: int = num % r
        str_rep.append(REMAINDER_TO_SYMBOL_MAP[remainder])
        num = num // r
        base_power_counter += 1
    return "".join(str_rep[::-1])
