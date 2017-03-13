import pulp
import csv
import numpy as n

#Define variables
s = pulp.LpVariable("s", 0, None)
x0 = pulp.LpVariable("x0", 0, None)
x1 = pulp.LpVariable("x1", 0, None)
x2 = pulp.LpVariable("x2", 0, None)
x3 = pulp.LpVariable("x3", 0, None)
x4 = pulp.LpVariable("x4", 0, None)
x5 = pulp.LpVariable("x5", 0, None)

#Define problem
prob = pulp.LpProblem("bestFit", pulp.LpMinimize)

#Define instance
t = []

with open('Corvallis.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
	for row in reader:
		t.append((float(row['average']), int(int(row['day1'])%365.25)))

#Add contraints
b1 = 365.25
b2 = 365.25 * 10.7
for i in t:
	d = i[1]
	a = i[0]
	top = 2*n.pi*d  #saving space
	prob += x0+x1*d+x2*n.cos(top/b1)+x3*n.sin(top/b1)+x4*n.cos(top/b2)+x5*n.sin(top/b2)-a-s <= 0
	prob += -(x0+x1*d+x2*n.cos(top/b1)+x3*n.sin(top/b1)+x4*n.cos(top/b2)+x5*n.sin(top/b2)-a)-s <= 0


#Add objective, just minimizing s
prob += s

ans = prob.solve()
print ans
print "Status: ", pulp.LpStatus[prob.status]
print "Values: "
val = [pulp.value(x0),pulp.value(x1),pulp.value(x2),pulp.value(x3),pulp.value(x4),pulp.value(x5)]
for i in range(0,6):
	print "x",i, " = ", val[i]



