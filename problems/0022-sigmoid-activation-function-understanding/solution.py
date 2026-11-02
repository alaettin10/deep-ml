import math

def sigmoid(z: float) -> float:
	#Your code here
	sum = 1 + math.exp(-z)
	return 1 / sum
	return result