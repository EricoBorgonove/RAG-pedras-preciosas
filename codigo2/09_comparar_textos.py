from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


texto_1 = (
    "O rubi possui coloração vermelha."
)


texto_2 = (
    "Quero uma pedra de cor vermelha."
)


embedding_1 = modelo.encode(
    [texto_1]
)


embedding_2 = modelo.encode(
    [texto_2]
)


similaridade = cosine_similarity(
    embedding_1,
    embedding_2
)


print(
    "Texto 1:"
)

print(
    texto_1
)


print()

print(
    "Texto 2:"
)

print(
    texto_2
)


print()

print(
    "Similaridade:"
)

print(
    similaridade[0][0]
)
