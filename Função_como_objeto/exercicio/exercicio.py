"""
Construa u uma função de ordenação que ordene os alunos por nota. Se houver empate, o nome deverá definir a ordem

"""

alunos =[('Renzo',0), ('Luciano',6), ('Ada',9),('Raphael Moral',10), ('Victor', 7),('Thamires', 10), ]
alunos.sort(key = lambda aluno: aluno[-1])
print(alunos)
def por_nota(aluno):

    return aluno[1]
def por_nome (aluno):
    return aluno[0]

notas =(list(reversed(sorted(alunos, key=por_nota))))
print(notas)