from pulp import *

# Instantiate our problem class
prob = LpProblem("Cost minimizing blending problem", pulp.LpMinimize)

# Construct our decision variable lists
sausage_types = ['eco', 'prem']
ingredients = ['pork', 'wheat', 'starch']

ing_weight = LpVariable.dicts("weight-kg",
                                     ((i, j) for i in sausage_types for j in 
                                      ingredients), lowBound=0)
                                     
# Objective Function
prob += (pulp.lpSum([
        4.32 * ing_weight[(i, 'pork')]
        + 2.46 * ing_weight[(i, 'wheat')]
        + 1.86 * ing_weight[(i, 'starch')]
        for i in sausage_types]))

# Constraints
# 350 economy and 500 premium sausages at 0.05 kg
prob += lpSum([ing_weight['eco', j] for j in ingredients]) == 350 * 0.05
prob += lpSum([ing_weight['prem', j] for j in ingredients]) == 500 * 0.05

# Economy has >= 40% pork, premium >= 60% pork
prob += ing_weight['eco', 'pork'] >= (
    0.4 * lpSum([ing_weight['eco', j] for j in ingredients]))

prob += ing_weight['prem', 'pork'] >= (
    0.6 * lpSum([ing_weight['prem', j] for j in ingredients]))

# Sausages must be <= 25% starch
prob += ing_weight['eco', 'starch'] <= (
    0.25 * lpSum([ing_weight['eco', j] for j in ingredients]))

prob += ing_weight['prem', 'starch'] <= (
    0.25 * lpSum([ing_weight['prem', j] for j in ingredients]))

# We have at most 30 kg of pork, 20 kg of wheat and 17 kg of starch available
prob += lpSum([ing_weight[i, 'pork'] for i in sausage_types]) <= 30
prob += lpSum([ing_weight[i, 'wheat'] for i in sausage_types]) <= 20
prob += lpSum([ing_weight[i, 'starch'] for i in sausage_types]) <= 17

print(prob)

# Solve our problem
prob.solve()

print(LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))
    
print("Z* = ", value(prob.objective))