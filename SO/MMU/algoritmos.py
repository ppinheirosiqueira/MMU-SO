from random import choice, randint
from time import time

def Rand(algo,swap):
    while len(algo.memoria.listaExec) > 0:
        inicio = algo.memoria.listaExec.pop(0)
        processo = swap.findProcesso(inicio)
        page = processo.pagIni
        while page <= processo.pagFin:
            indexPag = next((i for i, item in enumerate(algo.memoria.paginas) if item["page"] == page), None)
            
            if indexPag == None:
                algo.incPM()

                seed = randint(1, 100000)
                
                start_time = time()
                
                algo.memoria.getPageFromSWAP(seed)

                possPags = [item for item in algo.memoria.paginas if item["processo"] != inicio]
                
                if len(possPags) > 0:
                    retirado = choice(possPags)
                    retirado.update({"page": page, "R": 0, "processo": inicio})
                else:
                    retirado = choice(algo.memoria.paginas)
                    retirado.update({"page": page, "R": 0, "processo": inicio})

                end_time = time()
                
                algo.incTimer(end_time-start_time)
            else:
                algo.memoria.paginas[indexPag].update({"R": 1})

            page += 1