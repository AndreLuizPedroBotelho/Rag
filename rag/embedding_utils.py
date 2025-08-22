from sentence_transformers import SentenceTransformer
import faiss

def create_index(chunks: list[str]):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = encoder.encode(
        chunks, show_progress_bar=True, normalize_embeddings=True
    )
    d = embeddings.shape[1]
    index = faiss.IndexFlatIP(d)
    index.add(embeddings)
    return encoder, index, chunks
