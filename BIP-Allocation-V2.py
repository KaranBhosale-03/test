#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:36:14 2023

@author: alirezazadeh
"""


from pulp import * 

dc_list = ["LA", "Den", "Pns", "Cnc"]
city_list = ["Hou", "LV", "NO", "Chi", "SF"]

cost = [
        [40, 11, 75, 70, 60],
        [72, 77, 120, 30, 75],
        [24, 44, 45, 80, 90],
        [32, 55, 90, 20, 105]
        ]

# Define Decision Vriables
prob = LpProblem("Paul & Giovanni Foods", LpMinimize)

num_dcs = len(cost)
num_cities = len(cost[0])
decision_vars = []
for i in dc_list:
    dc_vars = []
    for j in city_list:
        var_name = f"X_{i}_{j}"
        dc_vars.append(LpVariable(var_name, lowBound=0, upBound=1, cat='Integer'))
    decision_vars.append(dc_vars)

# Auxiliary variables to decide about the selection of DC locations
aux_vars = []
for i in dc_list:
    aux_vars.append(LpVariable(f"y_{i}", lowBound=0, upBound=1, cat='Integer'))

bigM = 10000

# Objective function
prob += lpSum([
    decision_vars[i][j] * cost[i][j]
    for i in range(num_dcs)
    for j in range(num_cities)
])

# add the constraints
# each city can only be supplied by a single distribution center
for j in range(num_cities):
    prob += lpSum([decision_vars[i][j] for i in range(num_dcs)]) == 1

# each distribution center can only supply a single city
for i in range(num_dcs):
    prob += lpSum(decision_vars[i]) <= bigM*aux_vars[i]
    
prob += lpSum([
    aux_vars[i]
    for i in range(num_dcs)
]) == 2


# only two distribution centers can be assigned
# prob += lpSum([lpSum(decision_vars[i]) for i in range(num_dcs)]) == 2

prob.solve()

print("Status: " + LpStatus[prob.status])

# print formulation
print(prob)

for variable in prob.variables():
  print("{} = {}".format(variable.name, variable.varValue))

print("Optimial Function Value = {}".format(value(prob.objective)))



