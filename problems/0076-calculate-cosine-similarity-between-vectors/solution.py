import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	import numpy as np
	v1_dot_v2 = np.dot(v1,v2)
	v1_norm = np.linalg.norm(v1)
	v2_norm = np.linalg.norm(v2)
	cos_sim = v1_dot_v2/(v1_norm * v2_norm)
	return cos_sim