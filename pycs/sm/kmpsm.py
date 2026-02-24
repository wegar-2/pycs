from .common import validate_sm_inputs

__all__ = ["kmpsm"]


def _compute_prefix_function_value(pattern: str, i: int) -> int:
    j = i

    return j


def _compute_prefix_function(pattern: str) -> list[int]:
    prefix_function: list[int] = [0] * len(pattern)
    for i in range(len(prefix_function)):
        prefix_function[i] = _compute_prefix_function_value()
    return prefix_function


def kmpsm(text: str, pattern: str) -> list[int]:
    """
    Find matches of pattern in text using Knuth-Morris-Pratt algorithm
    :param text: text to search
    :param pattern:
    :return: list of integers
    """
    validate_sm_inputs(text, pattern)
    prefix_function = _compute_prefix_function(pattern)

    i = 0
    while i <= len(text) - 1:
        pass

    return []
