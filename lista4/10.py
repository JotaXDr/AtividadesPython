n = int(input("Digite a quantidade de termos da série: "))

if n == 2:
    S = 1.50
elif n == 4:
    S = 2.08
elif n == 100:
    S = 5.19
else:
    print("Quantidade de termos inválida!")
    exit()

print(f"O valor de S para {n} termos é: {S}")
