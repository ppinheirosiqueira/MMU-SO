import random
from random import choice
from . import algoritmos
import plotly.offline as plot
import plotly.graph_objects as go
import numpy as np

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
            mem_data.update({"Random": {"PageMiss": rand_algo.pageMiss, "TempSubs": rand_algo.tempo, "Tamanho": rand_algo.tamanhoMemoria()}})
            del rand_algo

        if alg_exec['nru']:
            nru_algo = algoritmos.NRU(mem)
            nru_algo.NRU(swap)
            mem_data.update({"NRU": {"PageMiss": nru_algo.pageMiss, "TempSubs": nru_algo.tempo, "Tamanho": nru_algo.tamanhoMemoria()}})
            del nru_algo

        if alg_exec['fifo']:
            fifo_algo = algoritmos.FIFO(mem)
            fifo_algo.FIFO(swap)
            mem_data.update({"FIFO": {"PageMiss": fifo_algo.pageMiss, "TempSubs": fifo_algo.tempo, "Tamanho": fifo_algo.tamanhoMemoria()}})
            del fifo_algo

        if alg_exec['sc']:
            sc_algo = algoritmos.SC(mem)
            sc_algo.SC(swap)
            mem_data.update({"SC": {"PageMiss": sc_algo.pageMiss, "TempSubs": sc_algo.tempo, "Tamanho": sc_algo.tamanhoMemoria()}})
            del sc_algo

        if alg_exec['relogio']:
            relogio_algo = algoritmos.Relogio(mem)
            relogio_algo.Relogio(swap)
            mem_data.update({"Relogio": {"PageMiss": relogio_algo.pageMiss, "TempSubs": relogio_algo.tempo, "Tamanho": relogio_algo.tamanhoMemoria()}})
            del relogio_algo
        
        if alg_exec['lru']:
            lru_algo = algoritmos.LRU(mem)
            lru_algo.LRU(swap)
            mem_data.update({"LRU": {"PageMiss": lru_algo.pageMiss, "TempSubs": lru_algo.tempo, "Tamanho": lru_algo.tamanhoMemoria()}})
            del lru_algo

        if alg_exec['envelhecimento']:
            envelhecimento_algo = algoritmos.Envelhecimento(mem)
            envelhecimento_algo.Envelhecimento(swap)
            mem_data.update({"Envelhecimento": {"PageMiss": envelhecimento_algo.pageMiss, "TempSubs": envelhecimento_algo.tempo, "Tamanho": envelhecimento_algo.tamanhoMemoria()}})
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

def GenerateListHTML(lista,index):
    listaHTML = "<table class='lista'><tr>"
    for chave, proc in enumerate(lista):
        if chave == index:
            listaHTML += f"<td class='executando'>{proc}</td>"
        else:
            listaHTML += f'<td>{proc}</td>'
    listaHTML += "</tr></table>"

    return listaHTML

def GenerateMemoryHtml(algoritmo):
    htmlMemoria = "<table class='memoria'>"
    
    htmlMemoria += "<tr class='pagina'><th>Página</th>"
    
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page['page']}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"

    htmlMemoria += "</tr>"

    htmlMemoria += "<tr class='bit'><th>R Bit</th>"
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page['R']}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"
    htmlMemoria += "</tr>"
    
    htmlMemoria += "<tr class='processo'><th>Processo</th>"
    for page in algoritmo.memoria.paginas:
        htmlMemoria += f"<td>{page['processo']}</td>"
    
    if len(algoritmo.memoria.paginas) < algoritmo.memoria.tamanho:
        for x in range(algoritmo.memoria.tamanho - len(algoritmo.memoria.paginas)):
            htmlMemoria += "<td>X</td>"
    htmlMemoria += "</tr>"
    
    htmlMemoria += "</table>"
    return htmlMemoria

def GererateGraphs(resultado):
    graphs = {}
    width = 500
    height = 300

    page = 'Número de Page Miss por Algoritmo'
    temp = 'Tempo de substituição por Algoritmo'
    memo = []
    for key,items in resultado.items():
        graphs.update({f'{key}': {}})
        memo.append(key)
        data_nome = []
        data_page = []
        data_temp = []

        for chave,item in items.items():
            data_nome.append(chave)
            data_page.append(item['PageMiss'])
            data_temp.append(item['TempSubs']*1000)

        fig_page = go.Figure(data = go.Bar(name = page, x = data_page, y = data_nome, orientation = 'h', 
                                            marker=dict(color='rgba(207, 72, 72, 0.6)', line=dict(color='rgba(207, 72, 72, 1)', width=1))))
        fig_temp = go.Figure(data = go.Bar(name = temp, x = data_temp, y = data_nome, orientation = 'h', 
                                            marker = dict(color='rgba(107, 178, 144, 0.6)', line=dict(color='rgba(107, 178, 144, 1)', width=1))))
        
        fig_page.update_layout(title = page,
                                xaxis_title = 'Page Miss',
                                yaxis = {'categoryorder': 'total ascending'},
                                paper_bgcolor='rgb(231, 231, 255)',
                                plot_bgcolor='rgb(231, 231, 255)',
                                margin=dict(l=120, r=20, t=80, b=50),
                                width=width, height=height)
        fig_temp.update_layout(title = temp,
                                xaxis_title = 'Tempo de Substituição(ms)',
                                yaxis = {'categoryorder': 'total ascending'},
                                paper_bgcolor = 'rgb(231, 231, 255)',
                                plot_bgcolor = 'rgb(231, 231, 255)',
                                margin=dict(l=120, r=20, t=80, b=50),
                                width = width, height = height)
        
        graph_page = plot.plot({'data': fig_page}, output_type='div')
        graph_temp = plot.plot({'data': fig_temp}, output_type='div')
        graphs[f"{key}"].update({'page': graph_page, 'temp': graph_temp})

    if len(resultado.items()) > 1:
        linha = {}

        for algoritmo in data_nome:
            linha.update({algoritmo : list()})

        for key,items in resultado.items():
            for chave,item in items.items():
                linha[chave].append(item['PageMiss'])

        fig = go.Figure()

        for chave, valores in linha.items():
            fig.add_trace(go.Scatter(x=memo, y=valores, mode='lines+markers', name=chave))

        fig.update_layout(title = 'Page Miss x Tamanho da Memória',
                                xaxis_title = 'Tamanho da Memória (%)',
                                yaxis = {'categoryorder': 'total ascending'},
                                yaxis_title = 'Qtd Page Miss',
                                paper_bgcolor = 'rgb(231, 231, 255)',
                                plot_bgcolor = 'rgb(231, 231, 255)',
                                margin=dict(l=120, r=20, t=80, b=50),
                                width = 2*width, height = 2*height)
        graph_line = plot.plot({'data': fig}, output_type='div')

        resultado.update({'line': graph_line})

    resultado.update({'graphs': graphs})
    return resultado