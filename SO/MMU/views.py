from django.shortcuts import render
from . import classes, algoritmos, util
from math import ceil
from django.http import JsonResponse
import json

swap = classes.SWAP()
procExec = []

def home(request):
    return render(request, "MMU/home.html", {})

def executar(request):
    if request.method=="POST":
        dados_do_formulario = request.POST

        # Pegando dados gerais dos testes
        if 'todos' in dados_do_formulario:
            todos = True
        else:
            todos = False
            if 'envelhecimento' in dados_do_formulario:
                envelhecimento = True
            else:
                envelhecimento = False
            if 'fifo' in dados_do_formulario:
                fifo = True
            else:
                fifo = False
            if 'lru' in dados_do_formulario:
                lru = True
            else:
                lru = False
            if 'nru' in dados_do_formulario:
                nru = True
            else:
                nru = False
            if 'rand' in dados_do_formulario:
                rand = True
            else:
                rand = False
            if 'relogio' in dados_do_formulario:
                relogio = True
            else:
                relogio = False
            if 'sc' in dados_do_formulario:
                sc = True
            else:
                sc = False
        if 'grafico' in dados_do_formulario:
            grafico = True
        else:
            grafico = False
        if 'tabelas' in dados_do_formulario:
            tabelas = True
        else:
            tabelas = False
        if 'algoritmos' in dados_do_formulario:
            algExc = True
        else:
            algExc = False

        # Pegando dados que formam a memória
        page = int(dados_do_formulario['page'])
        Y = int(dados_do_formulario['Y'])

        # Pegando valores de X
        vetorX = []
        for chave, valor in dados_do_formulario.items():
            if chave.startswith('X') and chave[1:].isdigit():
                vetorX.append(int(dados_do_formulario[f'X{chave[1:]}']))

        for X in vetorX:
            qtdPags = 0
            for proc in swap.processos:
                qtdPags += swap.processos[proc].qtdPag
            qtdPags = round(qtdPags * (X/100))

            memoria = classes.Memoria((Y/100), page, qtdPags)

            inicias = list()
            finais = list()
            for proc in procExec:
                processo = swap.findProcesso(proc)
                qtdPagProc = ceil(processo.qtdPag * memoria.Y)
                if len(memoria.paginas) + qtdPagProc <= memoria.tamanho:
                    for i in range(0,qtdPagProc):
                        memoria.addPagina({'page': processo.pagIni + i, 'R': 0, 'processo': proc})
                    inicias.append(proc)
                else:
                    finais.append(proc)
            memoria.addListaExec(inicias + finais)

            random = classes.Algoritmo('Random', memoria)
            print(swap.print())
            print(procExec)
            algoritmos.Rand(random, swap)
            print(f"Algoritmo: {random.nome}, PageMiss: {random.pageMiss}, Tempo de Subistituição: {random.tempo}s")
            

    return render(request, "MMU/home.html", {})

def criarSwap(request, vetor_qtd_pro, vetor_tam_pro):
    global swap
    swap, mensagem = classes.criandoSWAP(swap, json.loads(vetor_qtd_pro),json.loads(vetor_tam_pro))
    data = {'status': mensagem}
    return JsonResponse(data)

def criarListaProcessos(request, aleatorio, lote, qtdProExe, listaProcessos):
    global procExec
    procExec, mensagem = util.criarListaProcessos(aleatorio, lote, qtdProExe, swap, json.loads(listaProcessos))
    data = {'status': mensagem}
    return JsonResponse(data)
