from django.shortcuts import render
from . import classes, algoritmos, util
from django.http import JsonResponse
import json
from django.http import HttpResponseRedirect
from django.urls import reverse

swap = classes.SWAP()
memorias = []
algoritmo = []
procExec = []
alg_exec = {}
saida = {}
resultado = {}

def home(request):
    return render(request, "MMU/home.html", {})

def executar(request):
    global alg_exec
    global resultado
    global saida
    alg_exec.clear()
    resultado.clear()
    saida.clear()
    if request.method=="POST":
        dados_do_formulario = request.POST

        # Pegando dados gerais dos testes
        if 'todos' in dados_do_formulario:
            alg_exec.update({'rand': True})
            alg_exec.update({'nru': True})
            alg_exec.update({'fifo': True})
            alg_exec.update({'sc': True})
            alg_exec.update({'relogio': True})
            alg_exec.update({'lru': True})
            alg_exec.update({'envelhecimento': True})
        else:
            alg_exec.update({'rand': True}) if 'rand' in dados_do_formulario else alg_exec.update({'rand': False})
            alg_exec.update({'nru': True}) if 'nru' in dados_do_formulario else alg_exec.update({'nru': False})
            alg_exec.update({'fifo': True}) if 'fifo' in dados_do_formulario else alg_exec.update({'fifo': False})
            alg_exec.update({'sc': True}) if 'sc' in dados_do_formulario else alg_exec.update({'sc': False})
            alg_exec.update({'relogio': True}) if 'relogio' in dados_do_formulario else alg_exec.update({'relogio': False})
            alg_exec.update({'lru': True}) if 'lru' in dados_do_formulario else alg_exec.update({'lru': False})
            alg_exec.update({'envelhecimento': True}) if 'envelhecimento' in dados_do_formulario else alg_exec.update({'envelhecimento': False})

        saida.update({'graficos': True}) if 'graficos' in dados_do_formulario else saida.update({'graficos': False})
        saida.update({'tabelas': True}) if 'tabelas' in dados_do_formulario else saida.update({'tabelas': False})

        if 'algoritmos' in dados_do_formulario:
            global algoritmo
            algoritmo = util.PreencherListaAlgoritmo(memorias, alg_exec)
            for mem in memorias:
                resultado.update({f"{mem.X}": {}})
            return HttpResponseRedirect(reverse('PassoAPasso',None))
            
        resultado = util.ExecutarAlgoritmos(memorias,alg_exec,swap,resultado)
    return HttpResponseRedirect(reverse('Resultados',None))

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

def PassoAPasso(request):
    global algoritmo
    global resultado
    global memorias

    memAntiga = util.GenerateMemoryHtml(algoritmo[0])
    if algoritmo[0].Step(swap):
        nome, pageMiss, tempo, pagina, memNova = util.GenerateDataToAlgoritmo(algoritmo[0])
        passo = "Próximo Passo"
        return render(request, "MMU/algoritmo.html", {'nome': nome, 'pageMiss': pageMiss, 'tempo': tempo, 'memAntiga': memAntiga, 'pagina': pagina, 'memNova': memNova, 'passo': passo})
    
    resultado[f"{memorias[0].X}"].update({f"{algoritmo[0].nome}": {"PageMiss": algoritmo[0].pageMiss, "TempSubs": algoritmo[0].tempo}})
    algoritmo.pop(0)

    if len(algoritmo) == 0:
        memorias.pop(0)
        
        if len(memorias) == 0:
            return HttpResponseRedirect(reverse('Resultados',None))

        algoritmo = util.PreencherListaAlgoritmo(memorias, alg_exec)
        
    nome, pageMiss, tempo, pagina, memNova = util.GenerateDataToAlgoritmo(algoritmo[0])
    passo = "Começar Próximo Algoritmo"
    memAntiga = ""
    return render(request, "MMU/algoritmo.html", {'nome': nome, 'pageMiss': pageMiss, 'tempo': tempo, 'memAntiga': memAntiga, 'pagina': pagina, 'memNova': memNova, 'passo': passo})

def Resultados(request):
    global resultado
    resultado = dict(sorted(resultado.items(), key=lambda x: int(x[0])))
    if saida['graficos'] and 'graphs' not in resultado:
        resultado = util.GererateGraphs(resultado)

    return render(request, "MMU/resultado.html", {
        'resultado': resultado,
        'tabela': saida['tabelas'],
        'graficos': saida['graficos'],
        })