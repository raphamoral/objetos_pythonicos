from functools import wraps
from time import strftime, sleep

def logar(fmt ='%H:%M:%$'):
    def decorator(f):
        @wraps(f) # utilizado para retornar o nome original da função executada
        def executar_com_tempo(*arg,**kwargs):

            print(strftime(fmt))
            return f(*arg,**kwargs)
        return executar_com_tempo
    return decorator

@logar(fmt='%H:%M:$S')
def mochileiro():
    return 42
@logar(fmt='/%d/%m/%Y %H:%M:$S')
def ola(nome):
    strftime('%H:%M:$S')

    return f"Olá {nome}"

if __name__ == '__main__':
    print((mochileiro()))
    print(mochileiro.__name__)
    print(ola('Raphael'))
    sleep(1)
    print()