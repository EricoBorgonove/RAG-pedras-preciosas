import json
import re
from pathlib import Path
from pypdf import PdfReader

def extrair_texto_pdf(arquivo):
    pdf = PdfReader(arquivo)
    texto = ""

    for pagina in pdf.pages:
        conteudo = pagina.extract_text()
        if conteudo:
            texto += conteudo + "\n"

    return texto

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
base_conhecimento = []

for arquivo in pasta.glob("*.pdf"):
    print("Processando:", arquivo.name)

    texto = extrair_texto_pdf(arquivo)
    texto = limpar_texto(texto)
    chunks = criar_chunks(texto)

    for indice, chunk in enumerate(chunks):
        registro = {
            "arquivo": arquivo.name,
            "chunk_id": indice,
            "texto": chunk
        }
        base_conhecimento.append(registro)

pasta_saida = Path("saida")
pasta_saida.mkdir(exist_ok=True)
arquivo_saida = pasta_saida / "chunks.json"

conteudo_json = json.dumps(
    base_conhecimento,
    ensure_ascii=False,
    indent=4
)

arquivo_saida.write_text(
    conteudo_json,
    encoding="utf-8"
)

print("\n====================================")
print("BASE CRIADA COM SUCESSO")
print("====================================\n")
print("Quantidade de chunks:", len(base_conhecimento))
print("\nArquivo criado:")
print(arquivo_saida)
