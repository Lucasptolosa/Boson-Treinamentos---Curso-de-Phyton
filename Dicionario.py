#Dicionários - é uma estrutura que permite adicionar valor dentro de uma variável 

elemento = {
    'z': 3, 
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f"elemento: {elemento['nome']}") # Ela devolve o valor associado.
print(f"elemento: {elemento['densidade']}")
print(f"O dicionário possui {len(elemento)} elementos")

#Atualizar uma entrada 
elemento['grupo'] = 'Alcalinos '

#Adicionar uma entrada
elemento['período'] = 1
print(elemento)

#Exclusão de intens em dicionário
#del elemento['período']
#print(elemento)

#elemento.clear()
#print(elemento) # O dicionário AINDA existe, mas não tem mais assosiações

#del elemento # Neste caso, o dicionário é deletado, tanto que na execução ele da erro.
#print(elemento)

print(elemento.items())

for i in elemento.items(): #Dessa forma, cada item fica separado para melhorar visualização.
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f"{i}: {j}")