def chunk_text(t: str, max_len: int = 512, overlap: int = 64):
    words = t.split()
    i = 0
    while i < len(words):
        j = min(len(words), i + max_len)
        yield " ".join(words[i:j])
        i = j - overlap
        if i < 0:
            i = 0