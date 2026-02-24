from typing import Final

__all__ = ["FiniteAutomaton"]


class FiniteAutomaton:

    def __init__(self, states: set[str]):
        self._states: Final[set[str]] = states

    @property
    def states(self) -> set[str]:
        return self._states

    def parse(self, inp: str) -> str:
        pass
