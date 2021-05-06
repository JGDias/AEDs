import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype = int)

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def fila_vazia(self):
        return self.numero_elementos == 0

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia.')
            return

        elif self.final == self.capacidade - 1:
            self.final = -1
        
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1
    
    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila está vazia.')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp
    
    def ver_inicio(self):
        if self.fila_vazia():
            print(-1)
        else:
            print(self.valores[self.inicio])


fila = FilaCircular(5)

for i in range(fila.capacidade):
    fila.enfileirar(i)
    fila.ver_inicio()

print(fila.valores)

fila.desenfileirar()
fila.ver_inicio()
print(fila.valores)

fila.enfileirar(6)
print(fila.valores)
fila.desenfileirar()
fila.ver_inicio()