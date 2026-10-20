def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    # the formula is simple
    # c*n * (x^n-1)
    return c*n*(x**(n-1))