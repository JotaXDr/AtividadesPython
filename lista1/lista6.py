salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts gasta pela residência: "))

valor_quilowatt = salario_minimo / 700
valor_pago = quilowatts * valor_quilowatt
valor_pago_desconto = valor_pago * 0.9

print(f"Valor do quilowatt: R${valor_quilowatt:.2f}")
print(f"Valor a ser pago: R${valor_pago:.2f}")
print(f"Valor a ser pago com desconto: R${valor_pago_desconto:.2f}")
