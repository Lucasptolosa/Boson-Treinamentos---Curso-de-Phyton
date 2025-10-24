from math import sqrt

class NumeroNegativoErro(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input('digite um número positivo: '))
        if num < 0:
            raise NumeroNegativoErro
    except NumeroNegativoErro:
        print(f"Foi fornecido um número negativo!")
    else:
        print(f"A raiz quadra de {num} é {sqrt(num)}")
    finally:
        print('Fim de cálculo') 