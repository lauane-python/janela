import tkinter as tk
from tkinter import messagebox

# Cores simples para feedback visual
COR_PADRAO = "#f0f0f0"
COR_HOVER = "#c0c0c0"

# Função de ação do botão
def acao_botao():
    messagebox.showinfo("Mensagem", "Você clicou no botão.")

# Função para criar uma nova janela
def criar_janela():
    janela = tk.Toplevel(root)
    janela.title("Janela Secundária")
    janela.geometry("300x200")
    janela.resizable(True, True)  # RF4

    # Título
    label_titulo = tk.Label(janela, text="Janela Secundária", font=("Arial", 12))
    label_titulo.pack(pady=10)

    # Botão interativo com feedback visual simples (RF2 e RF6)
    botao_acao = tk.Button(janela, text="Clique Aqui", command=acao_botao)
    botao_acao.pack(pady=10)

    # Feedback visual ao passar o mouse
    botao_acao.bind("<Enter>", lambda e: botao_acao.config(bg=COR_HOVER))
    botao_acao.bind("<Leave>", lambda e: botao_acao.config(bg=COR_PADRAO))

    # Botão de fechar a janela (RF3)
    
    btn_fechar = tk.Button(janela, text="X", command=janela.destroy, bg="red", fg="white")
    btn_fechar.place(x=270, y=5, width=25, height=25)

# Janela principal (root)
root = tk.Tk()
root.title("RetroTech System")
root.geometry("400x300")
root.resizable(True, True)

# Texto de instrução
instrucao = tk.Label(root, text="Clique para abrir novas janelas", font=("Arial", 12))
instrucao.pack(pady=20)

# Botão para criar novas janelas (RF1)
btn_nova_janela = tk.Button(root, text="Nova Janela", command=criar_janela)
btn_nova_janela.pack(pady=10)

# Feedback visual simples no botão principal (RF6)
btn_nova_janela.bind("<Enter>", lambda e: btn_nova_janela.config(bg=COR_HOVER))
btn_nova_janela.bind("<Leave>", lambda e: btn_nova_janela.config(bg=COR_PADRAO))

# Inicia o sistema
root.mainloop()
