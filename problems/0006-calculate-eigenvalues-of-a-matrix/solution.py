def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	matrix = np.array(matrix)
	eig_values, eig_vectors = np.linalg.eig(matrix)
	return eig_values.tolist()