"Função é um cidadão de 1ª classe na linguagem Python"
" A função é um objeto como outro qualquer"
"Objetos em python São dinâmicos"
" Significa que é possivel criar ou remover atributos em tempo de execução"
" É possivel acessar um objeto por um resultado de uma função"
from dis import dis
def dobro(x):
    return x*2
dobro2= lambda  x: x*2

dis(dobro.__code__.co_code)
dis(dobro2.__code__.co_code)
# podemos observar que é o mesmo byte code criado
dobro.__name__
dobro2.__name__
" Aqui podemos observar que dobro2 não possui um __name__ pois toda função que usa lambda se torna uma função anônima"
