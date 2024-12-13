import tkinter as tk
from tkinter import messagebox, simpledialog
from contract_generator import ContractGenerator
import os

class ContractApp:
    def __init__(self, master):
        self.master = master
        master.title("Gerador de Contratos")
        master.geometry("400x300")

        self.contract_generator = ContractGenerator()

        # Criar diretório de saída se não existir
        os.makedirs('output', exist_ok=True)

        # Botões
        self.gerar_btn = tk.Button(master, text="Gerar Novo Contrato", command=self.gerar_contrato)
        self.gerar_btn.pack(pady=10)

        self.listar_btn = tk.Button(master, text="Listar Contratos", command=self.listar_contratos)
        self.listar_btn.pack(pady=10)

    def gerar_contrato(self):
        dados = {}
        campos = [
            "Nome do Cliente", 
            "Tipo de Evento", 
            "Data do Evento", 
            "Local", 
            "Valor Total", 
            "Forma de Pagamento"
        ]

        for campo in campos:
            valor = simpledialog.askstring("Entrada", f"Digite {campo}:")
            if valor:
                dados[campo] = valor

        if dados:
            filename = self.contract_generator.generate_contract(dados)
            messagebox.showinfo("Sucesso", f"Contrato gerado: {filename}")

    def listar_contratos(self):
        contratos = self.contract_generator.listar_contratos()
        if contratos:
            messagebox.showinfo("Contratos Gerados", "\n".join(contratos))
        else:
            messagebox.showinfo("Contratos", "Nenhum contrato gerado ainda.")

def main():
    root = tk.Tk()
    app = ContractApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
