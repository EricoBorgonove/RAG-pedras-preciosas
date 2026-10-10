import json

import numpy as np

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


textos = [
    registro["texto"]
    for registro in base
]


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
)[0]


indices = np.argsort(
    similaridades
)[::-1]


top_k = 3


indices = indices[
    :top_k
]


print()

print(
    "===================================="
)

print(
    "TOP 3 RESULTADOS"
)

print(
    "===================================="
)


for posicao, indice in enumerate(
    indices,
    start=1
):

    registro = base[
        indice
    ]

    score = similaridades[
        indice
    ]

    print()

    print(
        f"RESULTADO {posicao}"
    )

    print(
        "Arquivo:",
        registro["arquivo"]
    )

    print(
        "Chunk:",
        registro["chunk_id"]
    )

    print(
        "Similaridade:",
        round(
            float(score),
            4
        )
    )

    print()

    print(
        registro["texto"]
    )

    print(
        "------------------------------------"
    )
