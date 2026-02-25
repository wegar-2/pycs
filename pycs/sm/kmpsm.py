from .common import validate_sm_inputs

__all__ = [
    "compute_prefix_function_value",
    "compute_prefix_function",
    "kmpsm"
]


def compute_prefix_function_value(pattern: str, i: int) -> int:
    if i == 0:
        return 0
    value = 0
    for j in range(1, i + 1):
        if pattern[:j] == pattern[i+1-j:i+1]:
            value = j
    return value


def compute_prefix_function(pattern: str) -> list[int]:
    prefix_function: list[int] = [0] * len(pattern)
    for i in range(len(prefix_function)):
        prefix_function[i] = compute_prefix_function_value(pattern, i)
    return prefix_function


def kmpsm(text: str, pattern: str) -> list[int]:
    """
    Find matches of pattern in text using Knuth-Morris-Pratt algorithm
    :param text: text to search
    :param pattern: string pattern to search for
    :return: list of integers indicating locations of pattern inside text,
    empty if no occurrences found
    """
    validate_sm_inputs(text, pattern)
    # prefix_function = _compute_prefix_function(pattern)

    i = 0
    while i <= len(text) - 1:
        pass

    return []
