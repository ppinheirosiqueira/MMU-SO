from django.shortcuts import render
from . import classes
from random import choice
from math import ceil

def home(request):
    return render(request, "MMU/home.html", {})

def executar(request):
    if request.method=="POST":
        dados_do_formulario = request.POST
        if dados_do_formulario['todos'] == 'on':
            todos = True
        else:
            if dados_do_formulario['envelhecimento'] == 'on':
                envelhecimento = True
            if dados_do_formulario['fifo'] == 'on':
                fifo = True
            if dados_do_formulario['lru'] == 'on':
                lru = True
            if dados_do_formulario['nru'] == 'on':
                nru = True
            if dados_do_formulario['rand'] == 'on':
                rand = True
            if dados_do_formulario['relogio'] == 'on':
                relogio = True
            if dados_do_formulario['sc'] == 'on':
                sc = True
        page = int(dados_do_formulario['page'])
        Y = int(dados_do_formulario['Y'])
        if dados_do_formulario['graficos'] == 'on':
            graficos = True
        if dados_do_formulario['tabelas'] == 'on':
            tabelas = True
        if dados_do_formulario['algoritmos'] == 'on':
            algoritmos = True
        qtdProExe = int(dados_do_formulario['qtdProExe'])
        if dados_do_formulario['lote'] == 'on':
            lote = True
        if dados_do_formulario['aleatorio'] == 'on':
            aleatorio = True
        else:
            listaProcessos = dados_do_formulario['lista']

        vetorQtdPro = []
        vetorTamPro = []
        for chave, valor in dados_do_formulario.items():
            if chave.startswith('qtdPro') and chave[6:].isdigit():
                numero_processo = chave[6:]
                vetorQtdPro.append(valor)
                string = f'tamPro{numero_processo}'
                vetorTamPro.append(dados_do_formulario[string])

        aux = 1
        auxPag = 0
        vetorQtdPro2 = vetorQtdPro.copy()
        vetorTamPro2 = vetorTamPro.copy()
        swap = classes.SWAP()
        while len(vetorQtdPro2) > 0:
            index = choice([*range(0,len(vetorQtdPro2))]) # Sorteia uma tamanho de página aleatória do vetor de processos
            pagFin = auxPag + int(vetorTamPro2[index]) - 1 # A página final é igual a inicial + o tamanho do processo - 1
            # o -1 é necessário, pois imaginando que o processo tenha 5 páginas, comece na 0, somando 5, o processo teria 6 páginas, pois iria da 0 até a 5
            procAux = classes.Processo(auxPag, pagFin) # Criar o processo
            auxPag = pagFin + 1 # a próxima página inicial é uma a mais da ultima do último processo
            swap.addProcesso(f'P{aux}',procAux) # coloco o processo na swap
            aux += 1 # auxiliar só para o nome do processo
            vetorQtdPro2[index] = int(vetorQtdPro2[index]) - 1 # diminuo em 1 a quantidade de processos que estou olhando
            if vetorQtdPro2[index] == 0: # se o primeiro valor estiver zerado, retiro ele, pois não existem mais processos desse tamanho
                vetorQtdPro2.pop(index)
                vetorTamPro2.pop(index)
        swap.attTotal(pagFin + 1) # o total de páginas da swap é igual o valor da pagina final + 1, já q tem a página 0
        
        swap.print()
        
        lote = False # Arrumar formulario
        aleatorio = True # Arrumar formulario
        listaProcessos = 'P1, P2, P3, P4, P5' # Arrumar formulario
        procExec = list()
        if lote and qtdProExe <= swap.qtdProcessos():
            if aleatorio:
                procPoss = [*range(1, swap.qtdProcessos()+1)]
                for i in range(0, qtdProExe):
                    index = choice([*range(0,len(procPoss))])
                    procExec.append(f'P{procPoss[index]}')
                    procPoss.pop(index)
            else:
                listaProcessos = listaProcessos.split(',')
                listaProcessos = [value.strip() for value in listaProcessos]
                if len(listaProcessos) == qtdProExe: 
                    if len(set(listaProcessos)) == len(listaProcessos):
                        for proc in listaProcessos:
                            if int(proc[1:]) > 0 and int(proc[1:]) < swap.qtdProcessos()+1:
                                procExec.append(proc)
                            else:
                                print("Error um Processo na Lista de Processos Não Faz Está na SWAP") # Arrumar depois para mostrar um pop-up na tela
                                break
                    else:
                        print("Error Lote Está Marcado Não Pode Repetir Processos") # Arrumar depois para mostrar um pop-up na tela
                else:
                    print("Error Quantidade de Processos a Serem Executaods é Diferente da Quantidade de Processos na Lista de Processos") # Arrumar depois para mostrar um pop-up na tela
        elif lote and qtdProExe > swap.qtdProcessos():
            print("Error Quantidade de Processos a Serem Executaods Maior que o Número de Processos Na SWAP") # Arrumar depois para mostrar um pop-up na tela
        else:
            if aleatorio:
                procPoss = [*range(1, swap.qtdProcessos()+1)]
                for i in range(0, qtdProExe):
                    index = choice([*range(0,len(procPoss))])
                    procExec.append(f'P{procPoss[index]}')
            else:
                listaProcessos = listaProcessos.split(',')
                listaProcessos = [value.strip() for value in listaProcessos]
                if len(listaProcessos) == qtdProExe:
                    for proc in listaProcessos:
                        if int(proc[1:]) > 0 and int(proc[1:]) < swap.qtdProcessos()+1:
                            procExec.append(proc)
                        else:
                            print("Error um Processo na Lista de Processos Não Faz Está na SWAP") # Arrumar depois para mostrar um pop-up na tela
                            break
                else:
                    print("Error Quantidade de Processos a Serem Executaods é Diferente da Quantidade de Processos na Lista de Processos") # Arrumar depois para mostrar um pop-up na tela
        print(procExec)

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
            memoria.print()

    return render(request, "MMU/home.html", {})

