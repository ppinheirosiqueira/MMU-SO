import numpy as np
import random as rd
rd.seed(2023)

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
            if len(referencias) < size:
                for x in range(size-len(referencias)):
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
            if len(referencias) < size:
                for x in range(size-len(referencias)):
                    referencias.append(0)
            referencias = np.array(referencias)
            referencias = referencias[...,None]
            np.flip(referencias, axis=0)
            matriz_paginas[:, 7] = referencias.flatten()

        print(f"Pagina passada: {page} --> Aconteceu: {text}")

        if len(pages) == 0:
            break
    
    print(pagemiss)

pages = [66, 88, 87, 79, 9, 52, 91, 67, 63, 29, 85, 42, 77, 19, 92, 46, 92, 66, 54, 92, 39, 53, 36, 98, 57, 80, 96, 78, 91, 24, 7, 44, 67, 93, 41, 87, 7, 94, 36, 81, 67, 52, 96, 72, 61, 69, 24, 3, 9, 19, 35, 83, 91, 77, 50, 36, 21, 86, 14, 99, 6, 99, 5, 60, 53, 85, 17, 48, 33, 3, 42, 93, 60, 1, 79, 31, 34, 38, 12, 55, 51, 92, 62, 73, 81, 25, 41, 32, 5, 73, 46, 30, 31, 73, 74, 70, 57, 76, 2, 6, 2, 58, 43, 8, 4, 25, 30, 29, 75, 34, 44, 84, 4, 69, 100, 37, 90, 91, 34, 98, 12, 61, 33, 71, 3, 44, 25, 38, 45, 86, 72, 12, 35, 19, 53, 9, 31, 69, 38, 33, 2, 52, 55, 4, 35, 41, 84, 5, 16, 63, 43, 24, 7, 45, 85, 6, 72, 50, 69, 47, 23, 7, 65, 89, 35, 84, 50, 98, 68, 56, 80, 80, 39, 13, 1, 56, 3, 17, 53, 69, 5, 72, 57, 28, 14, 18, 10, 72, 27, 62, 90, 83, 87, 14, 71, 71, 8, 58, 88, 79, 10, 63, 32, 19, 37, 50, 64, 12, 29, 16, 42, 41, 100, 73, 41, 5, 94, 9, 67, 39, 13, 19, 71, 74, 97, 96, 16, 30, 82, 69, 64, 26, 57, 86, 43, 16, 96, 62, 84, 52, 18, 32, 2, 51, 61, 46, 76, 81, 9, 23, 98, 19, 18, 63, 83, 11, 94, 9, 56, 35, 44, 1, 57, 70, 72, 50, 50, 6, 62, 59, 29, 2, 93, 78, 72, 12, 81, 66, 74, 95, 76, 35, 58, 44, 15, 5, 20, 35, 62, 95, 89, 94, 80, 9, 50, 58, 69, 1, 6, 21, 93, 30, 8, 76, 28, 83, 32, 47, 42, 83, 20, 97, 54, 41, 85, 65, 2, 71, 61, 66, 68, 31, 38, 49, 83, 27, 45, 16, 29, 37, 20, 70, 20, 83, 45, 95, 97, 61, 93, 10, 75, 96, 55, 67, 11, 45, 26, 4, 25, 78, 49, 24, 63, 48, 100, 42, 30, 68, 62, 99, 97, 33, 98, 85, 40, 100, 88, 17, 88, 10, 68, 16, 39, 45, 78, 88, 87, 45, 89, 27, 77, 51, 32, 5, 70, 12, 4, 98, 92, 78, 25, 28, 68, 38, 76, 19, 18, 4, 85, 38, 34, 81, 99, 98, 18, 72, 99, 93, 15, 87, 56, 61, 73, 41, 52, 57, 91, 47, 55, 60, 95, 36, 10, 94, 16, 34, 54, 19, 57, 65, 56, 62, 64, 85, 76, 93, 86, 27, 42, 60, 2, 100, 12, 74, 4, 62, 20, 4, 90, 3, 32, 92, 19, 36, 78, 27, 26, 57, 56, 100, 82, 39, 10, 95, 58, 72, 12, 96, 72, 38, 17, 21, 46, 34, 23, 3, 40, 20, 49, 56, 61, 2, 97, 1, 96, 70, 2, 75, 50, 35, 38, 89, 62, 37, 46, 5, 39, 78, 85, 57, 11, 30, 78, 67, 51, 56, 92, 46, 76, 33, 46, 16, 15, 90, 82, 2, 73, 63, 4, 13, 69, 70, 62, 92, 62, 22, 50, 13, 95, 60, 11, 73, 39, 77, 71, 86, 63, 12, 78, 79, 91, 49, 63, 47, 23, 77, 69, 57, 40, 59, 48, 23, 60, 5, 34, 4, 75, 32, 72, 40, 37, 73, 32, 59, 71, 29, 28, 48, 7, 24, 93, 95, 38, 85, 39, 55, 12, 42, 9, 26, 24, 90, 35, 88, 88, 40, 87, 66, 98, 99, 48, 13, 66, 93, 41, 14, 86, 1, 11, 16, 43, 87, 79, 20, 78, 79, 27, 58, 43, 7, 53, 5, 96, 2, 28, 3, 61, 50, 75, 36, 7, 97, 31, 22, 47, 42, 88, 67, 52, 7, 20, 91, 79, 98, 65, 98, 46, 32, 90, 49, 60, 45, 29, 8, 29, 84, 30, 91, 73, 15, 30, 1, 54, 18, 86, 1, 12, 57, 82, 49, 54, 35, 82, 78, 61, 98, 22, 68, 54, 51, 60, 5, 36, 63, 88, 61, 37, 49, 51, 67, 35, 61, 47, 17, 94, 3, 71, 2, 21, 83, 9, 71, 17, 24, 90, 41, 42, 50, 88, 40, 12, 80, 56, 2, 36, 27, 94, 70, 99, 1, 14, 56, 12, 54, 33, 73, 56, 61, 99, 86, 90, 62, 46, 23, 83, 14, 53, 85, 56, 25, 61, 51, 97, 17, 89, 91, 31, 58, 8, 87, 36, 74, 11, 91, 78, 68, 41, 42, 61, 2, 28, 35, 65, 79, 41, 90, 80, 73, 21, 11, 1, 76, 9, 25, 15, 24, 88, 14, 31, 9, 12, 58, 49, 59, 56, 1, 46, 79, 75, 86, 5, 63, 76, 91, 64, 67, 8, 81, 9, 45, 67, 97, 81, 14, 84, 63, 5, 37, 43, 58, 12, 43, 10, 20, 86, 80, 2, 70, 31, 14, 9, 64, 94, 83, 99, 3, 15, 74, 81, 47, 75, 70, 95, 75, 91, 86, 63, 43, 68, 35, 29, 41, 9, 78, 20, 41, 54, 25, 50, 20, 92, 29, 87, 29, 30, 5, 75, 30, 45, 64, 22, 37, 67, 82, 61, 74, 19, 43, 12, 62, 80, 13, 76, 63, 64, 54, 57, 42, 24, 72, 36, 82, 85, 68, 4, 1, 20, 75, 56, 48, 1, 18, 21, 40, 27, 98, 49, 36, 12, 7, 38, 27, 87, 53, 6, 35, 63, 94, 87, 10, 78, 24, 42, 86, 57, 68, 48, 3, 71, 1, 70, 70, 91, 2, 79, 60, 67, 8, 27, 62, 30, 25, 38, 64, 24, 73, 19, 65, 19, 13, 38, 2, 12, 26, 23, 84, 72, 38, 60, 72, 40, 19, 86, 21, 54, 39, 82, 30, 98, 83, 84, 97, 30, 43, 60, 70, 15, 90, 68, 81, 85, 86, 14, 23, 10, 3, 87, 84, 9, 27, 51, 12, 72, 17, 45, 67, 62, 8, 92, 25, 77, 2, 20, 85, 43, 18, 100, 19, 52, 8, 34, 100, 1, 36, 63, 67, 93, 10, 46, 10]
mem = list()
size = int(100 * (rd.choice([10,20,30,40,50])/100))
matriz_paginas = np.array(np.zeros((size,8)))
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
        if len(referencias) < size:
            for x in range(size-len(referencias)):
                referencias.append(0)
        referencias = np.array(referencias)
        referencias = referencias[...,None]
        np.flip(referencias, axis=0)
        matriz_paginas[:, count-1] = referencias.flatten()
    else:
        matriz_paginas = np.roll(matriz_paginas, shift=-1, axis=1)
        referencias = list(x["R"] for x in mem)
        if len(referencias) < size:
            for x in range(size-len(referencias)):
                referencias.append(0)
        referencias = np.array(referencias)
        referencias = referencias[...,None]
        np.flip(referencias, axis=0)
        matriz_paginas[:, 7] = referencias.flatten()

    if i == size:
        break

Envelhecimento(mem, matriz_paginas, pages)