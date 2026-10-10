# PRÁTICA 01 - PROCESSAMENTO DE DOCUMENTOS COM PYTHON

## Tema
PDFs, documentos e textos estruturados.

## Objetivo
Preparar uma pequena base de conhecimento sobre pedras preciosas para uso posterior em IA.

Ao final, o aluno deverá ser capaz de:
- diferenciar dados estruturados e não estruturados;
- ler CSV com Pandas;
- extrair texto de PDF com PyPDF;
- realizar limpeza básica;
- dividir textos em chunks;
- gerar um arquivo JSON preparado para a próxima prática de embeddings.

## Instalação

Windows:
python -m venv .venv
.venv\Scripts\activate

macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

## Ordem
python codigo/01_explorar_csv.py
python codigo/02_extrair_pdfs.py
python codigo/03_limpar_texto.py
python codigo/04_criar_chunks.py
python codigo/05_pipeline_completo.py

## Resultado final
saida/chunks.json

## Questões
1. Qual é a diferença entre o conteúdo de pedras.csv e dos PDFs?
2. O que acontece quando extraímos texto de um PDF?
3. Por que limpar o texto antes de utilizá-lo em IA?
4. O que é um chunk?
5. Por que não transformar um documento grande em um único bloco?
6. Qual a função da sobreposição entre chunks?
7. Quais metadados deveriam acompanhar cada chunk?
8. O que precisaremos acrescentar para realizar busca por significado?

## Fonte
Material didático resumido com base em páginas públicas do Gemological Institute of America (GIA):
https://www.gia.edu/
