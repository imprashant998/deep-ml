import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    # formula can be derived simply with chain rule
    # (g'h - gh') / h**2
    # now we need to write a small helper function for f' and/or g'
    # caution - be super-explicit with braces otherwise operator precedence could kick in and posssibly be unintended
    def value(coeffs):
        L = len(coeffs)
        return sum(coeffs[i]*(x**(L-1-i)) for i in range(L))
    def derivative(coeffs):
        # general form could be written as
        # f(x) = coeffs[0](x^L-1) + coeffs[1](x^L-2) + ... + coeffs[L-1](x^0)
        # f'(x) = (L-1)coeffs[0](x^L-2) + (L-2)coeffs[1](x^L-3) + .... + 0 ( last term const)
        L = len(coeffs)
        return sum((L-1-i)*coeffs[i]*(x**(L-2-i)) for i in range(L-1)) # since last term is constant; derivative = 0
    # plug into the formaula
    derivative_g = derivative(g_coeffs)
    derivative_h = derivative(h_coeffs)
    g = value(g_coeffs)
    h = value(h_coeffs)

    return ((derivative_g * h) - (derivative_h * g)) / (h**2)
