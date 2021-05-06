import numpy as np
import random as rd
class FilaPrioridade:

    def __init__(self, capacidade):
        self. capacidade = capacidade
        self.numero_elementos = 0 
        self.valores = np.empty(self.capacidade, dtype = int)

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def fila_vazia(self):
        return self.numero_elementos == 0

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia.')
        
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x+1] = valor
            self.numero_elementos += 1 

    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila está vazia.')
        else:
            valor = self.valores[self.numero_elementos - 1]
            self.numero_elementos -= 1 
            return valor


    def primeiro(self):
        if self.fila_vazia():
            print(-1)
        else:
            print(self.valores[self.numero_elementos - 1])


fila = FilaPrioridade(5)

for i in range(fila.capacidade):
    x = rd.randrange(0, 150, 1)
    print(x)
    fila.enfileirar(x)
    fila.primeiro()