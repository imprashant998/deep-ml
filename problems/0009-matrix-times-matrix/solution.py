def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    result = []
    # all we need to iteratively pick the rows and cols in proper order and build the result matrix
    # to build the ith row of the result matrix, we need to target ith row of a with all cols of b 
    if len(a[0])!= len(b):
        return -1
    cols = []
    def dot(v1,v2):
        dot_product = 0
        for i in range(len(v1)):
            dot_product += v1[i]*v2[i]
        return dot_product
    for j in range(len(b[0])):
        col = []
        for i in range(len(b)):
            col.append(b[i][j])
        cols.append(col)
    for row in a:
        result_row = []
        for col in cols:
            result_row.append(dot(row,col))
        result.append(result_row)
    return result

    
        
    