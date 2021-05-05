import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype = int)

    def pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    
    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilha_cheia():
            print('A pilha está cheia.')
        else:
            self.topo += 1
            self.valores[self.topo] = valor
    
    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia.')
        else:
            self.topo -= 1
    
    def ver_topo(self):
        if self.topo != -1:
            print(self.valores[self.topo])
        else:
            print(-1) 

pilha = Pilha(9)

for i in range(pilha.capacidade):
    pilha.empilhar(i)
    pilha.ver_topo()

for i in range(pilha.capacidade + 1):
    pilha.desempilhar()
    pilha.ver_topo()