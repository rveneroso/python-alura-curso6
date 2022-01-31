idades = [32, 38, 54, 85, 85, 60, 10]

print(range(len(idades))) # Fica no estado lazy. Em outras palavras, não popula o range.
print(enumerate(idades)) # Fica no estado lazy. Em outras palavras, não popula o enumerate.

#
# Quando usamos list forçamos a 'população' do objeto.
#
# Exibe a lista de índices dos elementos.
print(list(range(len(idades))))
# Exibe as tuplas geradas pelo enumerate a partir da lista de idades. Cada elemento da tupla tem o índice e
# o elemento daquele índice.
print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(f'Na posição {indice} temos a idade {idade}')

# Com enumerate é possível extrair os objetos contidos no enumerate e usar somente aqueles que interessam.
usuarios = [
    ('Ivan Piro', 37, 1981),
    ('Daniela Craia', 31, 1987),
    ('Osmar Mita', 39, 1979)
]

for nome, idade, ano_nascimento in usuarios:
    print(nome)

# Caso estejamos interessados em apenas um dos atributos do objeto sendo iterado podemos omitir os demais
# atributos com underline. Porém, é preciso observar que deve ser informado um underline para cada atributo
# sendo omitido. Se o objeto possui 3 atributos, usamos um deles e informamos somente um underline, um erro
# ocorrerá.
for nome, _, _ in usuarios:
    print(nome)

# A posição em que os atributos são listados também importa. No exemplo abaixo, teoricamente eu estaria usando
# os atributos nome e ano_nascimento e omitindo o atributo idade. Porém, no objeto usuario, o segundo atributo
# é a idade e não o ano de nascimento. Dessa forma, o código abaixo irá listar efetivamente o nome e a idade
# dos usuários e não o nome e o ano de nascimento.
for nome, ano_nascimento, _ in usuarios:
    print(f'{nome} nasceu em {ano_nascimento}') # Imprimirá o nome e a idade.

