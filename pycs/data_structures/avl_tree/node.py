from __future__ import annotations
from typing import Optional

__all__ = ["Node"]


class Node:

    def __init__(self, key: int):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.height = 0
