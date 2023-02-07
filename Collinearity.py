# Collinearity equation
import math as m 
import numpy as np

# Rotation matrix parameters 
w = 82.8536955
o = 71.37945995
k = 31.30165175

# Exterior Orientation parameters
X0 = 17.54629705
Y0 = 80.9923985
Z0 = 82.99158017

# Object space coordinate 
XA = 85.43834073
YA = 50.82044744
ZA = 41.52743782

# Rotation matrix according to X axis 
Mx = np.array([[1,0,0],
      [0,m.cos(w),m.sin(w)],
      [0,-m.sin(w),m.cos(w)]])
      
My = np.array([[m.cos(o),0,-m.sin(o)],
      [0,1,0],
      [m.sin(o),0,m.cos(o)]])
      
Mz = np.array([[m.cos(k),m.sin(k),0], 
      [-m.sin(k),m.cos(k),0],
      [0,0,1]])
      
print("The rotation matrix according to the X,Y,Z axis are :\n",Mx,"\n")
print(My,"\n")
print(Mz,"\n")

# Multiplication of the rotation matrix 
M_init = My.dot(Mz)
M = Mx.dot(M_init)
print("The Multiplication of the rotation matrix:\n",M,"\n")

# Extract the matrix elements 
m11= M[0][0]
m12= M[0][1]
m13= M[0][2]
m21= M[1][0]
m22= M[1][1]
m23= M[1][2]
m31= M[2][0]
m32= M[2][1]
m33= M[2][2]

c=-1

# form the Collinearity equations 

xa=-c*((m11*(XA-X0))+(m12*(YA-Y0))+(m13*(ZA-Z0))/((m31*(XA-Z0))+(m32*(YA-Y0))+(m33*(ZA-Z0))))

ya=-c*((m21*(XA-X0))+(m22*(YA-Y0))+(m23*(ZA-Z0))/((m31*(XA-Z0))+(m32*(YA-Y0))+(m33*(ZA-Z0))))

print("The xa is:",xa,"\nThe ya is :",ya)
