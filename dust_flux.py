# Importing libraries
import numpy as np
import pandas as pd
import rasterio as rio

# Loading raster
src = rio.open("/content/9SE22C(e809n812,e809n812).tif")

# Estimating dust flux
cellsize = src.res[0]
arr = src.read(1, masked = True)

# Calculating elevation difference
elev_diff = []
for y in range(src.height):
    for x in range(src.width):
        if x != src.width-1 and y != src.height-1:
            elev_diff.append(abs(arr[y,x] - arr[y,x+1]))
            elev_diff.append(abs(arr[y,x] - arr[y+1,x]))

# Computing dust flux
flux = np.array(elev_diff) * cellsize

# Outputting dust flux results
print("Dust flux:", flux)
