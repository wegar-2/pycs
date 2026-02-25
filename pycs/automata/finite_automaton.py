from typing import Final

__all__ = ["FiniteAutomaton"]

import pandas as pd


class FiniteAutomaton:

    def __init__(
            self,
            states: set[str],
            transition_func: pd.DataFrame,
            input_alphabet: set[str],
            accepting_states: set[str]
    ):
        self._states: Final[set[str]] = states
        self._accepting_states: Final[set[str]] = accepting_states
        self._input_alphabet: Final[set[str]] = input_alphabet

        self._validate_transition_func(transition_func)
        self._transition_func: Final[pd.DataFrame] = transition_func

    def _validate_accepting_states(self, states: set[str]) -> None:
        if self._states.intersection(states) != states:
            raise ValueError()

    def _validate_transition_func(
            self,
            transition_func: pd.DataFrame
    ) -> None:
        pass

    @property
    def states(self) -> set[str]:
        return self._states

    @property
    def accepting_states(self) -> set[str]:
        return self._accepting_states

    @property
    def input_alphabet(self) -> set[str]:
        return self._input_alphabet

    def parse(self, inp: list[str]) -> str:
        pass
