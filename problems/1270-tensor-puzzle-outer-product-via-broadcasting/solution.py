import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    a = np.asarray(a).reshape(-1, 1)
    b = np.asarray(b).reshape(1, -1)

    return a * b