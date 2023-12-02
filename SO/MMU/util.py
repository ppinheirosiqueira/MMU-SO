import random
from random import choice
from . import algoritmos

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
    
    memNova = """<div class='memoria'>
        <div class='pagina'>
            <div class='page'>
                Página
            </div>
            <div class='reference'>
                Bit R
            </div>
            <div class='process'>
                Processo
            </div>
        </div>"""
    for page in algoritmo.memoria.paginas:
        memNova += f"""
        <div class='pagina'>
            <div class='page'>
                {page["page"]}
            </div>
            <div class='reference'>
                {page["R"]}
            </div>
            <div class='process'>
                {page["processo"]}
            </div>
        </div>"""
    memNova += "</div>"

    return nome, pageMiss, tempo, pagina, memNova