import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	# np is imported , so better use it
	gradient = np.array(gradient)
	magnitude = np.linalg.norm(gradient) # default is L2
	if not magnitude:
		direction = np.zeros_like(gradient)
	else:
		direction = gradient/magnitude
	descent_direction = -1* direction
	return {'magnitude':magnitude, 'direction':direction, 'descent_direction':descent_direction}
