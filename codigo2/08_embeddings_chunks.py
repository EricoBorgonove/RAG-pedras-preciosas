import json

from sentence_transformers import SentenceTransformer


arquivo = "saida/chunks.json"


with open(
    arquivo,
    "r",
    encoding="utf-8"
) as f:

    base = json.load(
        f
    )


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


textos = []


for registro in base:

    textos.append(
        registro["texto"]
    )


embeddings = modelo.encode(
    textos
)


print(
    "Quantidade de chunks:"
)

print(
    len(base)
)


print()

print(
    "Quantidade de embeddings:"
)

print(
    len(embeddings)
)


print()

print(
    "Dimensões de cada embedding:"
)

print(
    len(embeddings[0])
)
