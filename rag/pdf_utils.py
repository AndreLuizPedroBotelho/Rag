import PyPDF2

def load_pdf(path: str) -> list[str]:
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return split_into_chunks(full_text)

def split_into_chunks(text: str, max_len: int = 500) -> list[str]:
    paragraphs = text.split("\n")
    chunks = []
    chunk = ""
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if len(chunk) + len(p) < max_len:
            chunk += " " + p
        else:
            chunks.append(chunk.strip())
            chunk = p
    if chunk:
        chunks.append(chunk.strip())
    return chunks
