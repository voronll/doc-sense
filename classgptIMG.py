import fitz  # PyMuPDF para manipulação de PDFs
import camelot  # Para extração de tabelas
import pdfplumber  # Alternativa para extração de tabelas
import os

# Função para extrair imagens do PDF
def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for i, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = os.path.join(output_folder, f"page_{page_num + 1}_img_{i + 1}.png")

            with open(image_filename, "wb") as img_file:
                img_file.write(image_bytes)
            print(f"Imagem salva: {image_filename}")

    doc.close()

# Função para extrair tabelas do PDF usando Camelot
def extract_tables_from_pdf(pdf_path, output_folder):
    tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")  # Ou "lattice" para arquivos bem formatados
    os.makedirs(output_folder, exist_ok=True)

    for i, table in enumerate(tables):
        table.to_csv(os.path.join(output_folder, f"table_{i + 1}.csv"))
        print(f"Tabela salva: table_{i + 1}.csv")

# Caminho do PDF e pasta de saída
pdf_path = "pdfOriginais/PPC.pdf"
output_folder = "pdfIMG"

# Extrair imagens e tabelas
extract_images_from_pdf(pdf_path, os.path.join(output_folder, "images"))
extract_tables_from_pdf(pdf_path, os.path.join(output_folder, "tables"))