import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    rows = np.arange(n)[:, None]
    cols = np.arange(n)[None, :]
    return (rows == cols).astype(np.float64)
