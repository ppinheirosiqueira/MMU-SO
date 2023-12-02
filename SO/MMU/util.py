import random
from random import choice
from . import algoritmos
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def criarListaProcessos(aleatorio, lote, qtdProExe, swap, listaProcessos):
    listaProcessos = [item.strip() for item in listaProcessos]
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

def PreencherListaAlgoritmo(memorias, alg_exec):
    algoritmo = []
    print(alg_exec)
    for key,item in alg_exec.items( ):
        if item:
            match key:
                case 'rand':
                    algoritmo.append(algoritmos.Random(memorias[0]))
                case 'nru':
                    algoritmo.append(algoritmos.NRU(memorias[0]))
                case 'fifo':
                    algoritmo.append(algoritmos.FIFO(memorias[0]))
                case 'sc':
                    algoritmo.append(algoritmos.SC(memorias[0]))
                case 'relogio':
                    algoritmo.append(algoritmos.Relogio(memorias[0]))
                case 'lru':
                    algoritmo.append(algoritmos.LRU(memorias[0]))
                case 'envelhecimento':
                    algoritmo.append(algoritmos.Envelhecimento(memorias[0]))
    return algoritmo

def ExecutarAlgoritmos(memorias, alg_exec, swap, resultados):
    for mem in memorias:
        mem_data = {}

        if alg_exec['rand']:
            rand_algo = algoritmos.Random(mem)
            rand_algo.Rand(swap)
            mem_data.update({"Random": {"PageMiss": rand_algo.pageMiss, "TempSubs": rand_algo.tempo}})
            del rand_algo

        if alg_exec['nru']:
            nru_algo = algoritmos.NRU(mem)
            nru_algo.NRU(swap)
            mem_data.update({"NRU": {"PageMiss": nru_algo.pageMiss, "TempSubs": nru_algo.tempo}})
            del nru_algo

        if alg_exec['fifo']:
            fifo_algo = algoritmos.FIFO(mem)
            fifo_algo.FIFO(swap)
            mem_data.update({"FIFO": {"PageMiss": fifo_algo.pageMiss, "TempSubs": fifo_algo.tempo}})
            del fifo_algo

        if alg_exec['sc']:
            sc_algo = algoritmos.SC(mem)
            sc_algo.SC(swap)
            mem_data.update({"SC": {"PageMiss": sc_algo.pageMiss, "TempSubs": sc_algo.tempo}})
            del sc_algo

        if alg_exec['relogio']:
            relogio_algo = algoritmos.Relogio(mem)
            relogio_algo.Relogio(swap)
            mem_data.update({"Relogio": {"PageMiss": relogio_algo.pageMiss, "TempSubs": relogio_algo.tempo}})
            del relogio_algo
        
        if alg_exec['lru']:
            lru_algo = algoritmos.LRU(mem)
            lru_algo.LRU(swap)
            mem_data.update({"LRU": {"PageMiss": lru_algo.pageMiss, "TempSubs": lru_algo.tempo}})
            del lru_algo

        if alg_exec['envelhecimento']:
            envelhecimento_algo = algoritmos.Envelhecimento(mem)
            envelhecimento_algo.Envelhecimento(swap)
            mem_data.update({"Envelhecimento": {"PageMiss": envelhecimento_algo.pageMiss, "TempSubs": envelhecimento_algo.tempo}})
            del envelhecimento_algo

        resultados.update({f"{mem.X}": mem_data})
    return resultados

def GenerateDataToAlgoritmo(algoritmo):
    nome = algoritmo.nome
    
    pageMiss = algoritmo.pageMiss
    
    tempo = algoritmo.tempo 
    
    if algoritmo.currentPage == -1:
        pagina = ""
    else:
        pagina = str(algoritmo.currentPage)
    
    memNova = GenerateMemoryHtml(algoritmo)

    return nome, pageMiss, tempo, pagina, memNova

def GenerateMemoryHtml(algoritmo):
    htmlMemoria = "<table class='memoria'>"
    
    htmlMemoria += "<tr class='pagina'><th>Página</th>"
    
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page["page"]}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"

    htmlMemoria += "</tr>"

    htmlMemoria += "<tr class='bit'><th>R Bit</th>"
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page["R"]}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"
    htmlMemoria += "</tr>"
    
    htmlMemoria += "<tr class='processo'><th>Processo</th>"
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page["processo"]}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"
    htmlMemoria += "</tr>"
    
    htmlMemoria += "</table>"
    return htmlMemoria

def GererateGraphs(resultado):
    objects = ['12/10/2019','12/11/2020','15/10/2020']
    y_pos = [0, 1, 2]
    qty = [10,20,25]
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Quantity')
    plt.title('Sales')
    plt.savefig('static/imgs/barchart.png')