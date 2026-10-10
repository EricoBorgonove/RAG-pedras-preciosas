from pathlib import Path
from pypdf import PdfReader

pasta = Path("base_pedras/pdfs")
arquivos = pasta.glob("*.pdf")

for arquivo in arquivos:
    print("\n==============================")
    print("Arquivo:", arquivo.name)
    print("==============================")

    pdf = PdfReader(arquivo)
    texto = ""

    for pagina in pdf.pages:
        conteudo = pagina.extract_text()
        if conteudo:
            texto += conteudo + "\n"

    print("\n", texto)
