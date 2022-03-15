alunos =[('Renzo',0), ('Luciano',10), ('Ada',9)]
print([(nome , nota) for nome , nota in alunos if nota>5])
def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota>5
def extrair_nome(alunos):
    nome,_ =alunos
    return nome

print(list(filter(possui_nota_maior_que_5,alunos)))
print(list(map(extrair_nome,alunos)))
print(list(map(extrair_nome,(filter(possui_nota_maior_que_5,alunos)))))
import operator
pegar_primeiro = operator.itemgetter(0)
pegar_primeiro([1,2])
print(list(map(operator.itemgetter(0),(filter(possui_nota_maior_que_5,alunos))))) # another way , pode ser encontrado em programadores mais experientes
#"Em termos de funcionalidade as duas funções funcionam da mesma maneira, porém o filter é mais conciso no que está executando"
