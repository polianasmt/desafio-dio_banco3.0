from abc import ABC, abstractmethod
import os

class conta:

    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    def saldo(self):
        pass
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            os.system('cls')
            print("Não foi possivel realizar o saque por falta de saldo.")
    
        else:
            os.system('cls')
            print(f"O saque de R$ {valor} foi realizado com sucesso.")
            numero_saque += 1
            extrato += f"\nSaque: R$ {valor:.2f}."
            self._saldo -= valor

        return False
    
    @property
    def depositar(self, valor):
        pass

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico


class conta_corrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    pass

class cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        pass

class pessoa_fisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class transacao(ABC):
    @abstractmethod
    def regitrar(self, conta):
        pass

class deposito(transacao):
    def regitrar(self, conta):
        pass

class saque(transacao):
    def regitrar(self, conta):
        pass

