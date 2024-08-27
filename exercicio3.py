
A = int(input("Digite o valor de A: "))


B = int(input("Digite o valor de B: "))


print(f"Antes da troca: A = {A}, B = {B}")


resposta = input("Você deseja trocar os valores de A e B? (sim/não): ").strip().lower()


if resposta == 'sim':
    
    A, B = B, A
    print(f"Depois da troca: A = {A}, B = {B}")
else:
    print("Os valores não foram trocados.")
