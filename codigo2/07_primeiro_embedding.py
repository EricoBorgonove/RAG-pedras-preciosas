from sentence_transformers import SentenceTransformer


modelo = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


texto = (
    "O rubi é uma pedra vermelha."
)


embedding = modelo.encode(
    texto
)


print(
    "Embedding:"
)

print(
    embedding
)


print()

print(
    "Quantidade de dimensões:"
)

print(
    len(embedding)
)
