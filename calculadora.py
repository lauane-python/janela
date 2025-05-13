import tkinter as tk
def somar():
    num1 = float(primeiro_num.get())
    num2 = float(segun_num.get())
    resultado = num1 + num2
    exibe_resultado.config(text=f"Resultado da SOMA: {resultado}")
def menos():
    num1 = float(primeiro_num.get())
    num2 = float(segun_num.get())
    resultado = num1 - num2
    exibe_resultado.config(text=f"Resultado da subtração: {resultado}")
def dividir():
    num1 = float(primeiro_num.get())
    num2 = float(segun_num.get())
    resultado = num1 % num2
    exibe_resultado.config(text=f"Resultado da divisão: {resultado}")
def multiplicar():
    num1 = float(primeiro_num.get())
    num2 = float(segun_num.get())
    resultado = num1 * num2
    exibe_resultado.config(text=f"Resultado da multiplicação: {resultado}")
janela = tk.Tk()
janela.geometry("500x500")
janela.title("Calculadora")
janela.configure(bg="#016b68")

primeiro_num = tk.Label(janela, text="Digite um primeiro valor: ", bg= "#5bc9c6",  font= ("times new roman", 10))
primeiro_num.pack(pady=5)
primeiro_num = tk.Entry(janela,bg="#5bc9c6", font=("times new roman", 10))
primeiro_num.pack(pady=5)


segun_num = tk.Label(janela , bg= "#5bc9c6", text= "Digite um segundo valor: ", font=("times new roman", 10))
segun_num.pack(pady=5)
segun_num = tk.Entry(janela,bg="#5bc9c6", font=("times new roman",10))
segun_num.pack(pady=10)


frame_boto = tk.Frame(janela)
frame_boto.pack(pady=10)

boto_aumentar = tk.Button(frame_boto, bg= "#5bc9c6", text="Adicionar +", command= somar, width=10).pack(side="left", pady=10)
boto_subtrair = tk.Button(frame_boto, bg= "#5bc9c6", text="subtrair -", command=menos).pack(side="left", pady=10)
boto_dividir = tk.Button(frame_boto, bg= "#5bc9c6", text="dividir", command=dividir).pack(side="left", pady=10)
boto_multi = tk.Button(frame_boto, bg= "#5bc9c6", text="multiplicar", command=multiplicar).pack(side="left", pady=10)

exibe_resultado = tk.Label(frame_boto, text = "resultado: ")
exibe_resultado.pack(side="left", pady=10) 

janela.mainloop()