class Processo:
    def __init__(self, nome, pagIni, pagFin):
        self.nome = nome
        self.pagIni = pagIni
        self.pagFin = pagFin

class Memoria:
    def __init__(self, qtdPaginas):
        self.tamanho = qtdPaginas
        self.paginas = []
        self.pagRef = []

    def addPagina(self, pagina):
        self.paginas.append(pagina)
        self.pagRef.append(0)
    
    def popPagina(self, posPagina): # precisa ser a posição da página
        self.paginas.pop(posPagina)
        self.pagRef.pop(posPagina)