import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Variáveis para armazenar os operandos
        self.num1 = tk.DoubleVar()
        self.num2 = tk.DoubleVar()

        # Entradas para os operandos
        self.entry_num1 = tk.Entry(root, textvariable=self.num1)
        self.entry_num2 = tk.Entry(root, textvariable=self.num2)

        # Rótulos e entradas
        tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_num1.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_num2.grid(row=1, column=1, padx=10, pady=10)

        # Botões para operações
        tk.Button(root, text="Adição", command=self.add).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Subtração", command=self.subtract).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Multiplicação", command=self.multiply).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Divisão", command=self.divide).grid(row=5, column=0, columnspan=2, pady=10)

    def add(self):
        result = self.num1.get() + self.num2.get()
        self.show_result(result)

    def subtract(self):
        result = self.num1.get() - self.num2.get()
        self.show_result(result)

    def multiply(self):
        result = self.num1.get() * self.num2.get()
        self.show_result(result)

    def divide(self):
        if self.num2.get() != 0:
            result = self.num1.get() / self.num2.get()
            self.show_result(result)
        else:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")

    def show_result(self, result):
        messagebox.showinfo("Resultado", f"O resultado é: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
