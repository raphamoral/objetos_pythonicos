a= 5
def f(a=3):
    b = 3 # A variavel só fica disponivel dentro desta função
    print(globals()) #Imprime variaveis globais a=5 , não imprimirá b
    print(locals()) # Imprime variveis locais dentro do escopo local a=3 , imprimirá b
    print(a) #a=3
    print(b)
    "Escopo local da função"
class A: # Também define um escopo especifico da classe
    a = 8
    print(a)
    print(globals())
    print(locals())
#f() "imprime o contexto local do global"