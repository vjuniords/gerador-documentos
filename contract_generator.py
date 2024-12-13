from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

class ContractGenerator:
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir

    def generate_contract(self, dados):
        # Gera nome de arquivo único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/contrato_{timestamp}.pdf"

        # Cria o PDF
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Configurações de fonte e layout
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height - inch, "CONTRATO DE EVENTOS")

        # Detalhes do contrato
        c.setFont("Helvetica", 12)
        y = height - 2*inch
        for key, value in dados.items():
            c.drawString(inch, y, f"{key}: {value}")
            y -= 20

        # Rodapé
        c.setFont("Helvetica", 10)
        c.drawString(inch, inch, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

        c.save()
        return filename

    def listar_contratos(self):
        import os
        return os.listdir(self.output_dir)
