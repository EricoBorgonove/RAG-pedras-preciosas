import chromadb


PASTA_BANCO = "chroma_db"
NOME_COLECAO = "pedras_preciosas"


cliente = chromadb.PersistentClient(
    path=PASTA_BANCO
)


colecao = cliente.get_collection(
    name=NOME_COLECAO
)


quantidade = colecao.count()


print()
print("====================================")
print("INFORMAÇÕES DA COLEÇÃO")
print("====================================")
print()
print("Nome:", NOME_COLECAO)
print("Quantidade de registros:", quantidade)


dados = colecao.get()


print()
print("====================================")
print("REGISTROS")
print("====================================")


for i in range(
    len(dados["ids"])
):

    print()
    print("ID:", dados["ids"][i])

    if dados.get("metadatas"):
        print(
            "Metadados:",
            dados["metadatas"][i]
        )

    if dados.get("documents"):
        print(
            "Texto:",
            dados["documents"][i]
        )

    print(
        "------------------------------------"
    )
