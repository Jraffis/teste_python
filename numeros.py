# Solicitar dois números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Comparar os números e identificar o maior
if numero1 > numero2:
    print(f"O maior numeração é: ", numero1)
elif numero2 > numero1:
    print(f"O maior numeracao é: {numero2}")
else:
    print("Os dois números são iguais.")
