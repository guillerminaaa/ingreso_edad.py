# 1: solicitar al usuario que ingrese el radio del circulo de tipo flotante
import math


radius_of_the_circle = float(input("Por favor ingrese el rqadio del circulo"))

# 2: calcular el area del circulo usando la formula area = π * radio^2
area = math.pi * (radius_of_the_circle**2)

# 3: Mostrar al usuario el area calculada
print("El area del circulo con radio", radius_of_the_circle , "es:", area)
