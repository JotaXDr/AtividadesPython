valor_multa = float(input("Digite o valor da multa mensal: "))
faturamento_mensal = float(input("Digite o valor do faturamento mensal: "))
num_fitas_mes = float(input("Digite o número de fitas alugadas por mês: "))

faturamento_anual = faturamento_mensal * 12
multas_anuais = valor_multa * 12
total_fitas = num_fitas_mes * 12

print("Faturamento anual: R${:.2f}".format(faturamento_anual))
print("Valor das multas anuais: R${:.2f}".format(multas_anuais))
print("Total de fitas ao final de 1 ano: {:.2f}".format(total_fitas))
