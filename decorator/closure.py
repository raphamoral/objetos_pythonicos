def fabrica_de_multiplicadores(multiplicador):
    def multiplicar (n): # EScopo de variavel de outras funções
        return n*multiplicador
    return multiplicar # retorna o resultado da função dobro  como resultado de outra função
#dobro_externo = fabrica_de_multiplicadores()
#dobro_externo_2 = fabrica_de_multiplicadores()
#print(dobro_externo is dobro_externo_2)
#print(dobro_externo(3))

print(" Tudo que fazemos com objetos em  tipos inteiros ,string  e entre outros , pode ser feito em objetos tipo função")
"""
Closure 
"""
dobro =  fabrica_de_multiplicadores(2)
triplo =fabrica_de_multiplicadores(3)
print(dobro(2))
print(triplo(3))
# Escopo estático é aquele quando você não manipula o valor da variavel do escopo exterior