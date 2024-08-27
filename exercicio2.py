try:
    dividendo = int(input("digite o dividendo: "))
    divisor = int(input(" digite o divisor: "))
    resultado = dividendo/divisor
except ValueError:
    print ("numero invalidado")
except ZeroDivisionError:
    print("divisao por zero nao permitido")