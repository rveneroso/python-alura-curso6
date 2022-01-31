from contasalario import ContaSalario
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

# A função sorted permite que se especifique qual atributo será utilizado como critério de comparação
# na ordenação de objetos que não possuem uma ordem natural. Tomando como exemplo objetos do tipo
# ContaSalario, podemos proceder como mostrado abaixo. No exemplo em questão foi criado um método
# extrai_saldo() na classe ContaSalario e o retorno desse método é que será usado como critério de
# ordenação.
cs1 = ContaSalario(1)
cs1.deposita(620)
cs2 = ContaSalario(2)
cs2.deposita(505)
cs3 = ContaSalario(3)
cs3.deposita(1054)

contas = [cs1, cs2, cs3]
contas_ordenadas_por_saldo = sorted(contas, key=ContaSalario.extrai_saldo)

print('Contas salário ordenadas por saldo\n')
for conta_salario in contas_ordenadas_por_saldo:
    print(conta_salario.extrai_saldo())

# Uma abordagem mais limpa para realizar a ordenação baseada no saldo é acessar o atributo por seu
# nome sem a necessidade de expô-lo. Para isso usamos o método attrgetter da classe operator.
# Com essa abordagem o método extrai_saldo() que foi implementado para atender à solução anterior
# poderia ser removido da classe ContaSalario.
# Então a ordenação passaria a ser feita da seguinte maneira:
from operator import attrgetter
contas_ordenadas_por_saldo = sorted(contas, key=attrgetter("_saldo"))
print('Contas salário ordenadas por saldo usando attgetter\n')
for conta_salario in contas_ordenadas_por_saldo:
    print(conta_salario.extrai_saldo())

# Outra abordagem ainda mais simples é implementar na classe a ser ordenada o método __lt__
# Isso permitirá que duas instâncias do mesmo objeto possam ser comparadas utilizando-se o
# operador < que é justamente o operador utilizado em operações de ordenação. A implementação
# do método __lt__ permite inclusive que instâncias desse objeto possam ser utilizadas em
# comparações com o operador > sem a necessidade de se implementar o método __gt__. Isso porque
# __gt__ é simplesmente o oposto de __lt__.
# Como esse método já foi implementado na classe ContaSalario, a ordenção agora pode ser
# feita diretamente.
contas_ordenadas_por_saldo = sorted(contas)
print('Contas salário ordenadas após implentação do método __lt__\n')
for conta_salario in contas_ordenadas_por_saldo:
    print(conta_salario.extrai_saldo())