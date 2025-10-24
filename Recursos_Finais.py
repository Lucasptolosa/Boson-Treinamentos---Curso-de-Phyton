# Trocar valores entre duas variáveis

var1 = 12
var2 = 31

#var2, var1 = var1, var2

#print(f'var1: {var1}, var2: {var2}')

# Operador condicional ternário
#menor = var1 if var1 < var2 else var2
#print(f'Menor valor: {menor}')

#Generator

#valores = [1,3,5,7,9,11,13,15]
#quadrados = (i ** 2 for i in valores)
#print(quadrados)
#for valor in quadrados:
#    print(valor)

# Função Enumerate()
#bebidas = ['café', 'chá', 'água', 'suco', 'refrigerante']
#for i, item in enumerate(bebidas):
#    print(f'Indice: {i}, item: {item}')

#lista = ['maça','banana','uva ']
#for i, fruta in enumerate(lista,1):
#    print(i,fruta)

temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t} graus Celcius')