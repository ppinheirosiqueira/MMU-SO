import numpy as np

class Processo:
    def __init__(self, pagIni, pagFin):
        self.pagIni = pagIni
        self.pagFin = pagFin
        self.qtdPag = pagFin - pagIni + 1

class SWAP:
    def __init__(self):
        self.processos = {}
        self.totalPag = 0

    def addProcesso(self, nome, processo):
        self.processos.update({nome:processo})

    def findProcesso(self,nome):
        return self.processos[nome]
    
    def attTotal(self, valor):
        self.totalPag = valor

    def print(self):
        for chave, valor in self.processos.items():
            print(f'Chave: {chave}, QtdPag: {valor.qtdPag}')

class Memoria:
    def __init__(self, qtdPaginas):
        self.tamanho = qtdPaginas
        self.paginas = []

    def addPagina(self, pagina):
        self.paginas.append(pagina)
    
    def popPagina(self, posPagina): # precisa ser a posição da página
        self.paginas.pop(posPagina)

class Algoritmo:
    def __init__(self, memoria):
        self.memoria = memoria.copy()
        self.pageMiss = 0
        self.tempo = 0

    def incPM(self):
        self.pageMiss += 1

    def incTimer(self, valor):
        self.tempo += valor

class Envelhecimento(Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.matriz = np.array(np.zeros((memoria.tamanho,memoria.tamanho)))

class LRU(Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.matriz = np.array(np.zeros((memoria.tamanho,8)))