from pulp import *

x12 = LpVariable("x12", 0, 14)  # 0<= x12 <= 14
x13 = LpVariable("x13", 0, 15)  # 0<= x13 <= 15
x23 = LpVariable("x23", 0, 4)  # 0<= x23 <= 4
x24 = LpVariable("x24", 0, 10)  # 0<= x24 <= 10
x34 = LpVariable("x34", 0, 18)  # 0<= x34 <= 18

# Definimos el problema (Pudiendo ser de maximizacion o minimizacion)
prob = LpProblem("Max flow", LpMaximize)

# Definimos las restricciones

prob += x12 - x23 - x24 == 0
prob += x13 + x23 - x34 == 0

# Definimos la funcion objetivo
prob += x12 + x13

# Resolvemos el problema
status = prob.solve(pulp.GLPK())
print(LpStatus[status])

print(x12.value())
print(x13.value())
print(x23.value())
print(x24.value())
print(x34.value())


print('Valor optimo: ', pulp.value(prob.objective))

