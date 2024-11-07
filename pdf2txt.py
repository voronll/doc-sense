import pdfplumber
import sys

# Verifica se os argumentos foram passados corretamente
if len(sys.argv) != 3:
    print("Uso: python pdf2txt.py <arquivo_entrada.pdf> <arquivo_saida.txt>")
    sys.exit(1)

# Recebe os argumentos da linha de comando
pdf_path = sys.argv[1]
output_txt_path = sys.argv[2]

# Abre o arquivo PDF e extrai o texto
with pdfplumber.open(pdf_path) as pdf:
    text_content = ""
    for page in pdf.pages:
        text_content += page.extract_text() + "\n"

# Salva o texto extraído em um arquivo .txt
with open(output_txt_path, "w") as text_file:
    text_file.write(text_content)

print(f"O conteúdo do PDF foi salvo em {output_txt_path}")
