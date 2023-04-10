# pede ao usuário para informar a quantidade de CDs
n_cds = int(input("Informe a quantidade de CDs: "))

# inicializa as variáveis de contagem de CDs e de valor total investido com zero
total_cds = 0
total_valor = 0


for i in range(n_cds):
    print("CD {}:".format(i+1))
    valor_cd = float(input("Informe o valor investido: "))
    total_cds += 1
    total_valor += valor_cd


if total_cds > 0:
    media_valor = total_valor / total_cds
else:
    media_valor = 0


print("O valor total investido em {} CDs é: R$ {:.2f}".format(total_cds, total_valor))
print("O valor médio gasto em cada CD é: R$ {:.2f}".format(media_valor))
