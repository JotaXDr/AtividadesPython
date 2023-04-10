soma_alunos_terceira = 0
maior_quantidade_livros = 0
total_alunos = 0
alunos_nao_gostam_redacao_terceira = 0

while True:
    serie = int(input("Digite a série do aluno (1 a 4) ou 0 para sair: "))
    
    if serie == 0:
        break
    
    livros = int(input("Digite a quantidade de livros lidos por mês: "))
    redacao = int(input("Gosta de fazer redação? Digite 1 para sim ou 0 para não: "))
    
    if serie == 3:
        soma_alunos_terceira += 1
        if redacao == 0:
            alunos_nao_gostam_redacao_terceira += 1
        
    if serie == 4 and livros > maior_quantidade_livros:
        maior_quantidade_livros = livros
        
    total_alunos += 1

percentual_nao_gostam_redacao_terceira = (alunos_nao_gostam_redacao_terceira / soma_alunos_terceira) * 100 if soma_alunos_terceira != 0 else 0

print("a) Quantidade de alunos na terceira série: ", soma_alunos_terceira)
print("b) Maior quantidade de livros lidos por um aluno na quarta série: ", maior_quantidade_livros)
print("c) Porcentagem de alunos que não gostam de fazer redação e estão na terceira série: ", percentual_nao_gostam_redacao_terceira, "%")
