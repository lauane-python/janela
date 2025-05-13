import tkinter as tk 
import subprocess
import compu

def abrir_calculadora():
    subprocess.Popen(["python", "calculadora.py"])

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
btn_calc = tk.Button(janela, text = "CALCULADORA",command=abrir_calculadora, bg = "#5b89c9", font = ("Times New Romam", 15), width=20)
btn_calc.pack(pady = 30)
sair = tk.Button(janela, text = "SAIR", command=sair, bg = "#5b89c9", font = ("Times New Romam", 15), width=20)
sair.pack(pady = 30)

janela.mainloop()
