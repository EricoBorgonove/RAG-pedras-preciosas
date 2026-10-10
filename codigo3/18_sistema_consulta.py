import chromadb
from sentence_transformers import SentenceTransformer


PASTA_BANCO = "chroma_db"
NOME_COLECAO = "pedras_preciosas"
TOP_K = 3


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


cliente = chromadb.PersistentClient(
    path=PASTA_BANCO
)


colecao = cliente.get_collection(
    name=NOME_COLECAO
)


print()
print("====================================")
print("BASE DE CONHECIMENTO GEMOLÓGICA")
print("====================================")
print()
print(
    "Digite 'sair' para encerrar."
)


while True:

    print()

    pergunta = input(
        "Pergunta: "
    ).strip()


    if pergunta.lower() == "sair":

        print()
        print(
            "Consulta encerrada."
        )

        break


    if not pergunta:

        print(
            "Digite uma pergunta válida."
        )

        continue


    embedding_pergunta = modelo.encode(
        [pergunta]
    ).tolist()


    resultado = colecao.query(
        query_embeddings=embedding_pergunta,
        n_results=TOP_K
    )


    print()
    print(
        "------------------------------------"
    )

    print(
        "Resultados mais próximos:"
    )


    for i in range(
        len(resultado["ids"][0])
    ):

        print()
        print(
            f"{i + 1}º resultado"
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
            round(
                float(
                    resultado["distances"][0][i]
                ),
                4
            )
        )

        print()

        print(
            resultado["documents"][0][i]
        )

        print(
            "------------------------------------"
        )
