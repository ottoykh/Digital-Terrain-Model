## 3x3 template for computation 
## Please change the 3X3 grid !!! 
X1 = 5 
X2 = 2
X3 = 6
X4 = 1
X5 = 0
X6 = 3
X7 = 8 
X8 = 4
X9 = 7

## distance 
d = (X1+X2+X3+X4+X5+X6+X7+X8+X9)/9

## Equations for slope in row and column directions 
we1 = (X6-X4)/(2*d)
sn1 = (X2-X8)/(2*d)
we2 = ((X9+(2*X6)+X3)-(X7+(2*X4)+X1))/(8*d)
sn2 = ((X3+(2*X2)+X1)-(X9+(2*X8)+X7))/(8*d)
we3 = ((X9+(1.41421362*X6)+X3)-(X7+(1.41421362*X4)+X1))/(4+(2*1.41421362)*d)
sn3 = ((X3+(1.41421362*X2)+X1)-(X9+(1.41421362*X8)+X7))/(4+(2*1.41421362)*d)
G   = ((X9+X6+X3)-(X7+X4+X1))/(6*d)
H   = ((X3+X2+X1)-(X9+X8+X7))/(6*d)

## Plan and Profile curvatures 
D   = ((X4+X6+X1+X3+X9+X7)-2*(X5+X2+X8))/(3*(d**2))
E   = ((X2+X8+X1+X3+X9+X7)-2*(X5+X4+X6))/(3*(d**2))
F   = (X3+X7-(X1+X9))/(4*(d**2))
PlanC= -((H**2)*D-2*G*H*F+(G**2)*E)/(((G**2)+(H**2))**1.5)
ProfC= -((G**2)*D+2*G*H*F+(H**2)*E)/(((G**2)+(H**2))*((1+(G**2)+(H**2))**1.5))
MeanC= - ((1+(H**2))*D-2*G*H*F+((1+G)**2)*E)/(((G**2)+(H**2))*((1+(G**2)+(H**2))**1.5))

print("The Slope we (1) = % f" 
       %we1)
print("The Slope we (2) = % f" 
       %we2)
print("The Slope we (3) = % f" 
       %we3)
print("The Slope sn (1) = % f" 
       %sn1)
print("The Slope sn (2) = % f" 
       %sn2)
print("The Slope sn (3) = % f" 
       %sn3)
print("The Slope of G = % f" 
       %G)
print("The Slope of H = % f" 
       %H)
print("The curvature D = % f" 
       %D)
print("The curvature E = % f" 
       %E)
print("The curvature F = % f" 
       %F)
print("The Plan curvature = % f" 
       %PlanC)  
print("The Profile curvature = % f" 
       %ProfC)  
print("The Mean curvature = % f" 
       %MeanC)
