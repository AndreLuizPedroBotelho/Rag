from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from yaspin import yaspin
from rag.pdf_utils import load_pdf
from rag.embedding_utils import create_index
from rag.rag_pipeline import answer

OLLAMA_URL = "http://localhost:11434"
MODEL = "mistral"


# 7. Executar
if __name__ == "__main__":
    print("🔍 Lendo PDF e criando índice...")
    pdf_chunks = load_pdf("meu_arquivo.pdf")
    encoder, index, chunks = create_index(pdf_chunks)

    while True:
        q = input("\n❓ Pergunta (q para sair): ")
        if q.lower().startswith("q"):
            break
        answer(q, encoder, index, chunks)
