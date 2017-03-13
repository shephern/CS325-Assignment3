import pulp

#Define variables
s = pulp.LpVariable("s", 0, None)
a = pulp.LpVariable("a", 0, None)
b = pulp.LpVariable("b", 0, None)

#Define problem
prob = pulp.LpProblem("bestFit", pulp.LpMinimization)

#Define instance
t = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]


