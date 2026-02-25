from typing import Any, Final, Literal
from pathlib import Path

DATA_FOLDER_PATH: Final[Path] = Path(__file__).parent.parent / "data"

__all__ = ["load_data"]


def load_data(data_file: Literal["peloponnesian_war"]) -> Any:
    if data_file == "peloponnesian_war":
        with open(DATA_FOLDER_PATH / "peloponnesian_war.txt", mode="rt") as f:
            return "".join(f.readlines())
    else:
        raise ValueError(f"Trying to load unknown {data_file=}")
