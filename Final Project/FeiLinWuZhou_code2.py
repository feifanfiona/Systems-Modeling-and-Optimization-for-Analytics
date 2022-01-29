#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:52:12 2020

ISE 3230: Homework 5
Problem #5

Plan B, Budget minimizing solely.

@author: jinlin
"""

import numpy as np
import cvxpy as cp 
import gurobi
import pandas as pd
import sys

#import the data

#car distance matrix
c=pd.read_excel (r'/Users/jinlin/Downloads/Book2.xls', header=None)

#car time matrix
car_time=pd.read_excel(r'/Users/jinlin/Downloads/car_time_matrix.xlsx')
f=car_time.iloc[:, [1,2,3,4,5,6,7,8]]


#flight time matrix
flight_time=pd.read_excel(r'/Users/jinlin/Downloads/flight_time_matrix.xlsx')
u=flight_time.iloc[:, [1,2,3,4,5,6,7,8]]


#need Gij matrix for budget 
flight_price=pd.read_excel(r'/Users/jinlin/Downloads/flight_price_matrix.xlsx')
g=flight_price.iloc[:, [1,2,3,4,5,6,7,8]]


n,m=c.shape



#Define the Binary decision variable, Xij=1 if we travel from city i to j and 0 if not.
X = cp.Variable((8, 8), boolean=True)

#binary variable for flight time
Y = cp.Variable((8, 8), boolean=True)


t =cp.Variable((8), nonneg=True)


#transforming the data frame to matrix
c=c.values
f=f.values
u=u.values
g=g.values


#Define the objective function, summation of all distances traveled across all cities
obj_func=cp.trace(f.T @ X)+cp.trace(u.T@ Y)

constraints = []



col_sums_X = cp.sum(X, axis=0, keepdims=True)
col_sums_Y = cp.sum(Y, axis=0, keepdims=True) # axis=0 sums over rows for each column
constraints.append(col_sums_X+col_sums_Y==1)
row_sums_X = cp.sum(X, axis=1, keepdims=True)
row_sums_Y = cp.sum(Y, axis=1, keepdims=True) # axis=1 sums over columns for each row
constraints.append(row_sums_X+row_sums_Y==1)


# Budget constraint
p=0.17 # gas cost per mile
constraints.append(cp.trace(g.T @ Y)+cp.trace(c.T @ X)*p<=500)


for i in range(1,n):
    constraints.append(t[i]>=1)
    constraints.append(t[i]<=n-1)

    


for i in range(1,n):
        for j in range (1,m):
            if i==j:
                continue
            else: constraints.append(t[i]-t[j]+8*X[i,j]+8*Y[i,j]<=7)
            

problem = cp.Problem(cp.Minimize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)


print("obj_func =")
print(obj_func.value)
print("X =")
print(X.value)
print("Y =")
print(Y.value)


