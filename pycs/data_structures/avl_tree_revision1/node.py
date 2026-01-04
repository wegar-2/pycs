from __future__ import annotations
from typing import Optional


class Node:

    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.height: int = 0
