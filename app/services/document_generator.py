import os
import uuid
from docxtpl import DocxTemplate
from docx2pdf import convert

class DocumentGenerator:
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def gerar_documento(self, template, dados):
        # Gera nome de arquivo único
        filename = f"documento_{uuid.uuid4()}"
        docx_path = os.path.join(self.output_dir, f"{filename}.docx")
        pdf_path = os.path.join(self.output_dir, f"{filename}.pdf")

        # Carregar template
        doc = DocxTemplate(template)
        
        # Renderizar documento
        doc.render(dados)
        doc.save(docx_path)

        # Converter para PDF
        convert(docx_path, pdf_path)

        return pdf_path

    def listar_documentos(self, usuario_id=None):
        return os.listdir(self.output_dir)
