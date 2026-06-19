### Função Troca Valores
###
def troca_valor():
    global a, b
    aux = a
    a = b
    b = aux
###
### Programa principal
###
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
troca_valor()
print("Novo valor de a: ", a)
print("Novo valor de b: ", b)