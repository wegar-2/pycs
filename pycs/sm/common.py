
__all__ = ["validate_sm_inputs"]


def validate_sm_inputs(text: str, pattern: str) -> None:
    if not isinstance(text, str):
        raise TypeError("Invalid text passed - not a string")
    if not isinstance(pattern, str):
        raise TypeError("Invalid pattern passed - not a string")
    if len(text) < len(pattern):
        raise ValueError("Inconsistent lengths of text and pattern: "
                         "text shorter than the text! ")
