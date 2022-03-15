alunos =[('Renzo',0),('Alexandre',10) ,('Luciano',10), ('Ada',10)]

"Método de alta ordem"
alunos.sort(key = lambda aluno: aluno[1]) # Recebe um critério de ordenação quando escolhe [1] , retorna o segundo padrão de ordenação

print(alunos)
" Função de alta ordem"

def por_nome(aluno):
    return aluno[0]
print(sorted(alunos, key= por_nome))
# Neste caso a ordenação é por nome
" Função de alta ordem"
""