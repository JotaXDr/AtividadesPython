
n = int(input("Informe o número total de eleitores: "))


votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(n):
    print("Eleitor {}:".format(i+1))
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do candidato escolhido: "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido, tente novamente")
        continue


print("Resultado da eleição:")
print("Candidato 1 - {} votos".format(votos_candidato1))
print("Candidato 2 - {} votos".format(votos_candidato2))
print("Candidato 3 - {} votos".format(votos_candidato3))
