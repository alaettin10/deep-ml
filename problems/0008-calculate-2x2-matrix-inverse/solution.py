import numpy as np
def inverse_2x2(a: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    det = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
    
    # 2. Singular (tekil) matris kontrolü: det sıfırsa tersi yoktur
    if det == 0:
        return None
    
    # 3. Elemanların yerini değiştir, eksile ve det'e böl
    new_array = np.array([
        [a[1][1] / det, -a[0][1] / det],
        [-a[1][0] / det, a[0][0] / det]
    ])
    
    return new_array.tolist()
    pass