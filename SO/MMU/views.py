from django.shortcuts import render
from . import classes

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
        page = dados_do_formulario['page']
        X = dados_do_formulario['X']
        Y = dados_do_formulario['Y']
        if dados_do_formulario['graficos'] == 'on':
            graficos = True
        if dados_do_formulario['tabelas'] == 'on':
            tabelas = True
        if dados_do_formulario['algoritmos'] == 'on':
            algoritmos = True
        qtdProExe = dados_do_formulario['qtdProExe']
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
            pagFin = auxPag + int(vetorTamPro2[0]) - 1 # A página final é igual a inicial + o tamanho do processo - 1
            # o -1 é necessário, pois imaginando que o processo tenha 5 páginas, comece na 0, somando 5, o processo teria 6 páginas, pois iria da 0 até a 5
            procAux = classes.Processo(auxPag, pagFin) # Criar o processo
            auxPag = pagFin + 1 # a próxima página inicial é uma a mais da ultima do último processo
            swap.addProcesso(f'P{aux}',procAux) # coloco o processo na swap
            aux += 1 # auxiliar só para o nome do processo
            vetorQtdPro2[0] = int(vetorQtdPro2[0]) - 1 # diminuo em 1 a quantidade de processos que estou olhando
            if vetorQtdPro2[0] == 0: # se o primeiro valor estiver zerado, retiro ele, pois não existem mais processos desse tamanho
                vetorQtdPro2.pop(0)
                vetorTamPro2.pop(0)
        swap.attTotal(pagFin + 1) # o total de páginas da swap é igual o valor da pagina final + 1, já q tem a página 0
        print(pagFin)
        swap.print()

    return render(request, "MMU/home.html", {})

