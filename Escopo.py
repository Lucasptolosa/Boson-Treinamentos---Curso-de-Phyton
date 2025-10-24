# Escopo global e local

var_global = 'Curso completo phyton'

def escreve_texto():
    global var_global
    var_global = 'bancos de dados com sql' #Dentro da função nos alteramos o valor da var_global de modo que dentro da função ela execute o valor inserido, já na execução manual fora da função, o valor manten-se o de fora.
    var_local = 'Lucas Tolosa'
    print(f"Variável global: {var_global}")
    print(f'Váriavel local: {var_local}')

if __name__ == '__main__':
    print(f"Executar a função escreve_texto()")
    escreve_texto()

    print("Tentar acessar as variaveis diretamente")
    print(f'Váriavel global: {var_global}') # A variavel global pode ser acessada de onde eu quiser da função
    #print(f"Váriavel local: {var_local}") # Já a local não pode ser exeuctada diretamente, tendo que processada diretamente pela função.