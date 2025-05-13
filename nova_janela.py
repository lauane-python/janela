import tkinter  

def fechar_janela():
    janela.destroy()

janela = tkinter.Tk()

janela.configure(bg="#3a1666")

janela.title("Sistema de Cadastro ")

janela.geometry("500x500")

tkinter.Label(janela, text="Informe seu nome: ").pack(pady=5)

tkinter.Entry(janela, bg="#6928b8").pack(pady=5)

tkinter.Checkbutton(janela,text="aceito todos os termos: ").pack(pady=5)

tkinter.Button(janela, text= "fechar", command=fechar_janela, bg="#6928b8").pack(pady=10)

janela.mainloop() 
