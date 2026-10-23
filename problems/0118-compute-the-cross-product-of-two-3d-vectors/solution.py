import numpy as np

def cross_product(a, b):
    # Your code here
    # we can try to implement the determinant method to calculate the cross prodcut
    # a[0] a[1] a[2]
    # b[0] b[1] b[2]
    result = [0,0,0]
    result[0] = a[1]*b[2] - b[1]*a[2]
    result[1] = - (a[0]*b[2] - b[0]*a[2])
    result[2] = a[0]*b[1] - b[0]*a[1]
    return result