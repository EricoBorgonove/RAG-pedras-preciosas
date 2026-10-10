import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


ARQUIVO_CHUNKS = Path("saida/chunks.json")
PASTA_BANCO = "chroma_db"
NOME_COLECAO = "pedras_preciosas"


with open(
    ARQUIVO_CHUNKS,
    "r",
    encoding="utf-8"
) as f:

    base = json.load(f)


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


cliente = chromadb.PersistentClient(
    path=PASTA_BANCO
)


try:
    cliente.delete_collection(
        name=NOME_COLECAO
    )
except Exception:
    pass


colecao = cliente.create_collection(
    name=NOME_COLECAO
)


documentos = []
ids = []
metadados = []


for registro in base:

    arquivo = registro["arquivo"]
    chunk_id = registro["chunk_id"]
    texto = registro["texto"]

    documentos.append(
        texto
    )

    ids.append(
        f"{arquivo}_{chunk_id}"
    )

    metadados.append(
        {
            "arquivo": arquivo,
            "chunk_id": int(chunk_id)
        }
    )


embeddings = modelo.encode(
    documentos
).tolist()


colecao.add(
    ids=ids,
    documents=documentos,
    embeddings=embeddings,
    metadatas=metadados
)


print()
print("====================================")
print("BANCO VETORIAL CRIADO")
print("====================================")
print()
print("Coleção:", NOME_COLECAO)
print("Documentos inseridos:", len(documentos))
print("Pasta do banco:", PASTA_BANCO)
