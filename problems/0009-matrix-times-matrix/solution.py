def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    result = []
    # all we need to iteratively pick the rows and cols in proper order and build the result matrix
    # to build the ith row of the result matrix, we need to target ith row of a with all cols of b 
    if len(a[0])!= len(b):
        return -1
    # we need to adopt pythonic code
    def dot(u,v):
        return sum(x*y for x,y in zip(u,v))
    b_transpose = [list(col) for col in zip(*b)]
    return [[dot(row,col) for col in b_transpose] for row in a]

        

    
        
    