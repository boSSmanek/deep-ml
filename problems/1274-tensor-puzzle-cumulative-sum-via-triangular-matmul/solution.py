import numpy as np

def cumsum(a: np.ndarray) -> np.ndarray:
    """Inclusive cumulative sum of 1-D array a without np.cumsum."""
    rows = np.arange(len(a))[:, None]
    cols = np.arange(len(a))[None, :]
    return (rows >= cols) @ a
