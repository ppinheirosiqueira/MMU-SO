import numpy as np
from time import sleep
from random import choice, seed
import copy

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
    
    def qtdProcessos(self):
        return len(self.processos)

    def print(self):
        for chave, valor in self.processos.items():
            print(f'Chave: {chave}, QtdPag: {valor.qtdPag}, PagIni: {valor.pagIni}, PagFin: {valor.pagFin}')

class Memoria:
    def __init__(self, yProcessos, sizePaginas, qtdPaginas):
        self.Y = yProcessos
        self.size = sizePaginas
        self.tamanho = qtdPaginas
        self.paginas = []
        self.listaExec = []

    def addListaExec(self, lista):
        self.listaExec = lista

    def addPagina(self, pagina):
        self.paginas.append(pagina)
    
    def popPagina(self, posPagina): # precisa ser a posição da página
        self.paginas.pop(posPagina)

    def getPageFromSWAP(self, semente):
        seed(semente)
        time = choice([*range(1,11)])
        sleep(time/100)

    def print(self):
        print(f'Procentagem Inical dos Processos: {self.Y*100}%, Tamanho das Páginas: {self.size}kB, Quantidade de Páginas: {self.tamanho}, Espaço Total: {self.size * self.tamanho}kB, Lista de Execução: {self.listaExec}')
        for page in self.paginas:
            print(f'Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}')

class Algoritmo:
    def __init__(self, nome, memoria):
        self.nome = nome
        self.memoria = copy.copy(memoria)
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