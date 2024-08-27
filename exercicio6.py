
m = float(input("Digite o valor de m: "))


n = float(input("Digite o valor de n: "))


produto = m * n

if produto > 0:
    print(f"O produto de {m} e {n} é positivo.")
elif produto < 0:
    print(f"O produto de {m} e {n} é negativo.")
else:
    print(f"O produto de {m} e {n} é zero.")