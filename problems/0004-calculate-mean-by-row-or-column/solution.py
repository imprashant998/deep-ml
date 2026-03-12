def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	matrix = np.array(matrix)
	if mode == "column":
		return np.mean(matrix,axis=0,dtype= np.float32).tolist()
	if mode == "row":
		return np.mean(matrix, axis =1, dtype = np.float32).tolist()