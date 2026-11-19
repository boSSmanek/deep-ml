import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    return a @ (np.arange(len(a)) * 0.0 + 1.0)
