from typing import Any

__all__ = ["InvalidContainsException"]


class InvalidContainsException(Exception):

    def __init__(self, item: Any):
        self.message = (f"Received invalid item in the magic contains method "
                        f"of a Graph class: {type(item)=}")
