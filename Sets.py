# São coleções não ordenadas de valores únicos. Os quais a gente usa pra armazenar multiplos itens dentro de um objeto.
# Eles armazenam itens não duplicados e suportam operações matemáticas sob conjuntos.
# A gente não consegue modificar os itens dentro de um set, mas é possível adicionar novos elementos

planeta_anao = {'plutao', 'ceres', 'eris', 'haumea', 'makemake'}
print(planeta_anao) # a diferença entre dicionários e sets, vem de que os dicionários devolvem os valores em pares, enquanto o set mostra os conjuntos.
print('ceres' in planeta_anao)
print('lua' in planeta_anao)

# print('lua' not in planeta_anao)

#for astro in planeta_anao:
#    print(astro.upper()) #.upper deixa tudo em letra maiuscula

#astros = ['lua', 'venus', 'sirius', 'marte', 'lua']
#print(astros, end='')
#astros_set = set(astros)
#print(astros_set) #cria um set baseado na lista. -- nos SETS não existem conjuntos duplicados, apenas na lista

astros1 = {"lua", "venus", "sirius", "marte", 'io'}
astros2 = {"lua", "venus", "sirius", "marte", 'cometa de halley'}
#print(astros1 | astros2) # | -> une os dois conjuntos
#print(astros1.union(astros2)) # Mesmo esquema do |

#print(astros1 & astros2)
#print(astros1.intersection(astros2)) # Dessa forma, tanto o & quanto o .intersection representa a expressão de apenas as informações presentes em ambos

#print(astros1 ^ astros2)
#print(astros1.symmetric_difference(astros2)) # Trazem os elementos que não aparecem em ambos os conjuntos

astros1.add('Urano')
astros1.add('sol')
astros1.remove('io') #astros1.discard também funcionaria, visto que com o remove da erro caso o elementos não exista, e o discard não
astros1.pop() #Aqui se elimina um elemento aleatório
astros1.clear() #Aqui esvazia tudo
print(astros1) #Os elementos dos conjuntos aparecem em uma ordem qualquer