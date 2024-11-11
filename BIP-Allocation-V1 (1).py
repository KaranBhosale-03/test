from pulp import *
  
prob = LpProblem("Paul & Giovanni Foods", LpMinimize)

x11 = LpVariable('LAtoHouston', lowBound = 0, upBound = 1, cat='Integer')
x12 = LpVariable('LAtoLasVegas', lowBound = 0, upBound = 1, cat='Integer')
x13 = LpVariable('LAtoNewOrleans', lowBound = 0, upBound = 1, cat='Integer')
x14 = LpVariable('LAtoChicago', lowBound = 0, upBound = 1, cat='Integer')
x15 = LpVariable('LAtoSanFran', lowBound = 0, upBound = 1, cat='Integer')
x21 = LpVariable('DenvertoHouston', lowBound = 0, upBound = 1, cat='Integer')
x22 = LpVariable('DenvertoLasVegas', lowBound = 0, upBound = 1, cat='Integer')
x23 = LpVariable('DenvertoNewOrleans', lowBound = 0, upBound = 1, cat='Integer')
x24 = LpVariable('DenvertoChicago', lowBound = 0, upBound = 1, cat='Integer')
x25 = LpVariable('DenvertoSanFran', lowBound = 0, upBound = 1, cat='Integer')
x31 = LpVariable('PensacolatoHouston', lowBound = 0, upBound = 1, cat='Integer')
x32 = LpVariable('PensacolatoLasVegas', lowBound = 0, upBound = 1, cat='Integer')
x33 = LpVariable('PensacolatoNewOrleans', lowBound = 0, upBound = 1, cat='Integer')
x34 = LpVariable('PensacolatoChicago', lowBound = 0, upBound = 1, cat='Integer')
x35 = LpVariable('PensacolatoSanFran', lowBound = 0, upBound = 1, cat='Integer')
x41 = LpVariable('CincytoHouston', lowBound = 0, upBound = 1, cat='Integer')
x42 = LpVariable('CincytoLasVegas', lowBound = 0, upBound = 1, cat='Integer')
x43 = LpVariable('CincytoNewOrleans', lowBound = 0, upBound = 1, cat='Integer')
x44 = LpVariable('CincytoChicago', lowBound = 0, upBound = 1, cat='Integer')
x45 = LpVariable('CincytoSanFran', lowBound = 0, upBound = 1, cat='Integer')

y1 = LpVariable('Use LA Distrib. Center', lowBound = 0, upBound = 1, cat='Integer')
y2 = LpVariable('Use Denver Distrib. Center', lowBound = 0, upBound = 1, cat='Integer')
y3 = LpVariable('Use Pensacola Distrib. Center', lowBound = 0, upBound = 1, cat='Integer')
y4 = LpVariable('Use Cincy Distrib. Center', lowBound = 0, upBound = 1, cat='Integer')

bigM = 10000
# Objective function
prob += 40000 * x11 + 11000 * x12 + 75000 * x13 + 70000 * x14 + 60000 * x15 + 72000 * x21 + \
77000 * x22 + 120000 * x23 + 30000 * x24 + 75000 * x25 + 24000 * x31 + 44000 * x32 + \
45000 * x33 + 80000 * x34 + 90000 * x35 + 32000 * x41 + 55000 * x42 + 90000 * x43 + \
20000 * x44 + 105000 * x45, "Obj"

# Single Sourcing Constraints
prob += x11 + x21 + x31 + x41 == 1, "Houston constraint"
prob += x12 + x22 + x32 + x42 == 1, "Las Vegas Constraint"
prob += x13 + x23 + x33 + x43 == 1, "New Orleans constraint"
prob += x14 + x24 + x34 + x44 == 1, "Chicago constaint"
prob += x15 + x25 + x35 + x45 == 1, "San Francisco constraint"

# Distribution Center Selection Constraint:
prob += x11 + x12 + x13 + x14 + x15 <= bigM*y1
prob += x21 + x22 + x23 + x24 + x25 <= bigM*y2
prob += x31 + x32 + x33 + x34 + x35 <= bigM*y3
prob += x41 + x42 + x43 + x44 + x45 <= bigM*y4
prob += y1 + y2 + y3 + y4 == 2, "Num of Dist Center constraint"

print(prob)

prob.solve()
print(LpStatus[prob.status])

for variable in prob.variables():
  print("{} = {}".format(variable.name, variable.varValue))

print("Optimial Function Value = {}".format(value(prob.objective)))