import json

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


with open(
    "saida/chunks.json",
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


embeddings_base = modelo.encode(
    textos
)


pergunta = input(
    "Digite sua pergunta: "
)


embedding_pergunta = modelo.encode(
    [pergunta]
)


similaridades = cosine_similarity(
    embedding_pergunta,
    embeddings_base
)


indice_melhor = (
    similaridades[0].argmax()
)


melhor = base[
    indice_melhor
]


print()

print(
    "===================================="
)

print(
    "RESULTADO MAIS RELEVANTE"
)

print(
    "===================================="
)

print()

print(
    "Arquivo:"
)

print(
    melhor["arquivo"]
)


print()

print(
    "Chunk:"
)

print(
    melhor["chunk_id"]
)


print()

print(
    "Similaridade:"
)

print(
    similaridades[0][indice_melhor]
)


print()

print(
    "Texto:"
)

print(
    melhor["texto"]
)
