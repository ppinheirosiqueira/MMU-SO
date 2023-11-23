import numpy as np
import random as rd

def Envelhecimento(mem, matriz_paginas, pages):
    pagemiss = 0
    while True:
        page = pages.pop(0)
        x = next((i for i, item in enumerate(mem) if item["page"] == page), None)

        if x == None:
            pagemiss += 1

            soma_linhas = (matriz_paginas.sum(axis=1)).tolist()
            menores_linhas = np.where(soma_linhas == np.min(soma_linhas))[0]
            
            pagina_index = rd.choice(menores_linhas)
            menor_pagina = mem[pagina_index]

            text = f"Removeu: {menor_pagina}"
            menor_pagina.update({"page": page, "R": 0})
            
            matriz_paginas = np.roll(matriz_paginas, shift=-1, axis=1)
            referencias = list(x["R"] for x in mem)
            if len(referencias) < 10:
                for x in range(10-len(referencias)):
                    referencias.append(0)
            referencias = np.array(referencias)
            referencias = referencias[...,None]
            np.flip(referencias, axis=0)
            matriz_paginas[:, 7] = referencias.flatten()
        else:
            mem[x].update({"R": 1})
            text = f"Referenciou: {mem[x]}"
            matriz_paginas = np.roll(matriz_paginas, shift=-1, axis=1)
            referencias = list(x["R"] for x in mem)
            if len(referencias) < 10:
                for x in range(10-len(referencias)):
                    referencias.append(0)
            referencias = np.array(referencias)
            referencias = referencias[...,None]
            np.flip(referencias, axis=0)
            matriz_paginas[:, 7] = referencias.flatten()

        print(f"Pagina passada: {page} --> Aconteceu: {text}")

        if len(pages) == 0:
            break
    
    print(pagemiss)

pages = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,15,13,7,13,5,24,4,14,18,2,18,15,22,24,14,9,17,21,1,9,21,24,17,16,3,8,8,21,15,4,25,18,2,9,23,6,10,13,5,13,4,4,2,16,17,17,11,25,5,13]
mem = list()
matriz_paginas = np.array(np.zeros((10,8)))
i = 0
count = 0

while True:
    count += 1
    num = pages.pop(0)
    x = next((n for n, item in enumerate(mem) if item["page"] == num), None)
    if x == None:
        i += 1
        mem.append({"page": num, "R": 0})
    else:
        mem[x].update({"R": 1})

    if count <= 8:
        referencias = list(x["R"] for x in mem)
        if len(referencias) < 10:
            for x in range(10-len(referencias)):
                referencias.append(0)
        referencias = np.array(referencias)
        referencias = referencias[...,None]
        np.flip(referencias, axis=0)
        matriz_paginas[:, count-1] = referencias.flatten()
    else:
        matriz_paginas = np.roll(matriz_paginas, shift=-1, axis=1)
        referencias = list(x["R"] for x in mem)
        if len(referencias) < 10:
            for x in range(10-len(referencias)):
                referencias.append(0)
        referencias = np.array(referencias)
        referencias = referencias[...,None]
        np.flip(referencias, axis=0)
        matriz_paginas[:, 7] = referencias.flatten()

    if i == 10:
        break

Envelhecimento(mem, matriz_paginas, pages)