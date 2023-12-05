from time import sleep
from random import choice
import copy
from math import ceil

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
    def __init__(self, x, yProcessos, sizePaginas, qtdPaginas, swapAle):
        self.X = x
        self.Y = yProcessos
        self.size = sizePaginas
        self.tamanho = qtdPaginas
        self.paginas = []
        self.listaExec = []
        self.swapAle = swapAle

    def addListaExec(self, lista):
        self.listaExec = lista

    def addPagina(self, pagina):
        self.paginas.append(pagina)
    
    def popPagina(self, posPagina): # precisa ser a posição da página
        self.paginas.pop(posPagina)

    def getPageFromSWAP(self):
        if self.swapAle:
            time = choice([*range(1,11)])
        else:
            time = 1
        sleep(time/100)

    def print(self):
        print(f'Procentagem Inical dos Processos: {self.Y*100}%, Tamanho das Páginas: {self.size}kB, Quantidade de Páginas: {self.tamanho}, Espaço Total: {self.size * self.tamanho}kB, Lista de Execução: {self.listaExec}')
        for page in self.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class Algoritmo:
    def __init__(self, memoria):
        self.memoria = copy.deepcopy(memoria)
        self.pageMiss = 0
        self.tempo = 0
        self.currentIndex = ""
        self.currentProc = None
        self.currentPage = -1

    def incPM(self):
        self.pageMiss += 1

    def incTimer(self, valor):
        self.tempo += valor
    
    def isFull(self):
        return True if self.memoria.tamanho == len(self.memoria.paginas) else False
    
    def tamanhoMemoria(self):
        tamanho = self.memoria.size * self.memoria.tamanho
        
        if tamanho / 1024 >= 1:
            tamanho /= 1024
            if tamanho / 1024 >= 1:
                tamanho /= 1024
                tamanho = str(tamanho) + 'GB'
            else:
                tamanho = str(tamanho) + 'MB'
        else:
            tamanho = str(tamanho) + 'kB'

        return tamanho

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

def criandoMemorias(swap, procExec, vetorX, Y, pageSize, swapAle):
    memorias = []
    
    qtdPags = 0
    for proc in swap.processos:
        qtdPags += swap.processos[proc].qtdPag
    
    for X in vetorX:
        qtdPaginas = round(qtdPags * (X/100))
        if qtdPaginas == 1:
            return None, 'Uma das memórias passadas terá espaço para só uma página!'

        memoria = Memoria(X, (Y/100), pageSize, qtdPaginas, swapAle)

        adicionados = list()
        for proc in procExec:
            processo = swap.findProcesso(proc)
            qtdPagProc = ceil(processo.qtdPag * memoria.Y)
            if not(proc in adicionados):
                if len(memoria.paginas) + qtdPagProc <= memoria.tamanho:
                    for i in range(0,qtdPagProc):
                        memoria.addPagina({'page': processo.pagIni + i, 'R': 0, 'processo': proc})
                    adicionados.append(proc)
        memoria.addListaExec(procExec)

        memorias.append(memoria)
    
    return memorias, 'Sucesso'