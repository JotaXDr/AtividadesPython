votos_branco = 0
votos_nulo = 0
votos_kiko = 0
votos_chaves = 0
votos_chiquinha = 0

while True:
    voto = input("Digite o número do seu voto (ou 666 para encerrar a votação): ")
    
    if voto == "1":
        votos_branco += 1
    elif voto == "2":
        votos_nulo += 1
    elif voto == "3":
        votos_kiko += 1
    elif voto == "4":
        votos_chaves += 1
    elif voto == "5":
        votos_chiquinha += 1
    elif voto == "666":
        break
    else:
        print("Voto inválido. Digite novamente.")
        
print("Resultado da votação:")
print("Branco:", votos_branco)
print("Nulo:", votos_nulo)
print("Kiko:", votos_kiko)
print("Chaves:", votos_chaves)
print("Chiquinha:", votos_chiquinha)
