from pulp import *

x12 = LpVariable("x12", 0, 5)  # 0<= x12 <= 5
x13 = LpVariable("x13", 0, 13)  # 0<= x13 <= 13
x23 = LpVariable("x23", 0, 4)  # 0<= x23 <= 4
x24 = LpVariable("x24", 0, 9)  # 0<= x24 <= 9
x34 = LpVariable("x34", 0, 10)  # 0<= x34 <= 10

# Definimos el problema (Pudiendo ser de maximizacion o minimizacion)
prob = LpProblem("Minimum-cost flow", LpMinimize)

# Definimos las restricciones
prob += x12 + x13 == 12
prob += x12 - x23 - x24 == 0
prob += x13 + x23 - x34 == 0

# Definimos la funcion objetivo
prob += 3 * x12 + 8 * x13 + 2 * x23 + 12 * x24 + 6 * x34

# Resolvemos el problema
status = prob.solve()
print(LpStatus[status])

print(x12.value())
print(x13.value())
print(x23.value())
print(x24.value())
print(x34.value())

print('Valor optimo: ', pulp.value(prob.objective))
