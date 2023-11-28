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

        print(memorias)
        for mem in memorias:
            random = algoritmos.Random(mem)
            swap.print()
            print(procExec)
            if algExc: 
                while random.RandStep(swap): pass
            else : random.Rand(swap)
            
            random.print()

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