# Colocando os valores a, b e c (ax²+bx+c=0) convertidos em reais
import math

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

# Calculando o delta da função
delta = b * b - 4 * a * c

# Criando os desvios condicionais
if delta > 0:
    # calculo de 2 valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("x1 = ",x1)
    print("x2 = ",x2)
elif delta == 0:
    # calculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("x = ",x)
else:
    # não há valor real para x
    print("não há x real")

