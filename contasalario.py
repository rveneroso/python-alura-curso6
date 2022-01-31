class ContaSalario:

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>> Conta {} Saldo {} <<<]".format(self._codigo, self._saldo)

    #
    # O método __lt__ (less than) permite que duas instâncias de uma mesma classe possam ser
    # comparadas através do operador <
    #
    def __lt__(self, other):
        return self._saldo < other._saldo

    def __eq__(self, other):
        #
        # Outra forma de testar o tipo de um objeto é através do operador isinstance. Esse operador retorna true
        # sempre que um objeto for do tipo de uma classe específica ou de qualquer subclasse daquela classe
        # específica. O operador isinstance é o equivalente em Python do instanceof de Java.
        # if(other isinstance ContaSalario)...
        if(type(other) != ContaSalario):
            return False
        return self._codigo == other._codigo

    def extrai_saldo(self):
        return self._saldo

cs = ContaSalario(23)
cs.deposita(200)
print(cs)

cs2 = ContaSalario(23)

if(cs == cs2):
    print('cs e cs2 são iguais')
else:
    print('cs e cs2 são diferentes')

#
# A implementação do método __eq__ permite que operações in envolvendo listas funcionem corretamente.
#
lista_contas = [cs]
print(cs2 in lista_contas) # Retorna true pois cs e cs2 são iguais.

lista_contas = [cs2]
print(cs in lista_contas) # Também retorna true pois cs2 e cs são iguais.

# Testando a igual com contas de tipos diferentes
from contas import ContaCorrente
cc = ContaCorrente(23)
if(cc == cs2):
    print('cc e cs2 são iguais')
else:
    print('cc e cs2 não são iguais') # Isso é o que será impresso já que o método __eq__ agora testa o tipo do objeto.
