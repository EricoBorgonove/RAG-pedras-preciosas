# PRÁTICA 01 - RAG e preparação de base de conhecimento para pedras preciosas

## Visão geral
Este projeto foi desenvolvido para construir uma base de conhecimento sobre pedras preciosas a partir de dados estruturados e documentos em PDF. O objetivo é preparar os textos para uso em sistemas de recuperação de informação e busca semântica com IA.

A prática envolve:
- leitura de dados em CSV;
- extração de texto de arquivos PDF;
- limpeza e padronização do conteúdo;
- criação de chunks de texto;
- organização dos dados em um formato pronto para etapas posteriores de embeddings e busca semântica.

## Objetivo
Preparar uma pequena base de conhecimento sobre pedras preciosas para uso posterior em aplicações de RAG (Retrieval-Augmented Generation).

Ao final da prática, o aluno deve ser capaz de:
- diferenciar dados estruturados e não estruturados;
- ler arquivos CSV com Python e Pandas;
- extrair texto de documentos PDF com bibliotecas adequadas;
- limpar e normalizar textos para processamento;
- dividir textos em blocos menores (chunks);
- gerar um conjunto de dados preparado para etapas de embeddings e recuperação semântica.

## Estrutura do projeto

- [base_pedras/](base_pedras/): dados e documentos originais
  - [base_pedras/pedras.csv](base_pedras/pedras.csv): tabela com dados das pedras
  - [base_pedras/observacoes.txt](base_pedras/observacoes.txt): textos complementares
  - [base_pedras/pdfs](base_pedras/pdfs): arquivos em PDF das pedras
- [codigo1/](codigo1/): sequência principal de scripts da prática
- [codigo/](codigo/): versão alternativa/compacta do mesmo fluxo
- [codigo2/](codigo2/): scripts de embeddings e busca semântica
- [codigo3/](codigo3/): scripts de banco vetorial e consulta
- [saida/](saida/): arquivos gerados pela pipeline
- [requirements.txt](requirements.txt): dependências do projeto
- [.gitignore](.gitignore): arquivos ignorados no Git

## Requisitos

Python 3.10+ recomendado.

## Instalação

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

No macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Fluxo de execução
A sequência principal da prática está em [codigo1/](codigo1/). A ordem sugerida é:

```bash
python codigo1/00_gerar_pdfs.py
python codigo1/01_ler_csv.py
python codigo1/02_ler_pdf.py
python codigo1/03_ler_varios_pdfs.py
python codigo1/04_limpar_textos.py
python codigo1/05_criar_chunks.py
python codigo1/06_criar_base.py
```

Também existe uma versão mais compacta em [codigo/](codigo/), com os arquivos:

```bash
python codigo/01_explorar_csv.py
python codigo/02_extrair_pdfs.py
python codigo/03_limpar_texto.py
python codigo/04_criar_chunks.py
python codigo/05_pipeline_completo.py
```

## Resultado esperado
A execução da pipeline gera arquivos processados e organizados em [saida/](saida/), sendo o principal resultado o arquivo de chunks em JSON.

## Dicas de estudo

1. Compare os dados em [base_pedras/pedras.csv](base_pedras/pedras.csv) com o conteúdo dos PDFs.
2. Observe como o texto extraído precisa ser limpo antes de ser usado em IA.
3. Entenda por que um documento grande deve ser dividido em chunks.
4. Pense em como metadados como nome da pedra, fonte, categoria e posição no texto ajudam na recuperação.
5. Reflita sobre a diferença entre busca textual e busca semântica.

## Perguntas para reflexão

1. Qual é a diferença entre o conteúdo da tabela e os documentos PDF?
2. O que acontece quando extraímos texto de um PDF?
3. Por que limpar o texto antes de usar em IA?
4. O que é um chunk e qual a sua função?
5. Por que não processar um documento inteiro como uma única unidade?
6. Qual a importância da sobreposição entre chunks?
7. Quais metadados deveriam acompanhar cada chunk?
8. O que será necessário adicionar para fazer busca por significado?

## Fonte de referência
Material didático com base em informações públicas do Gemological Institute of America (GIA):
https://www.gia.edu/

## Observações
Este projeto é uma base didática para aprender o fluxo básico de preparação de dados para RAG. Em etapas seguintes, o conteúdo gerado será usado para embeddings, armazenamento vetorial e busca por similaridade.
