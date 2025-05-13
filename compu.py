import tkinter as tk

def janela_contador():

    def aumentar():
        valor_atual = int(rotulo["text"])
        novo_valor = valor_atual +1
        rotulo.config(text=novo_valor)

    def diminuir():
        valor_atual = int(rotulo["text"])
        novo_valor = valor_atual -1
        rotulo.config(text=novo_valor)

    def zerar():
        valor_atual = int(rotulo["text"])
        novo_valor = valor_atual = 0
        rotulo.config(text=novo_valor)


    janela = tk.Tk()
    janela.title("Contador ")
    janela.geometry("500x500")
    janela.configure(bg="#016b68")


    rotulo = tk.Label(janela, bg="pink", text="   0   ",
    font=("times new roman",40))
    rotulo.pack(pady=100, padx=150)#016b68

    frame_boto = tk.Frame(janela)
    frame_boto.pack(side="left", pady=10)

    boto_aumentar = tk.Button(frame_boto, bg= "#016b68", text="adicionar +", command=aumentar, width=10).pack(side="left", pady=10)
    boto_subtrair = tk.Button(frame_boto, bg= "#5bc9c6", text="subtrair -", command=diminuir).pack(side="left", pady=10)
    boto_zerar = tk.Button(frame_boto, bg= "#5bc9c6", text="zerar", command=zerar).pack(side="left", pady=10)
    
    
# janela.mainloop()