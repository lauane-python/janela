import tkinter as tk 
import subprocess

def abrir_janela():
    subprocess.Popen(["python", "nova_janela.py"])

def abrir_contador():
    compu.janela_contador()

janela = tk.Tk()
janela.geometry("600x600")
janela.title("Sistema")
janela.configure(bg = "#9ac0f5")

def sair():
    janela.destroy()


contador = tk.Button(janela, text = "CONTADOR", bg = "#5b89c9", command= abrir_contador, font = ("Times New Romam", 15), width=20)
contador.pack(pady = 30)
btn_jal = tk.Button(janela, text = "Janela ",command=abrir_janela, bg = "#5b89c9", font = ("Times New Romam", 15), width=20)
btn_jal.pack(pady = 30)
sair = tk.Button(janela, text = "Sair", command=sair, bg = "#5b89c9", font = ("Times New Romam", 15), width=20)
sair.pack(pady = 30)

janela.mainloop()
