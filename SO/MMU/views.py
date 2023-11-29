from django.shortcuts import render
from . import classes, algoritmos, util
from math import ceil
from django.http import JsonResponse
import json

swap = classes.SWAP()
memorias = []
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
            if 'rand' in dados_do_formulario:
                rand = True
            else:
                rand = False
            if 'nru' in dados_do_formulario:
                nru = True
            else:
                nru = False
            if 'fifo' in dados_do_formulario:
                fifo = True
            else:
                fifo = False
            if 'sc' in dados_do_formulario:
                sc = True
            else:
                sc = False
            if 'relogio' in dados_do_formulario:
                relogio = True
            else:
                relogio = False
            if 'lru' in dados_do_formulario:
                lru = True
            else:
                lru = False
            if 'envelhecimento' in dados_do_formulario:
                envelhecimento = True
            else:
                envelhecimento = False

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

        swap.print()
        print(memorias)
        print(procExec)
        for mem in memorias:
            if todos or rand:
                rand_algo = algoritmos.Random(mem)
                if algExc: 
                    while rand_algo.RandStep(swap): pass
                else : rand_algo.Rand(swap)
                rand_algo.print()

            if todos or nru:
                nru_algo = algoritmos.NRU(mem)
                if algExc: 
                    while nru_algo.NRUStep(swap): pass
                else : nru_algo.NRU(swap)
                nru_algo.print()

            if todos or fifo:
                fifo_algo = algoritmos.FIFO(mem)
                if algExc: 
                    while fifo_algo.FIFOStep(swap): pass
                else : fifo_algo.FIFO(swap)
                fifo_algo.print()

            if todos or sc:
                sc_algo = algoritmos.SC(mem)
                if algExc: 
                    while sc_algo.SCStep(swap): pass
                else : sc_algo.SC(swap)
                sc_algo.print()

            if todos or relogio:
                relogio_algo = algoritmos.Relogio(mem)
                if algExc: 
                    while relogio_algo.RelogioStep(swap): pass
                else : relogio_algo.Relogio(swap)
                relogio_algo.print()
            
            if todos or lru:
                lru_algo = algoritmos.LRU(mem)
                if algExc: 
                    while lru_algo.LRUStep(swap): pass
                else : lru_algo.LRU(swap)
                lru_algo.print()

            if todos or envelhecimento:
                envelhecimento_algo = algoritmos.Envelhecimento(mem)
                if algExc: 
                    while envelhecimento_algo.EnvelhecimentoStep(swap): pass    
                else : envelhecimento_algo.Envelhecimento(swap)
                envelhecimento_algo.print()

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

def criarMemorias(request, vetorX, Y, pageSize, swapAle):
    global memorias
    memorias, mensagem = classes.criandoMemorias(swap, procExec, json.loads(vetorX), Y, pageSize, swapAle)
    data = {'status': mensagem}
    return JsonResponse(data)