import chromadb
from sentence_transformers import SentenceTransformer


PASTA_BANCO = "chroma_db"
NOME_COLECAO = "pedras_preciosas"


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


cliente = chromadb.PersistentClient(
    path=PASTA_BANCO
)


colecao = cliente.get_collection(
    name=NOME_COLECAO
)


texto = """
A tanzanita é uma variedade azul-violeta
do mineral zoisita.

Foi descoberta na Tanzânia.

Sua dureza fica aproximadamente
entre 6 e 7 na escala de Mohs.
"""


texto = " ".join(
    texto.split()
)


embedding = modelo.encode(
    [texto]
).tolist()


colecao.upsert(
    ids=[
        "tanzanita_0"
    ],
    documents=[
        texto
    ],
    embeddings=embedding,
    metadatas=[
        {
            "arquivo": "tanzanita.txt",
            "chunk_id": 0
        }
    ]
)


print()
print("Novo conhecimento adicionado com sucesso.")
print()
print("ID: tanzanita_0")
print("Arquivo: tanzanita.txt")
print()
print(texto)
