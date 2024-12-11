
# 1:solicitar al usuario que ingrese la edad del cliente

from operator import truediv

age = int(input("Por favor ingrese la edad del cliente: "))


# 2: Verificar si la edad ingresada cumple con el requisito para entrara al boliche
allowed = True if age >= 18 else False  # ternario
if allowed:
    print("Puedes ingresar al boliche !!")
else:
    print("Lo sentimos mucho, no puedes ingresar al boliche, vuelve siendo mayor de edad")

# 3:mostrar al usuario si su cliente puede o no ingresar al boliche
