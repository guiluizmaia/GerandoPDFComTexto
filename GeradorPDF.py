# Importação ultilizada
from fpdf import FPDF

# Chamando a importação em um objeto
pdf = FPDF()

# Função para adicionar uma pagina
pdf.add_page()

# Definindo a fonte ultilizada
pdf.set_font('Arial', 'B', 16)

# Adicionando linhas
pdf.cell(40, 10, 'Hello World!', ln=1)
pdf.cell(40, 10, 'Hello World!', ln=2)

# Salvando o arquivo
pdf.output('tuto1.pdf', 'F')
