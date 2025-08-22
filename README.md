# Projeto RAG

Este projeto utiliza Recuperação Aumentada por Geração (RAG) para responder perguntas com base em PDFs, usando embeddings, FAISS e Ollama.

## Estrutura Recomendada

```
Rag/
    rag/
        __init__.py
        pdf_utils.py
        embedding_utils.py
        retrieval_utils.py
        ollama_utils.py
        rag_pipeline.py
    meu_arquivo.pdf
    index.py
    requirements.txt
    Makefile
```

## Como rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script principal:
   ```bash
   python index.py
   ```
