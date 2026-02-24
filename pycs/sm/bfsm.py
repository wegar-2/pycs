from .common import validate_sm_inputs

__all__ = ["bfsm"]


def bfsm(text: str, pattern: str) -> list[int]:
    """
    Brute-force string matching
    :param text:
    :param pattern:
    :return:
    """
    validate_sm_inputs(text, pattern)
    pointers: list[int] = []
    for i in range(0, len(text) - len(pattern)):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
            pointers.append(i)
    return pointers
