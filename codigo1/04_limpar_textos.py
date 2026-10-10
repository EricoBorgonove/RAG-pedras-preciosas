import re
from pathlib import Path
from pypdf import PdfReader

def limpar_texto(texto):
    texto = re.sub(r"\s+", " ", texto)
    texto = texto.strip()
    return texto

pasta = Path("base_pedras/pdfs")
arquivos = pasta.glob("*.pdf")

for arquivo in arquivos:
    pdf = PdfReader(arquivo)
    texto = ""

    for pagina in pdf.pages:
        conteudo = pagina.extract_text()
        if conteudo:
            texto += conteudo + "\n"

    texto_limpo = limpar_texto(texto)

    print("\n==============================")
    print(arquivo.name)
    print("==============================\n")
    print(texto_limpo)
