
nota = float(input("Digite a nota (entre 0 e 20): "))


if 0 <= nota <= 20:

    if nota > 10:
        print("Nota validada.")
    else:
        print("Nota não validada.")
else:
    print("Nota inválida. A nota deve estar entre 0 e 20.")