# Import packages
import os
import rasterio 
import geopandas
import numpy as np

# Open Digital Terrain Model
hkdtm = rasterio.open('/content/9SE22C(e809n812,e809n812).tif')
# Please be aware that the path, I have tried different computer performance, only the mac can process teh path with () open and close bracket

# Extract the region
hkdtm = hkdtm.read(1, masked=True, window=rasterio.windows.Window(col_off=18, row_off=18,width=18, height=18)) 
# Change the col and row according to the your selected table column and rows
# The width and height here means "each pixel" width and heigh 

# Transform the extracted raster as an array
arr = np.array(hkdtm).astype('float')
# since this extract will not be an interger, so assign the array as float

# print(arr)
# print(np.array2string(arr).replace('[[',' [').replace(']]',']'))

# Print the table according to the extraction 
from pprint import pprint
import pandas as pd
# Data frame, here we set it blank "", but you can change it accoring to your own style 
table = pd.DataFrame(arr, columns = ['','','','','','','','','','','','','','','','','',''], index = ['','','','','','','','','','','','','','','','','',''])

print(table)

import numpy as np
from scipy.stats import pearsonr

# Iterate through d values from 0 to 8
for d in range(9):
    # Calculate Cov(d) Covariance 
    cov_d = np.mean([arr[i,i+d] * arr[j,j+d] for i in range(arr.shape[1] - d) for j in range(arr.shape[0] - d)])
    # Calculate V(d) Variance 
    v_d = np.mean([(arr[i,i+d])**2 for i in range(arr.shape[1] - d) for j in range(arr.shape[0] - d)])
    # Calculate R(d) 
    r_d = pearsonr(arr[0,d:], arr[1,d:])[0]
    print("For d = {}, Cov(d) = {}, V(d) = {}, R(d) = {}".format(d, cov_d, v_d, r_d))
    
for d in range(9):
    # Calculate R(d) 
    r_d = pearsonr(arr[0,d:], arr[1,d:])[0]
    print(r_d, end =',')
    # Copy the r_d (below):
    
import matplotlib.pyplot as plt

d = [0,1,2,3,4,5,6,7,8]
# Paste the r_d here 
r_d = [0.9968185628180135,0.9965139762282172,0.9959336029231166,0.9957720986695421,0.9951339494381652,0.9938982513023887,0.9919467848477075,0.9888550820225882,0.9837213613945754]
plt.plot(d, r_d, 'ro-')
plt.xlabel('d')
plt.ylabel('R(d)')
plt.title('The Plot of R(d) Against d')
plt.show()
