from pulp import *

x12 = LpVariable("x12", 0, 1)  # 0<= x12 <= 1
x13 = LpVariable("x13", 0, 1)  # 0<= x13 <= 1
x23 = LpVariable("x23", 0, 1)  # 0<= x23 <= 1
x24 = LpVariable("x24", 0, 1)  # 0<= x24 <= 1
x34 = LpVariable("x34", 0, 1)  # 0<= x34 <= 1

# Definimos el problema (Pudiendo ser de maximizacion o minimizacion)
prob = LpProblem("Shortest path", LpMinimize)

# Definimos las restricciones
prob += x12 + x13 == 1
prob += x12 - x23 - x24 == 0
prob += x13 + x23 - x34 == 0

# Definimos la funcion objetivo
prob += 5 * x12 + 8 * x13 + 2 * x23 + 7 * x24 + 4 * x34

# Resolvemos el problema
status = prob.solve()
print(LpStatus[status])

print(x12.value())
print(x13.value())
print(x23.value())
print(x24.value())
print(x34.value())

print('Valor optimo: ', pulp.value(prob.objective))

