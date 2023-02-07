# Import the necessary libraries
import numpy as np
import rasterio as rio

# Open the digital terrain model (DTM) raster
with rio.open('/content/9SE22C(e809n812,e809n812).tif') as src:
    dtm_data = src.read(1)

# Compute the slope from the DTM raster
# Slope is the change in elevation over the change in horizontal distance
slope = np.gradient(dtm_data)[1]

# Compute the aspect from the DTM raster
# Aspect is the direction the slope faces
aspect = np.arctan2(np.gradient(dtm_data)[0], np.gradient(dtm_data)[1])
