from django.shortcuts import render
from . import classes, algoritmos, util
from math import ceil
from django.http import JsonResponse
import json
from django.core import serializers

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

        saida.update({'grafico': True}) if 'grafico' in dados_do_formulario else saida.update({'grafico': False})
        saida.update({'tabelas': True}) if 'tabelas' in dados_do_formulario else saida.update({'tabelas': False})

        if 'algoritmos' in dados_do_formulario:
            # Pagina Algoritmo
            global algoritmo
            global resultado
            algoritmo = util.PreencherListaAlgoritmo(memorias, alg_exec)
            for mem in memorias:
                resultado.update({f"{mem.X}": {}})
            memAntiga = "<div class='meomria'></div>"
            nome, pageMiss, tempo, pagina, memNova = GenerateDataToAlgoritmo()
            passo = "Começar"
            return render(request, "MMU/algoritmo.html", {'nome': nome, 'pageMiss': pageMiss, 'tempo': tempo, 'memAntiga': memAntiga, 'pagina': pagina, 'memNova': memNova, 'passo': passo})
        else:
            # Página Resultados
            ExecutarAlgoritmos()
            return render(request, "MMU/resultado.html", {'resultado': resultado})

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

def GenerateDataToAlgoritmo():
    nome = algoritmo[0].nome
    
    pageMiss = algoritmo[0].pageMiss
    
    tempo = algoritmo[0].tempo 
    
    if algoritmo[0].currentPage == -1:
        pagina = ""
    else:
        pagina = str(algoritmo[0].currentPage)
    
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
    for page in algoritmo[0].memoria.paginas:
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

def ExecutarAlgoritmos():
    global resultado

    for mem in memorias:
        mem_data = {
            "size": mem.X
        }

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

        resultado.append(mem_data)

def Algoritmos(request):
    global algoritmo
        
    if not algoritmo[0].Step(swap):
        return render(request, "MMU/algoritmo.html", {})
    
    global resultado
    global memorias
    
    resultado[f"{memorias[0].X}"].update({f"{algoritmo[0].nome}": {"PageMiss": algoritmo[0].pageMiss, "TempSubs": algoritmo[0].tempo}})
    algoritmo.pop(0)

    if len(algoritmo) == 0:
        memorias.pop(0)
        
        if len(memorias) == 0:
            return
        
        algoritmo = util.PreencherListaAlgoritmo(memorias, alg_exec)