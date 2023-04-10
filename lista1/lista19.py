conta = input("Digite o número da conta corrente (3 dígitos): ")
conta_invertida = conta[::-1] 
soma = int(conta) + int(conta_invertida)  
mult_soma = [int(digito) * (i + 1) for i, digito in enumerate(str(soma))] 
digito_verificador = str(sum(mult_soma))[-1] 

print("Dígito verificador: ", digito_verificador)
