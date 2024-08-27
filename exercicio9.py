
quantidade_fotocopias = int(input("Digite a quantidade de fotocópias realizadas: "))


fatura = 0.0

if quantidade_fotocopias <= 10:
    fatura = quantidade_fotocopias * 0.25
elif quantidade_fotocopias <= 30:
    fatura = 10 * 0.25 + (quantidade_fotocopias - 10) * 0.20
else:
    fatura = 10 * 0.25 + 20 * 0.20 + (quantidade_fotocopias - 30) * 0.10


print(f"O valor total a ser pago é R$ {fatura:.2f}.")
