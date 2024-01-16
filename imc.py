import tkinter as tk

def calcular_imc():
    # Obter os valores inseridos pelo usuário
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())

    # Calcular o IMC
    imc = peso / (altura ** 2)

    # Atualizar o rótulo com o resultado
    resultado.config(text=f"Seu IMC é: {imc:.2f}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Criar elementos da interface
rotulo_peso = tk.Label(janela, text="Peso (kg):")
entrada_peso = tk.Entry(janela)

rotulo_altura = tk.Label(janela, text="Altura (m):")
entrada_altura = tk.Entry(janela)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)

resultado = tk.Label(janela, text="Seu IMC será exibido aqui.")

# Layout dos elementos
rotulo_peso.grid(row=0, column=0, pady=5)
entrada_peso.grid(row=0, column=1, pady=5)

rotulo_altura.grid(row=1, column=0, pady=5)
entrada_altura.grid(row=1, column=1, pady=5)

botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

resultado.grid(row=3, column=0, columnspan=2)

# Inicialização da janela
janela.mainloop()
