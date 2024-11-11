#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:47:03 2023

@author: alirezazadeh
"""

# import the solver
from pulp import * 

# Define the Model
prob = LpProblem("MIP Example", LpMaximize)
x1 = LpVariable("x_1", lowBound = 0)
x2 = LpVariable("x_2", lowBound = 0)
x3 = LpVariable("x_3", lowBound = 0)
y1 = LpVariable("y_1", lowBound = 0, upBound = 1, cat = "Integer")
y2 = LpVariable("y_2", cat = "Binary")
y3 = LpVariable("y_3", cat = "Binary")
y4 = LpVariable("y_4", cat = "Binary")

M = 100000000

# Obj fun
prob += 5*x1 + 7*x2 + 3*x3

#Constraint
prob += 3*x1 + 4*x2 + 2*x3 <= 30 + y4*M
prob += 4*x1 + 6*x2 + 2*x3 <= 40 + (1-y4)*M
prob += x1 <= 7 
prob += x2 <= 5
prob += x3 <= 9
prob += x1 <= y1*M
prob += x2 <= y2*M
prob += x3 <= y3*M
prob += y1 + y2 + y3 <= 2

prob.solve()

print("Status: " + LpStatus[prob.status])

# print formulation
print(prob)


# Print optimal solution

for v in prob.variables():
    print("{}^* = {}".format(v.name, v.varValue))

print("Z^* = " + str(value(prob.objective)) )