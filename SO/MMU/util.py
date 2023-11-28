import random
from random import choice

def criarListaProcessos(aleatorio, lote, qtdProExe, swap, listaProcessos):
    procExec = []
    if lote:
        if qtdProExe > swap.qtdProcessos():
            return '', "Quantidade de processos a serem executados maior que o número de processos na SWAP"
        if aleatorio:
            procPoss = list(range(1, swap.qtdProcessos() + 1))
            random.shuffle(procPoss)
            procExec = [f'P{num}' for num in procPoss[:qtdProExe]]
            return procExec, "Sucesso"
        else:
            if len(listaProcessos) != qtdProExe:
                return '', "Quantidade de processos a serem executados é diferente da quantidade de processos na lista de processos"
            if len(set(listaProcessos)) != len(listaProcessos):
                return '', "Lote está marcado, não se pode repetir processos"
            for proc in listaProcessos:
                if int(proc[1:]) > 0 and int(proc[1:]) < swap.qtdProcessos()+1:
                    procExec.append(proc)
                else:
                    return '', "Um processo na lista de processos não está presente na SWAP"
            return procExec, "Sucesso"
    if aleatorio:
        procPoss = [*range(1, swap.qtdProcessos()+1)]
        for i in range(0, qtdProExe):
            index = choice([*range(0,len(procPoss))])
            procExec.append(f'P{procPoss[index]}')
        return procExec, "Sucesso"
    if len(listaProcessos) != qtdProExe:
        return '', "Quantidade de processos a serem executados é diferente da quantidade de processos na lista de processos"
    for proc in listaProcessos:
        if int(proc[1:]) > 0 and int(proc[1:]) < swap.qtdProcessos()+1:
            procExec.append(proc)
        else:
            return '', "Um processo na lista de processos não está presente na SWAP"
    return procExec, "Sucesso"