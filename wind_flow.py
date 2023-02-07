# Import Libraries
import numpy as np
import rasterio

# Read Digital Terrain Model Raster Data
with rasterio.open('/content/9SE22C(e809n812,e809n812).tif') as src:
    dtm = src.read()

# Create Wind Flow Dynamic Computation
# Create a array of the elevations
elevations = dtm[0,:,:]

# Calculate the x and y gradients
dx, dy = np.gradient(elevations)

# Calculate the wind flow direction
wind_flow = np.arctan2(dy, dx)

# Output the result
print(wind_flow)
