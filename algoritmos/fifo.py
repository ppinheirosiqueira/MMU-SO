def FIFO(mem, pages):
    pagemiss = 0
    while True:
        page = pages.pop(0)
        x = next((i for i, item in enumerate(mem) if item["page"] == page), None)

        if x == None:
            pagemiss += 1
            element = mem.pop(0)
            text = f"Removeu: {element}"
            mem.append({"page": page, "R": 0})
        else:
            mem[x].update({"R": 1})
            text = f"Referenciou: {mem[x]}"

        print(f"Pagina passada: {page} --> Aconteceu: {text}")

        if len(pages) == 0:
            break
    
    print(pagemiss)

pages = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,15,13,7,13,5,24,4,14,18,2,18,15,22,24,14,9,17,21,1,9,21,24,17,16,3,8,8,21,15,4,25,18,2,9,23,6,10,13,5,13,4,4,2,16,17,17,11,25,5,13]
mem = list()
i = 0

while True:
    num = pages.pop(0)
    x = next((i for i, item in enumerate(mem) if item["page"] == num), None)
    if x == None:
        i += 1
        mem.append({"page": num, "R": 0})
    else:
        mem[x].update({"R": 1})
    if i == 10:
        break

FIFO(mem, pages)
