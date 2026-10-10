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


pergunta = input(
    "Digite sua pergunta: "
)


embedding_pergunta = modelo.encode(
    [pergunta]
).tolist()


resultado = colecao.query(
    query_embeddings=embedding_pergunta,
    n_results=3
)


print()
print("====================================")
print("RESULTADOS")
print("====================================")


for i in range(
    len(resultado["ids"][0])
):

    print()
    print(
        f"RESULTADO {i + 1}"
    )

    print(
        "ID:",
        resultado["ids"][0][i]
    )

    print(
        "Arquivo:",
        resultado["metadatas"][0][i]["arquivo"]
    )

    print(
        "Chunk:",
        resultado["metadatas"][0][i]["chunk_id"]
    )

    print(
        "Distância:",
        resultado["distances"][0][i]
    )

    print()
    print(
        resultado["documents"][0][i]
    )

    print(
        "------------------------------------"
    )
