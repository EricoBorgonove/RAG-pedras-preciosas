# RAG para pedras preciosas

Projeto de estudo para construir uma base de conhecimento sobre pedras preciosas e preparar esse conteúdo para uso em aplicações de RAG (Retrieval-Augmented Generation).

## Visão geral
Este repositório demonstra um pipeline completo de processamento de documentos para dados em formato tabular e textual. O objetivo principal é transformar informações dispersas em conteúdo estruturado, limpo e segmentado, pronto para ser usado em buscas semânticas, embeddings e recuperação de contexto em aplicações de IA.

A prática combina:
- leitura de dados em CSV;
- extração de texto de PDFs;
- limpeza e padronização textual;
- separação em chunks;
- preparação da base para etapas posteriores de busca vetorial e geração de respostas.

## Objetivo do projeto
Construir uma pequena base de conhecimento sobre pedras preciosas a partir de fontes diversas, permitindo explorar o fluxo básico de preparação de dados para sistemas de IA orientados a recuperação de informação.

Ao final da prática, o objetivo é que o aluno consiga:
- diferenciar dados estruturados e não estruturados;
- ler dados tabulares com Python e Pandas;
- realizar extração de texto em PDF;
- aplicar limpeza e normalização de textos;
- dividir documentos em blocos menores para melhor recuperação;
- organizar os dados em um formato funcional para embeddings e busca semântica.

## Estrutura do repositório

- [base_pedras](base_pedras): dados e documentos originais
  - [base_pedras/pedras.csv](base_pedras/pedras.csv): tabela principal com informações das pedras
  - [base_pedras/observacoes.txt](base_pedras/observacoes.txt): observações complementares
  - [base_pedras/pdfs](base_pedras/pdfs): arquivos PDF das gemas
- [codigo1](codigo1): sequência principal da prática, organizada em etapas didáticas
- [codigo](codigo): versão alternativa e mais compacta do fluxo
- [codigo2](codigo2): scripts para embeddings e busca semântica
- [codigo3](codigo3): scripts para criação e uso de banco vetorial
- [saida](saida): arquivos gerados pela pipeline
- [requirements.txt](requirements.txt): dependências do projeto
- [.gitignore](.gitignore): regras de exclusão do Git
- [README.md](README.md): documentação do repositório

## Requisitos

- Python 3.10 ou superior
- Ambiente virtual recomendado
- Bibliotecas listadas em [requirements.txt](requirements.txt)

## Configuração do ambiente

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Fluxo principal de execução
A sequência principal da prática está em [codigo1](codigo1). Para executar a pipeline em ordem:

```bash
python codigo1/00_gerar_pdfs.py
python codigo1/01_ler_csv.py
python codigo1/02_ler_pdf.py
python codigo1/03_ler_varios_pdfs.py
python codigo1/04_limpar_textos.py
python codigo1/05_criar_chunks.py
python codigo1/06_criar_base.py
```

Também há uma versão mais compacta em [codigo](codigo):

```bash
python codigo/01_explorar_csv.py
python codigo/02_extrair_pdfs.py
python codigo/03_limpar_texto.py
python codigo/04_criar_chunks.py
python codigo/05_pipeline_completo.py
```

## Resultado esperado
Ao concluir a pipeline, o projeto produz dados processados e organizados em [saida](saida), incluindo arquivos em JSON e textos preparados para uso em etapas posteriores de embeddings e recuperação semântica.

## Conceitos abordados

- Dados estruturados vs. não estruturados
- Extração de texto de documentos PDF
- Limpeza e padronização de textos
- Chunking de documentos
- Base de conhecimento para RAG
- Busca textual e busca semântica
- Metadados e contexto para recuperação de informações

## Perguntas para reflexão

1. Qual é a diferença entre os dados presentes em [base_pedras/pedras.csv](base_pedras/pedras.csv) e os textos presentes nos PDFs?
2. O que acontece quando o texto de um PDF é extraído para o ambiente Python?
3. Por que é importante limpar e normalizar o texto antes de usá-lo em IA?
4. O que representa um chunk e por que ele é útil?
5. Por que não processar um documento inteiro como um único bloco?
6. Qual a função da sobreposição entre chunks?
7. Quais metadados devem acompanhar cada chunk?
8. O que será necessário acrescentar para realizar busca por significado?

## Dicas de estudo

1. Compare a tabela de cadastro das pedras com os textos extraídos dos PDFs.
2. Observe as diferenças entre conteúdo bruto e conteúdo útil para processamento.
3. Reflita sobre a importância do chunking na recuperação de contexto relevante.
4. Entenda como metadados ajudam a conectar texto, categoria, fonte e contexto.
5. Considere como a busca semântica melhora a experiência em comparação com consultas textuais simples.

## Referência
Material didático desenvolvido com base em informações públicas do Gemological Institute of America (GIA):
https://www.gia.edu/

## Observações finais
Este projeto foi pensado como uma base didática para introduzir o fluxo de preparação de dados para aplicações de RAG. A partir desse ponto, o conteúdo gerado pode ser utilizado em etapas seguintes de embedding, armazenamento vetorial, busca por similaridade e geração contextualizada de respostas.
