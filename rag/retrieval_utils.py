def retrieve(query: str, encoder, index, chunks, k=4):
    qv = encoder.encode([query], normalize_embeddings=True)
    scores, idxs = index.search(qv, k)
    return [chunks[i] for i in idxs[0]]
