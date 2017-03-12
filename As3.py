from pulp import *

#Some example code I found online, however pulp doesn't seem to be on FLIP?

# declare your variables
x1 = LpVariable("x1", 0, 40)   # 0<= x1 <= 40
x2 = LpVariable("x2", 0, 1000) # 0<= x2 <= 1000
 
# defines the problem
prob = LpProblem("problem", LpMaximize)
 
# defines the constraints
prob += 2*x1+x2 <= 100 
prob += x1+x2 <= 80
prob += x1<=40
prob += x1>=0
prob += x2>=0
 
# defines the objective function to maximize
prob += 3*x1+2*x2
 
# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]
 
# print the results x1 = 20, x2 = 60
value(x1)
value(x2)