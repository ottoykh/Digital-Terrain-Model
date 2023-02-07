# Import libraries 
import numpy as np 
import math
import scipy.ndimage.morphology

with rio.open('/content/9SE22C(e809n812,e809n812).tif') as src:
    dtm_data = src.read(1)

# Compute the wind flow dynamic in 16 directions
directions = np.arange(0, 360, 22.5)
for direction in directions:
    # Compute the gradients of the DTM in the x and y directions
    dy, dx = np.gradient(dtm_data)

    # Rotate the gradients by the angle of the direction vector (in radians)
    angle_radians = (direction * np.pi) / 180
    dx_rotated = np.cos(angle_radians) * dx + np.sin(angle_radians) * dy
    dy_rotated = -np.sin(angle_radians) * dx + np.cos(angle_radians) * dy

    # Calculate the direction vector of the wind flow
    direction_vector = np.arctan2(dy_rotated, dx_rotated)
    direction_vector = np.rad2deg(direction_vector)

    # Use a morphological operator to detect sharp edges
    direction_vector = scipy.ndimage.morphology.binary_dilation(direction_vector, structure=np.ones((3, 3)))

    # Calculate the magnitude of the wind flow
    magnitude = np.sqrt(np.power(dx, 2) + np.power(dy, 2))

    # Save the direction vector and magnitude to a file
    np.savetxt('direction_vector_{}.txt'.format(direction), direction_vector)
    np.savetxt('magnitude_{}.txt'.format(direction), magnitude)
