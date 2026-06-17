import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v_arr = np.asarray(v, dtype=float)
    
    if v_arr.ndim == 1:
        return float(np.sqrt(np.sum(v_arr**2)))
    
    elif v_arr.ndim == 2:
        return np.sqrt(np.sum(v_arr**2, axis=1))
    
    else:
        raise ValueError("Input must be a single vector (1D) or a batch of vectors (2D).")