from pypdf import PdfReader

arquivo = "base_pedras/pdfs/rubi.pdf"
pdf = PdfReader(arquivo)

print("\nQuantidade de páginas:")
print(len(pdf.pages))

texto = ""

for pagina in pdf.pages:
    conteudo = pagina.extract_text()
    if conteudo:
        texto += conteudo + "\n"

print("\n==============================")
print("TEXTO EXTRAÍDO")
print("==============================\n")
print(texto)
