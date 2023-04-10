valor = float(input("Digite o valor da prestação em atraso: "))
taxa = float(input("Digite a taxa de juros em %: "))
tempo = int(input("Digite o tempo em dias de atraso: "))

prestacao = valor + (valor * (taxa/100) * (tempo/30))

print("O valor da prestação em atraso é R$%.2f" % prestacao)
