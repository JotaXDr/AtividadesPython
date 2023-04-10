
n = int(input("Quantas notas serão usadas para o cálculo da média? "))

soma = 0

for i in range(n):
    nota = float(input("Informe a nota {}: ".format(i+1)))
    soma += nota

media = soma / n

print("A média aritmética das {} notas informadas é {:.2f}".format(n, media))
