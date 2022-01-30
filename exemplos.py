#
# Criação de uma lista simples.
idades = [39, 30, 27, 18]

#
# Irá exibir <class 'list'>
#
type(idades)

#
# Irá exibir a quantidade de elmentos na lista. No caso, 4.
#
len(idades)

#
# Exibe o elemento na primeira posição da lista (índice 0)
#
idades[0]

#
# Exibe todos os elementos da lista
#
idades

print(idades[1]) # Exibe o segundo elemento da lista (índice 1)
print(idades[2]) # Exibe o terceiro elemento da lista (índice 2)
print(idades[3]) # Exibe o quarto elemento da lista (índice 3)
#
# Exibe a mensagem de erro IndexError: list index out of range já que a lista não possui um quinto elemento
#
print(idades[4])

idades.append(15) # Adiciona o elemento 15 após o último elemento da lista

idades

idades[4] # Agora exibe o elemento 15, adicionado pelo comando append acima.

idades[5] # Exibe a mensagem de erro IndexError: list index out of range já que a lista não possui um sexto elemento

#
# Percorre cada um dos elementos da lista e o imprime
for idade in idades:
  print(idade)

idades.remove(30) # Remove o primeiro elemento que for encontrado cujo valor seja 30.

idades

#
# Exibe a mensagem de erro ValueError: list.remove(x): x not in list pois não há mais o elemento 30 na lista
# (ele foi removido pelo comando remove() acima.
#
idades.remove(30)

idades.append(15) # Adiciona mais um elemento de valor 15 à lista (já existia um valor 15).

idades

#
# Remove o primeiro elemento 15 encontrado na lista. Antes dessa operação havia 2 elementos com valor 15.
# Após a operação ainda restará um elemento de valor 15.
#
idades.remove(15)

idades

idades.append(27) # Adiciona um elemento 27 à lista. Agora há dois elementos 27 na lista.

#
# Remove o primeiro elemento 27 que for encontrado. O elemento adicionado acima permanecerá na lista, sendo seu
# último elemento.
#
idades.remove(27)
idades


28 in idades # Retorna False pois 28 não está em idades

15 in idades # Retorna True pois 15 está em idades

#
# Verifica se o elemento 15 está em idades antes de tentar removê-lo para não levantar
# ValueError: list.remove(x): x not in list
#
if 15 in idades:
  idades.remove(15)

# Insere o elemento 20 na primeira posição da lista.
idades.insert(0, 20)
idades

#
# Reinicia a lista com os elementos 20, 39 e 18.
#
idades = [20, 39, 18]

#
# Ao contrário do que se possa imaginar, a linha abaixo não vai inserir dois novos elementos (27 e 19) à lista;
# será inserida uma lista contendo os elementos 27 e 19 à lista que já existia.
#
idades.append([27, 19])

#
# Ao imprimir a lista idades podemos ver que seu conteúdo agora é [20, 39, 18, 15, 27, [27, 19]] e não
# [20, 39, 18, 15, 27, 27, 19] como se poderia pensar.
#
idades

#
# Reinicia a lista com os elementos 20, 39 e 18.
#
idades = [20, 39, 18]

#
# Agora sim serão adicionados dois novos elementos ao fim da lista: 27 e 19.
#
idades.extend([27, 19])

idades # Exibirá [20, 39, 18, 27, 19]

# Cria uma lista vazia
idades_no_ano_que_vem = []
for idade in idades:
  # Adiciona à lista recém criada cada um dos elementos presentes na lista idades, porém acrescido de 1.
  idades_no_ano_que_vem.append(idade+1)

idades_no_ano_que_vem # Imprimirá [21, 40, 19, 28, 20]

# Uma maneira mais simples de realizar o trabalho do bloco mostrado acima é fazer tudo em uma única linha:
idades_no_ano_que_vem = [idade+1 for idade in idades]
idades_no_ano_que_vem

# Cria uma lista anônima que será composta por todos os elementos da lista idades cujo valor seja > 21.
# A lista original idades permanecerá inalterada.
[idade for idade in idades if idade > 21]

def proximo_ano(idade):
    return idade+1

#
# Será criada uma lista anônima onde cada elemento será a idade vinda da lista idades acrescida de 1. Porém,
# somente os elementos cujo valor seja > 21 serão passados à função proximo_ano.
# O resultado final será uma lista com 2 elementos: 40 (idade 39 + 1) e 28 (idade 27 + 1)
#
[proximo_ano(idade) for idade in idades if idade > 21]

#
# A função abaixo foi criada para mostrar como o Python - assim como o Java - passa objetos por referência aos
# métodos e funções. Isso significa que, se o objeto for alterado dentro da função, essa alteração permanecerá
# no objeto mesmo quando a função tiver sua execução encerrada.
#
def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades) # A função irá imprimir o tamanho de lista (5 elementos).
idades # Aqui já veremos a lista com 6 elementos sendo que o sexto elemento (13) foi adicionado dentro da funão.

#
# Aqui temos uma função que cria uma lista vazia em sua primeira execução caso nenhuma lista seja passada
# à ela.
#
def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

#
# Nas 4 chamadas consecutivas da função faz_processamento_de_visualizacao() podemos ver que, a cada chamada,
# um novo elemento 13 é adicionado ao fim da lista. Isso acontece porque somente na primeira chamada da função
# o Python irá criar um novo objeto lista em memória. Nas chamadas subsequentes será usado o objeto que já está
# na memória. Daí o que temos é que, à cada chamada, teremos um novo elemento 13 adicionado à lista existente.
#
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

#
# A sintaxe abaixo, embora seja um pouco diferente da primeira versão, apresenta o mesmo problema: o objeto lista
# será criado uma única vez e nas chamadas subsequentes um novo elemento 13 será adicionado a ele.
#
def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

#
# Essa é a maneira correta de fazer com que um novo objeto lista seja criado sempre que a função for chamada sem
# que uma lista seja passada a ela.
#
def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    #
    # Se nenhuma lista foi passada à função, uma nova lista será criada. Porém, o escopo dessa nova lista será
    # somente a função. Ela não existirá mais tão logo a função chegue ao fim de sua execução.
    #
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

# Todas as chamadas abaixo exibirão 0 e [].
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()



