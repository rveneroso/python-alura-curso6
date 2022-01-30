class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>> Código {} Saldo {} <<<]".format(self.codigo, self.saldo)

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

