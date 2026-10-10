import re
from pathlib import Path
from pypdf import PdfReader

def limpar_texto(texto):
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

def criar_chunks(texto, tamanho=350, sobreposicao=50):
    chunks = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho
        trecho = texto[inicio:fim].strip()

        if trecho:
            chunks.append(trecho)

        inicio += tamanho - sobreposicao

    return chunks

pasta = Path("base_pedras/pdfs")

for arquivo in pasta.glob("*.pdf"):
    pdf = PdfReader(arquivo)
    texto = ""

    for pagina in pdf.pages:
        conteudo = pagina.extract_text()
        if conteudo:
            texto += conteudo + "\n"

    texto = limpar_texto(texto)
    chunks = criar_chunks(texto)

    print("\n==============================")
    print("Arquivo:", arquivo.name)
    print("Chunks:", len(chunks))
    print("==============================")

    for numero, chunk in enumerate(chunks, start=1):
        print(f"\nCHUNK {numero}")
        print("------------------------------")
        print(chunk)
