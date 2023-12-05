import numpy as np
from random import choice
from time import time
from . import classes
class Random(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "Random"

    def Rand(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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

                if self.isFull():
                    retirado = choice(self.memoria.paginas)
                    retirado.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})

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

class NRU(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "NRU"

    def NRU(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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

                if self.isFull():
                    notReferenced = [item for item in self.memoria.paginas if item["R"] == 0]
                    
                    if len(notReferenced) > 0:
                        retirado = choice(notReferenced)
                        retirado.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                    else:
                        retirado = choice( self.memoria.pagina)
                        retirado.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})

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
        print(f"Algoritmo: NRU, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class FIFO(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "FIFO"

    def FIFO(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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

                if self.isFull():
                    self.memoria.paginas.pop(0)
                    self.memoria.paginas.append({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})

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
        print(f"Algoritmo: FIFO, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class SC(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "SC"

    def SC(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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

                if self.isFull():
                    while True:
                        if self.memoria.paginas[0]["R"] == 1:
                            self.memoria.paginas[0].update({"R": 0})
                            self.memoria.paginas.sort(key=self.memoria.paginas[0].__eq__)
                        else:
                            self.memoria.paginas.pop(0)
                            self.memoria.paginas.append({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                            break
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})

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
        print(f"Algoritmo: Segunda Chance, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class Relogio(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.pointer = 0
        self.nome = "Relogio"

    def Relogio(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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
                
                if self.isFull():
                    while True:
                        if self.memoria.paginas[self.pointer]["R"] == 1:
                            self.memoria.paginas[self.pointer].update({"R": 0})
                            self.pointer += 1
                            if self.pointer == len(self.memoria.paginas):
                                self.pointer = 0
                        else:
                            self.memoria.paginas[self.pointer].update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                            self.pointer += 1
                            if self.pointer == len(self.memoria.paginas):
                                self.pointer = 0
                            break
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})

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
        print(f"Algoritmo: Relógio, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")

class LRU(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "LRU"
        self.matriz = np.array(np.zeros((memoria.tamanho,memoria.tamanho)))
        
        for i in range(0,len(self.memoria.paginas)):
            self.memoria.paginas[i].update({'line': i})

    def LRU(self, swap):
        while self.Step(swap) : pass

    def Step(self, swap):
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
                
                if self.isFull():
                    soma_linhas = (self.matriz.sum(axis=1)).tolist()
                    menor_linha = soma_linhas.index(min(soma_linhas))

                    menor_pagina = ([item for item in self.memoria.paginas if item["line"] == menor_linha])[0]
                    menor_pagina.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex, "line": menor_linha})
                    
                    self.UpdateLineColumn(menor_linha)
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex, 'line': len(self.memoria.paginas)})
                    
                    self.UpdateLineColumn(len(self.memoria.paginas)-1)

                end_time = time()
                
                self.incTimer(end_time-start_time)
            else:
                self.memoria.paginas[indexPag].update({"R": 1})
                self.UpdateLineColumn(self.memoria.paginas[indexPag]["line"])

            if self.currentPage == self.currentProc.pagFin:
                self.currentIndex = ""
                self.memoria.listaExec.pop(0)
            
            return True
        else:
            return False
        
    def UpdateLineColumn(self, index):
        self.matriz[index] = np.ones(self.memoria.tamanho)
        self.matriz[:,index] = np.zeros(self.memoria.tamanho)

    def tamanhoMemoria(self):
        tamanho = super().tamanhoMemoria()
        matriz = self.memoria.tamanho * self.memoria.tamanho
        return tamanho + ' + ' + str(matriz) + ' contadores'

    def print(self):
        print(f"Algoritmo: LRU, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}, Line: {page['line']}")


class Envelhecimento(classes.Algoritmo):
    def __init__(self, memoria):
        super().__init__(memoria)
        self.nome = "Envelhecimento"
        self.matriz = np.array(np.zeros((memoria.tamanho,8)))

    def Envelhecimento(self, swap):
        while self.Step(swap) : pass
    
    def Step(self, swap):
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

                if self.isFull():
                    
                    soma_linhas = (self.matriz.sum(axis=1)).tolist()
                    menores_linhas = np.where(soma_linhas == np.min(soma_linhas))[0]
                    
                    pagina_index = choice(menores_linhas)
                    menor_pagina = self.memoria.paginas[pagina_index]

                    menor_pagina.update({"page": self.currentPage, "R": 0, "processo": self.currentIndex})
                    self.RollMatriz()
                else:
                    self.memoria.addPagina({'page': self.currentPage, 'R': 0, 'processo': self.currentIndex})
                    self.RollMatriz()

                end_time = time()
                    
                self.incTimer(end_time-start_time)
            else:
                self.memoria.paginas[indexPag].update({"R": 1})
                self.RollMatriz()

            if self.currentPage == self.currentProc.pagFin:
                self.currentIndex = ""
                self.memoria.listaExec.pop(0)
            
            return True
        else:
            return False
        
    def RollMatriz(self):
        self.matriz = np.roll(self.matriz, shift=1, axis=1)
        referencias = list(x["R"] for x in self.memoria.paginas)
        if len(referencias) < self.memoria.tamanho:
            for x in range(self.memoria.tamanho-len(referencias)):
                referencias.append(0)
        referencias = np.array(referencias)
        referencias = referencias[...,None]
        self.matriz[:, 0] = referencias.flatten()

    def tamanhoMemoria(self):
        tamanho = super().tamanhoMemoria()
        matriz = self.memoria.tamanho * 8
        return tamanho + ' + ' + str(matriz) + ' contadores'

    def print(self):
        print(f"Algoritmo: Envelhecimento, PageMiss: {self.pageMiss}, Tempo de Subistituição: {self.tempo}s")
        for page in self.memoria.paginas:
            print(f"Page: {page['page']}, R: {page['R']}, Processo: {page['processo']}")