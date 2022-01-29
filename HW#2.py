# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import cvxpy as cp

#Question 1

X = cp.Variable(3, nonneg  = True)

obj_func=600*X[0]+460*X[1]+320*X[2]

constraints = []
constraints.append(18*X[0] + 29*X[1] + 38*X[2] >= 30*(X[0] + X[1] + X[2]))
constraints.append(X[0] <= 600000)   
constraints.append(X[1] <= 800000)    
constraints.append(X[2] <= 700000)  
                   
                   
problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("X =")
print(X.value)


#Question 3

x = cp.Variable(6, nonneg = True)
y = cp.Variable(4, nonneg = True)
w = cp.Variable(2, nonneg = True)

obj_func = 1.051*x[5] + 1.162*y[3] + 1.285*w[1]

constraints = []
constraints.append(x[0] + y[0] + w[0] == 10000)
constraints.append(1.051*x[0] == x[1] + y[1] + w[1])
constraints.append(1.051 * x[1] == x[2] +y[2])
constraints.append(1.051 * x[2] +1.162 * y[0] == x[3] +y[3])
constraints.append(1.051 * x[3] +1.162 * y[1] == x[4])
constraints.append(1.051 * x[4] +1.285 * w[0] +1.162 * y[2] == x[5])

problem = cp.Problem(cp.Maximize(obj_func), constraints)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("X =")
print(x.value)
print("Y =")
print(y.value)
print("W =")
print(w.value)
                      
    
# =============================================================================
# x = cp.Variable((3, 6), nonneg  = True)
# 
# obj_func = 1.051 * x[0,5] + 1.162 * x[1,3] + 1.285 * x[2,1]
# m,n = x.shape
# 
# constraints = []
# constraints.append(x[0,0] + x[1,0] + x[2,0] == 10000)
# constraints.append(1.051 * x[0,0] == x[0,1] +x[1,1] + x[2,1])
# constraints.append(1.051 * x[0,1] == x[0,2] +x[1,2])
# constraints.append(1.051 * x[0,2] + 1.162 * x[1,0] == x[0,3] + x[2,3])
# constraints.append(1.051 * x[0,3] + 1.162 * x[1,1] == x[0,4])
# constraints.append(1.051 * x[0,4] + 1.285 * x[2,0] +1.162 * x[1,2] == x[0,5])
# 
# problem = cp.Problem(cp.Maximize(obj_func), constraints)
# problem.solve(solver=cp.GUROBI,verbose = True)
# 
# print("obj_func =")
# print(obj_func.value)
# print("X =")
# print(x.value)
# =============================================================================

#Question 5

W = cp.Variable(3, nonneg = True)
G = cp.Variable(4, nonneg  = True)

obj_func = 1.35*W[0] + 1.28*W[1] + 1.47*W[2] + 1.14*G[0] + 1.19*G[1] + 1.26*G[2] + 1.16*G[3]

constraints = []
constraints.append(W[0] + W[1] + W[2] >= 320)
constraints.append(G[0] + G[1] + G[2] + G[3] >= 250)
constraints.append(0.25*W[0] + 0.25*W[2] + 0.26*G[1] +0.2*G[2] <= 80)
constraints.append(0.13*W[0] +0.34*W[1] +0.18*G[0] +0.12*G[3] <= 80 )
constraints.append(0.15*W[1] + 0.42*W[2] +0.22*G[1] + 0.18*G[3] <= 80)
constraints.append(0.2*W[0] + 0.3*G[2] + 0.2*G[3] <= 80)
constraints.append(0.28*W[1] +0.32*G[0] + 0.14*G[1] <=80)

problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("W =")
print(W.value)
print("G =")
print(G.value)
