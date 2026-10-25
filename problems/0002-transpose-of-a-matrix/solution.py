def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    transpoz = []
    for col  in range(len(a[0])):
        yeni_satir = []
        for row  in range(len(a)):
            yeni_satir.append(a[row][col])
        transpoz.append(yeni_satir)
            
    return transpoz

     
    pass