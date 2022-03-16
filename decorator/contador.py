def fabrica_decontador():
    contador=0
    def contar():
        nonlocal contador # Ao utilizar nonlocal, o valor será modificado para cada função indepedente
        #global contador quando se usa global, o valor de contador se aplica tanto para contador1 quanto para2
        contador+=1 # por ser estático ele não identifica o contador
        return contador
    return contar
contador1 = fabrica_decontador()
contador2 = fabrica_decontador()
print(contador1())
print(contador1())
print(contador1())
print(contador2())