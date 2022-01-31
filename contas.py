#
# Torna a classe Conta abstrata. Embora ela possua alguns métodos implementados, o fato dela
# possuir um único método abstrato a torna automaticamente uma classe abstrata.
#
#
from abc import ABCMeta, abstractmethod
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>> Código {} Saldo {} <<<]".format(self._codigo, self._saldo)

    #
    # Define o método passa_o_mes abstrato.
    @abstractmethod
    def passa_o_mes(self):
        pass

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

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

#
# A tentativa de criar uma instância de ContaInvestimento resultará em erro uma vez que essa classe
# não implementa o método abstrato passa_o_mes definido na classe Conta:
# TypeError: Can't instantiate abstract class ContaInvestimento with abstract method passa_o_mes
#
# ci = ContaInvestimento(18) # Está comentado pois esse código não funciona.
