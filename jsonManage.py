import json

def abrirJson(caminho):
    f = open(caminho)

    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    # print(data['qtd_pag'])
    # print(data['tam_pag'])
    # for i in data['list_pag']:
    #     print(i)

    # Closing file
    f.close()

    return data

def verificar_tipo_json(arquivo):
    chaves = list(arquivo.keys())

    if "tam_pag" in chaves or "X" in chaves or "Y" in chaves:
        return 1
    elif "qtd_pag" in chaves or "qtd_pro" in chaves:
        return 2
    elif "pro_test" in chaves or "alg_test" in chaves or "lote" in chaves or "res_fin" in chaves:
        return 3
