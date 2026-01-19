import numpy as np

__all__ = ["array_for_sorting"]


def array_for_sorting() -> list[int]:
    return [x for x in np.random.randint(0, 1_000, size=500)]
