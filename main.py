import jsonManage

import tkinter as tk
from tkinter import filedialog, messagebox

def abrir_arquivo():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal
    tipos_de_arquivo = [("Arquivos JSON", "*.json")]

    # Pede ao usuário para escolher um arquivo JSON
    arquivo_path = filedialog.askopenfilename(filetypes=tipos_de_arquivo)

    # Verifica se o usuário escolheu um arquivo JSON
    if arquivo_path[-4:] != 'json':
        messagebox.showinfo("Error", "Favor selecionar um arquivo json!")
    else:
        dados = jsonManage.abrirJson(arquivo_path)
        teste = jsonManage.verificar_tipo_json(dados)
        if teste == 1:
            print('Carregar Tipo da Memória')
        elif teste == 2:
            print('Carregar Tipos de Processos')
        elif teste == 3:
            print('Carregar o Teste Requisitado')
        else: 
            messagebox.showinfo("Error", "O seu JSON não é válido")

if __name__ == "__main__":
    abrir_arquivo()


