import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	# Your code here
	U = np.array(A, dtype=float)
	L = np.eye(len(A))
	n = len(A)

	for i in range(n):
		for j in range(i+1,n):
			divide = U[j,i] / U[i,i]

			L[j,i] = divide

			U[j,:] = U[j,:] - divide * U[i,:]

	
	A = L @ U
	return L,U

	pass