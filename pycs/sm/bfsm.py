
__all__ = ["bfsm"]


def bfsm(text: str, pattern: str) -> list[int]:

    if not isinstance(text, str):
        raise TypeError("Invalid text passed - not a string")
    if not isinstance(pattern, str):
        raise TypeError(f"Invalid pattern passed - not a string")
    if len(text) < len(pattern):
        raise ValueError("Inconsistent lengths of text and pattern: "
                         "text shorter than the text! ")

    pointers: list[int] = []
    for i in range(0, len(text) - len(pattern)):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
            pointers.append(i)

    return pointers
