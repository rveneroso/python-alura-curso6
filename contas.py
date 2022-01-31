class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>> Código {} Saldo {} <<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

#
# Cria uma conta do tipo ContaCorrente
#
cc = ContaCorrente(16)
cc.deposita(1000)
cc.passa_o_mes() # O saldo deve ser de 998 reais
print(cc)

#
# Cria uma conta do tipo ContaPoupanca
#
cp = ContaPoupanca(17)
cp.deposita(1000)
cp.passa_o_mes() # O saldo deve ser de 1007 reais
print(cp)

#
# Aplicando polimorfismo em uma lista
#
# Reinicia cc e cp
cc = ContaCorrente(16)
cc.deposita(1000)
cp = ContaPoupanca(17)
cp.deposita(1000)

contas = [cc, cp] # A lista contém objetos do tipo Conta
for conta in contas:
    conta.passa_o_mes()
    print(conta) # O resultado será o mesmo obtido antes de se usar lista