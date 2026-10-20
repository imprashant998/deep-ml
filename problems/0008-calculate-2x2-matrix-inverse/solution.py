def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    #det = (a*d - b*c)
    det = matrix[0][0] * matrix[1][1] -  matrix[0][1] * matrix[1][0]
    if not det :
        return None
    # matrix[0][0],matrix[1][1] = matrix[1][1],matrix[0][0] # swap the diagnonal element
    # matrix[0][0] /= det
    # matrix[1][1] /= det
    # matrix[0][1] = (-1/det) *  matrix[0][1]
    # matrix[1][0] = (-1/det) * matrix[1][0]
    # return matrix 
    # changing the matrix in-place broke the code. 
    # gemni says - 
#     In professional programming and standard testing suites, a function should be a pure function—meaning it takes inputs, computes a result, and returns that result without unintentionally modifying (mutating) the input parameters.

# Why the blame lies with the solution:

# 1. Unintended Side Effects: When an engineer calls a function like inverse_2x2(A), they expect to receive the inverse matrix. They do not expect their original matrix A to be completely scrambled or rewritten in memory.
# 2. Violating Pass-by-Object-Reference: Because Python passes lists by reference, modifying matrix[0][0] directly inside the function mutates the caller's data.

    return [
        [matrix[1][1]/det , -matrix[0][1]/det],
        [-matrix[1][0]/det, matrix[0][0]/det]]



