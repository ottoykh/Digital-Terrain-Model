# NCC Normalized Cross Correlation coefficient 

import numpy as np

A = np.array ([   
     [38,51,53,50,64],
     [43,49,50,48,57],
     [39,52,80,71,68],
     [30,55,69,72,67],
     [21,49,56,61,60]])

B = np.array ([   
     [41,62,68,39,60],
     [31,52,38,41,44],
     [40,67,72,79,74],
     [31,42,77,87,70],
     [26,61,42,51,62]])

m = 25
n = 25
 
A_bar = np.sum(A)/(m*n)
B_bar = np.sum(B)/(m*n)

print("Normalised Cross Correlation coefficient (NCC)")
print("A-A_bar",(np.sum([A])-A_bar))
print("B-B_bar",(np.sum([B])-B_bar))
print("nominator   =",(np.sum([A])-A_bar)*(np.sum([B])-B_bar))
print("denominator =",((((np.sum([A])-A_bar)**2)*((np.sum([B])-B_bar)**2))**0.5))
print("\nNormalized cross Correlation coefficient\nA bar =",A_bar)
print("B bar =",B_bar)

NCC= ((np.sum([A])-A_bar)*(np.sum([B])-B_bar))/((((np.sum([A])-A_bar)**2)*((np.sum([B])-B_bar)**2))**0.5)

print("NCC  = ",NCC)
