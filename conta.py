class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>> Código {} Saldo {} <<<]".format(self.codigo, self.saldo)

    def deposita_para_todas_contas(contas, valor):
        for conta in contas:
            conta.deposita(valor)

    def __str__(self):
        return "Conta " + str(self.codigo) + " possui saldo de " + str(self.saldo)

#
# Utilizando lista contendo contas correntes
#
cc1 = ContaCorrente(70368)
cc1.deposita(500)

cc2 = ContaCorrente(13882)
cc2.deposita(1000)

#
# Assim como em Java, ao se incluir um objeto em uma lista, não estamos criando uma nova instância daquela classe.
# O que o Python faz é tão somente colocar na lista tão somente o endereço de memória onde aquele objeto está
# armazenado.
#
contasCorrentes = [cc1, cc2]
for cc in contasCorrentes:
    print(cc)

print('Antes do depósito')
for cc in contasCorrentes:
    print(cc)

ContaCorrente.deposita_para_todas_contas(contasCorrentes, 100)

print('Após o depósito')
for cc in contasCorrentes:
    print(cc)

#
# Listas são objetos mutáveis. Portanto, nada impede que alguém faça algo do tipo:
#contasCorrentes.insert(0,76)

# Porém, a linha acima 'destrói' a estrutura da lista pois ela passa a conter não apenas objetos
# do tipo ContaCorrente; agora ela contém também um int. Se a lista contasCorrentes for passada
# como parâmetro a um método que espera que todos os elementos da lista sejam do tipo ContaCorrente
# algum erro pode acontecer. É exatamente esse o caso da linha abaixo:
ContaCorrente.deposita_para_todas_contas(contasCorrentes, 100)

# A execução da linha acima resultará em um erro do tipo
# AttributeError: 'int' object has no attribute 'deposita'

#
# Listas não são recomendadas para representar objetos onde cada uma das posições dentro da lista
# tem um significado próprio. Supondo que eu queira criar uma lista para representar um usuário onde
# a posição 0 é o nome do usuário e a posição 1 é a idade do usuário. Não faz sentido criar algo
# do tipo:
#
# ['Ivan Piro', 45]
# ['Osmar Telo', 32]
#
# Para esses casos é recomendado o uso de tuplas. Por exemplo: pode-se criar tuplas representando
# um usuário pelo seu nome, sua idade e seu ano de nascimento da seguinte maneira
usuario1 = ('Ivan Piro', 45, 1973)
usuario2 = ('Osmar Telo', 32, 1982)

# Na tupla a posição da informação tem significado: nos exemplos acima o nome está sempre na posição
# 0, a idade na posição 1 e o ano de nascimento na posição 2.
# usuario3 = (39, 'Oscar Diologista', 1948) ==> quebraria toda a estrutura.
#
# Tuplas são imutáveis.
#

