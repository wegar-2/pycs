from pycs.common.constants import REMAINDER_TO_SYMBOL_MAP
from pycs.common.types import Radix


def _validate_is_nn(n: int):
    if not n >= 0 and isinstance(n, int):
        raise ValueError()


def _validate_allowed_base(base: int) -> bool:
    pass


def _validate_int_as_str():
    pass


def get_nn_len_at_base(n: int, base: int = 2) -> int:
    pass


def to_base(n: int | str, base: Radix) -> str:

    _validate_is_nn(n=n)

    str_rep: list[str] = []

    base_to_power: int = 1
    num: int = n

    while base_to_power < n:
        remainder: int = num % base
        str_rep.append(REMAINDER_TO_SYMBOL_MAP[remainder])
        num = num // base
        base_to_power *= base_to_power


    return "".join(str_rep[::-1])
