import numpy as np
from pydantic import BaseModel, ConfigDict, PositiveInt


class FixedInputSizeTimingResults(BaseModel):
    input_size: PositiveInt
    runs_num: PositiveInt
    times: np.ndarray

    median_time: float
    std_time: float


class TimingResults(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    input_sizes: np.ndarray
    runs_num: PositiveInt
    times: np.ndarray

    median_times: np.ndarray
    std_times: np.ndarray
