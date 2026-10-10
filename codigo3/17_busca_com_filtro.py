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


arquivo_filtro = input(
    "Digite o arquivo para filtrar "
    "(ex.: rubi.pdf): "
)


embedding_pergunta = modelo.encode(
    [pergunta]
).tolist()


resultado = colecao.query(
    query_embeddings=embedding_pergunta,
    n_results=3,
    where={
        "arquivo": arquivo_filtro
    }
)


print()
print("====================================")
print("RESULTADOS FILTRADOS")
print("====================================")


if not resultado["ids"][0]:

    print()
    print(
        "Nenhum resultado encontrado "
        "para esse filtro."
    )

else:

    for i in range(
        len(resultado["ids"][0])
    ):

        print()
        print(
            f"RESULTADO {i + 1}"
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
