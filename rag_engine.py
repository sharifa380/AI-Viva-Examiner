import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader


# ==========================================
# 1. Load Sentence Transformer Model
# ==========================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==========================================
# 2. Create ChromaDB
# ==========================================

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="viva_documents"
)


# ==========================================
# 3. Extract Text From PDF
# ==========================================

def extract_pdf_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ==========================================
# 4. Split Text Into Chunks
# ==========================================

def create_chunks(text, chunk_size=1000):

    chunks = []

    text = text.strip()

    for start in range(
        0,
        len(text),
        chunk_size
    ):

        chunk = text[
            start:start + chunk_size
        ]

        if chunk.strip():

            chunks.append(
                chunk.strip()
            )

    return chunks


# ==========================================
# 5. Process PDF
# ==========================================

def process_pdf(pdf_file):

    # Extract PDF text
    text = extract_pdf_text(pdf_file)

    if not text.strip():

        return 0

    # Create chunks
    chunks = create_chunks(text)

    # Delete old documents
    try:

        collection.delete(
            where={
                "source": "uploaded_pdf"
            }
        )

    except Exception:

        pass

    # Convert chunks into embeddings
    embeddings = embedding_model.encode(
        chunks
    ).tolist()

    # Create unique IDs
    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    # Metadata
    metadata = [
        {
            "source": "uploaded_pdf",
            "chunk_number": i
        }
        for i in range(len(chunks))
    ]

    # Store in ChromaDB
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata
    )

    return len(chunks)


# ==========================================
# 6. Retrieve Relevant Information
# ==========================================

def retrieve_context(
    query,
    top_k=5
):

    # Convert query into embedding
    query_embedding = embedding_model.encode(
        [query]
    ).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    documents = results.get(
        "documents",
        []
    )

    if not documents:

        return ""

    if not documents[0]:

        return ""

    # Combine retrieved chunks
    context = "\n\n".join(
        documents[0]
    )

    return context