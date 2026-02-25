from .common import validate_sm_inputs

__all__ = ["bfsm"]


def bfsm(text: str, pattern: str) -> list[int]:
    """
    Brute-force string matching algorithm.
    Checking for match for all possible shifts.
    Complexity: O(m*n) with n - length of text, m - length of pattern
    :param text: text to search
    :param pattern: string pattern to search for
    :return: list of integers indicating locations of pattern inside text,
    empty if no occurrences found
    """
    validate_sm_inputs(text, pattern)
    pointers: list[int] = []
    for shift in range(0, len(text) - len(pattern)):
        q = 0
        for j in range(len(pattern)):
            if text[shift + j] == pattern[j]:
                q += 1
            else:
                break
        if q == len(pattern):
            pointers.append(shift)
    return pointers
