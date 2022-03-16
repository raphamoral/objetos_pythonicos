from decorator.registrador import get_marcadas, marcar


def primeiro():
    pass
primeiro =marcar(primeiro)

@marcar
def segundo():
    pass
#@marcar do segundo executa a mesma coisa que primeiro=marcar(primeiro)

if __name__ == '__main__':
    for f in get_marcadas():
        print(f.__name__)
