import rasterio
import numpy as np

# open the raster file
raster = rasterio.open("/content/9SE22C(e809n812,e809n812).tif")
# read the data in the raster
data = raster.read(1)

# calculate flow direction
direction = np.empty(data.shape, dtype=np.uint8)
for i in range(1, data.shape[0]-1):
    for j in range(1, data.shape[1]-1):
        if data[i, j] == 0:
            direction[i, j] = 0
        else:
            if data[i-1, j] > data[i, j]:
                direction[i, j] = 1
            elif data[i, j-1] > data[i, j]:
                direction[i, j] = 2
            elif data[i+1, j] > data[i, j]:
                direction[i, j] = 4
            else:
                direction[i, j] = 8

# calculate accumulation
accumulation = np.zeros(data.shape)
for i in range(1, data.shape[0]-1):
    for j in range(1, data.shape[1]-1):
        if direction[i, j] & 1:
            accumulation[i, j] += accumulation[i-1, j]
        if direction[i, j] & 2:
            accumulation[i, j] += accumulation[i, j-1]
        if direction[i, j] & 4:
            accumulation[i, j] += accumulation[i+1, j]
        if direction[i, j] & 8:
            accumulation[i, j] += accumulation[i, j+1]
        accumulation[i, j] += 1
        
print(direction)
print()
print(accumulation)

import earthpy as et
import earthpy.plot as ep
ep.plot_bands(accumulation, title="Flow accumulation from the input raster", cmap="plasma")
plt.show()
