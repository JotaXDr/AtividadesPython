numero = int(input("Digite um número no formato CDU: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f"Centena={centena}")
print(f"Dezena={dezena}")
print(f"Unidade={unidade}")
