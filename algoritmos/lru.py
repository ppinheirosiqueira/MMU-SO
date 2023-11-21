import numpy as np

def LRU(mem, matriz_paginas, pages):
    pagemiss = 0
    while True:
        page = pages.pop(0)
        x = next((i for i, item in enumerate(mem) if item["page"] == page), None)

        if x == None:
            pagemiss += 1

            soma_linhas = (matriz_paginas.sum(axis=1)).tolist()
            menor_linha = soma_linhas.index(min(soma_linhas))

            menor_pagina = (list(i for i in mem if i["line"] == menor_linha))[0]

            text = f"Removeu: {menor_pagina}"
            menor_pagina.update({"page": page, "R": 0, "line": menor_linha})
            
            matriz_paginas[menor_linha] = np.ones(10)
            matriz_paginas[:,menor_linha] = np.zeros(10)
        else:
            mem[x].update({"R": 1})
            text = f"Referenciou: {mem[x]}"
            matriz_paginas[mem[x]["line"]] = np.ones(10)
            matriz_paginas[:,mem[x]["line"]] = np.zeros(10)

        print(f"Pagina passada: {page} --> Aconteceu: {text}")

        if len(pages) == 0:
            break
    
    print(pagemiss)

pages = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,15,13,7,13,5,24,4,14,18,2,18,15,22,24,14,9,17,21,1,9,21,24,17,16,3,8,8,21,15,4,25,18,2,9,23,6,10,13,5,13,4,4,2,16,17,17,11,25,5,13]
mem = list()
matriz_paginas = np.zeros((10,10))
i = 0

while True:
    num = pages.pop(0)
    x = next((n for n, item in enumerate(mem) if item["page"] == num), None)
    if x == None:
        i += 1
        mem.append({"page": num, "R": 0, "line": i-1})
        matriz_paginas[i-1] = np.ones(10)
        matriz_paginas[:,i-1] = np.zeros(10)
    else:
        mem[x].update({"R": 1})
    if i == 10:
        break

LRU(mem, matriz_paginas, pages)