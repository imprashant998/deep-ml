import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.
    """
    if norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Frobenius norm is defined only for 2D matrix")
        return float(np.linalg.norm(arr, ord='fro'))
        
    # Handle entrywise norms by flattening to guarantee correct element-wise math
    flat_arr = arr.ravel()
    
    if norm_type == 'l1':
        return float(np.linalg.norm(flat_arr, ord=1))
    elif norm_type == 'l2':
        return float(np.linalg.norm(flat_arr, ord=2))
    elif norm_type == 'linf':
        return float(np.linalg.norm(flat_arr, ord=np.inf))
    else:
        raise ValueError(f"Unknown norm type: {norm_type}")

        
        

