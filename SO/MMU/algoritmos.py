import numpy as np
from random import choice
from time import time
from . import classes
class Random(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)

    def Rand(self, swap):
        while self.RandStep(swap): pass

    def RandStep(self, swap):
        if len(self.memoria.listaExec) > 0 or self.currentIndex != "":
            if self.currentIndex == "":
                self.currentIndex = self.memoria.listaExec[0]
                self.currentProc = swap.findProcesso(self.currentIndex)
                self.currentPage = self.currentProc.pagIni
            else:
                self.currentPage += 1

            indexPag = next((i for i, item in enumerate(self.memoria.paginas) if item["page"] == self.currentPage), None)
                
            if indexPag == None:
                self.incPM()
                
                start_time = time()
                
                self.memoria.getPageFromSWAP()

                possPags = [item for item in self.memoria.paginas if item["processo"] != self.currentIndex]
                
                if len(possPags) > 0:
                    retirado = choice(possPags)
                    retirado.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                else:
                    retirado = choice(self.memoria.paginas)
                    retirado.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})

                end_time = time()
                
                self.incTimer(end_time-start_time)
            else:
                self.memoria.paginas[indexPag].update({"R": 1})

            if self.currentPage == self.currentProc.pagFin:
                self.currentIndex = ""
                self.memoria.listaExec.pop(0)
            
            return True
        else:
            return False
                   
    def print(self):
        print(f"Algoritmo: Random, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class Envelhecimento(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.matriz = np.array(np.zeros((memoria.tamanho,memoria.tamanho)))

class LRU(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.matriz = np.array(np.zeros((memoria.tamanho,8)))