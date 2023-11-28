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
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

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

def criandoSWAP(swap, vetorQtdPro,vetorTamPro):
    aux = 1
    auxPag = 0
    while len(vetorQtdPro) > 0:
        index = choice([*range(0,len(vetorQtdPro))]) # Sorteia uma tamanho de página aleatória do vetor de processos
        pagFin = auxPag + int(vetorTamPro[index]) - 1 # A página final é igual a inicial + o tamanho do processo - 1
        # o -1 é necessário, pois imaginando que o processo tenha 5 páginas, comece na 0, somando 5, o processo teria 6 páginas, pois iria da 0 até a 5
        procAux = Processo(auxPag, pagFin) # Criar o processo
        auxPag = pagFin + 1 # a próxima página inicial é uma a mais da ultima do último processo
        swap.addProcesso(f'P{aux}',procAux) # coloco o processo na swap
        aux += 1 # auxiliar só para o nome do processo
        vetorQtdPro[index] = int(vetorQtdPro[index]) - 1 # diminuo em 1 a quantidade de processos que estou olhando
        if vetorQtdPro[index] == 0: # se o primeiro valor estiver zerado, retiro ele, pois não existem mais processos desse tamanho
            vetorQtdPro.pop(index)
            vetorTamPro.pop(index)
    swap.attTotal(pagFin + 1) # o total de páginas da swap é igual o valor da pagina final + 1, já q tem a página 0
    return swap, 'Sucesso'