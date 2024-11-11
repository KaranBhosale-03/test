#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:53:31 2023

@author: alirezazadeh
"""
# import the solver
from pulp import * 


# Work scheduling problem

# RHS
staffDemand = {"8-9": 0,
               "9-10": 7,
               "10-11": 8,
               "11-Noon": 7,
               "Noon-1": 6,
               "1-2": 13,
               "2-3": 12,
               "3-4": 14,
               "4-5": 9}

prob = LpProblem("Work Scheduling", LpMinimize)
x1 = LpVariable("x_1", lowBound = 0, cat = "Integer")
x2 = LpVariable("x_2", lowBound = 0, cat = "Integer")
x3 = LpVariable("x_3", lowBound = 0, cat = "Integer")
x4 = LpVariable("x_4", lowBound = 0, cat = "Integer")
x5 = LpVariable("x_5", lowBound = 0, cat = "Integer")
x6 = LpVariable("x_6", lowBound = 0, cat = "Integer")

# Obj fun
prob += x1 + x2 + x3 + x4 + x5 + x6

#Constraint
prob += x1 >= staffDemand["8-9"]
prob += x1 + x2 >= staffDemand["9-10"]
prob += x1 + x2 + x3 >= staffDemand["10-11"]
prob += x1 + x2 + x3 + x4 >= staffDemand["11-Noon"]
prob += x2 + x3 + x4 + x5 >= staffDemand["Noon-1"]
prob += x3 + x4 + x5 + x6 >= staffDemand["1-2"]
prob += x4 + x5 + x6 >= staffDemand["2-3"]
prob += x5 + x6 >= staffDemand["3-4"]
prob += x6 >= staffDemand["4-5"]


prob.solve()

print("Status: " + LpStatus[prob.status])

# print formulation
print(prob)


# Print optimal solution

for v in prob.variables():
    print("{}^* = {}".format(v.name, v.varValue))

print("Z^* = " + str(value(prob.objective)) )