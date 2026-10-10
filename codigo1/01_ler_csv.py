import pandas as pd

arquivo = "base_pedras/pedras.csv"
dados = pd.read_csv(arquivo)

print("\n==============================")
print("BASE DE PEDRAS")
print("==============================\n")
print(dados)

print("\nQuantidade de pedras:")
print(len(dados))

print("\nColunas disponíveis:")
print(dados.columns.tolist())

print("\nPedras com dureza mínima >= 8")
resultado = dados[dados["mohs_min"] >= 8]
print(resultado[["nome", "mineral", "cor", "mohs_min"]])
