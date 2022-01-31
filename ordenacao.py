idades = [32, 38, 54, 85, 85, 60, 10]

# sorted ordena o iterável em ordem crescente. Para isso é utilizado o __eq__ do objeto contido no iterável.
print(sorted(idades))

# reversed gera um novo iterável no qual os elementos são apresentados na ordem inversa. NÃO SE TRATA DE UMA
# ORDENAÇÃO EM ORDEM DECRESCENTE. É apenas a inversão da posição dos elementos no iterável.
print(list(reversed(idades))) # Imprime [10, 60, 85, 85, 54, 38, 32]

# Para ordenar o iterável em ordem decrescente pode-se usar o próprio sorted com a flag reverse=True
print(sorted(idades, reverse=True))

# As operações acima não alteraram a lista idades. Se for necessário a própria lista pode-se usar o método
# sort dos objetos list.
idades.sort()
print(idades)

# Alterando idades para ordenar em ordem decrescente.
idades.sort(reverse=True)
print(idades)