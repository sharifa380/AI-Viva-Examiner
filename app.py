import streamlit as st
import chromadb
import ollama
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Viva Examiner",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🎓 AI Viva Examiner")

st.subheader(
    "Full-Stack AI Viva Examination using RAG + Ollama"
)

st.write(
    "Upload your study material PDF, select a viva topic, "
    "generate an AI question, answer it, and receive an AI evaluation."
)


# =========================================================
# LOAD EMBEDDING MODEL
# =========================================================

@st.cache_resource
def load_model():

    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


model = load_model()


# =========================================================
# CHROMADB
# =========================================================

@st.cache_resource
def get_collection():

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="viva_documents"
    )

    return collection


collection = get_collection()


# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_pdf_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# =========================================================
# CREATE CHUNKS
# =========================================================

def create_chunks(text, size=1000):

    chunks = []

    for i in range(0, len(text), size):

        chunk = text[i:i + size]

        if chunk.strip():

            chunks.append(chunk)

    return chunks


# =========================================================
# PROCESS PDF
# =========================================================

def process_pdf(pdf_file):

    text = extract_pdf_text(pdf_file)

    if not text.strip():

        return 0

    chunks = create_chunks(text)

    embeddings = model.encode(
        chunks
    ).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    # Clear old data
    try:

        old = collection.get()

        if old["ids"]:

            collection.delete(
                ids=old["ids"]
            )

    except Exception:

        pass

    collection.add(

        ids=ids,

        documents=chunks,

        embeddings=embeddings
    )

    return len(chunks)


# =========================================================
# RETRIEVE CONTEXT
# =========================================================

def retrieve_context(question):

    question_embedding = model.encode(
        [question]
    ).tolist()

    results = collection.query(

        query_embeddings=question_embedding,

        n_results=4
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return "\n\n".join(documents)


# =========================================================
# OLLAMA
# =========================================================

def ask_ollama(prompt):

    response = ollama.chat(

        model="llama3.2",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# =========================================================
# GENERATE VIVA QUESTION
# =========================================================

def generate_question(context, topic):

    prompt = f"""
You are an AI viva examiner.

Use ONLY the study material provided below.

STUDY MATERIAL:
{context}

TOPIC:
{topic}

Generate ONE clear technical viva question.

The question should be suitable for a B.Tech student.

Do not give the answer.

Return only the question.
"""

    return ask_ollama(prompt)


# =========================================================
# EVALUATE ANSWER
# =========================================================

def evaluate_answer(
    question,
    answer,
    context
):

    prompt = f"""
You are an AI viva examiner.

Evaluate the student's answer using the study material.

STUDY MATERIAL:
{context}

VIVA QUESTION:
{question}

STUDENT ANSWER:
{answer}

Evaluate the answer.

Use this format:

SCORE: X/10

CORRECTNESS:
Explain whether the answer is correct.

FEEDBACK:
Give useful suggestions.

MODEL ANSWER:
Give the correct answer briefly.

Keep the response easy to understand.
"""

    return ask_ollama(prompt)


# =========================================================
# SESSION STATE
# =========================================================

if "question" not in st.session_state:

    st.session_state.question = ""


if "context" not in st.session_state:

    st.session_state.context = ""


if "evaluation" not in st.session_state:

    st.session_state.evaluation = ""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Viva Settings")

    topic = st.text_input(
        "Viva Topic",
        placeholder="Example: RAG"
    )

    st.markdown("---")

    st.write("### Technologies")

    st.write("🐍 Python")
    st.write("🖥️ Streamlit")
    st.write("🧠 Ollama")
    st.write("🔎 Sentence Transformers")
    st.write("🗄️ ChromaDB")
    st.write("📄 PyPDF")


# =========================================================
# PDF UPLOAD
# =========================================================

st.header("📚 Step 1: Upload Study Material")

pdf_file = st.file_uploader(
    "Upload your AI notes PDF",
    type=["pdf"]
)


if pdf_file:

    if st.button(
        "📥 Process PDF",
        type="primary"
    ):

        with st.spinner(
            "Processing PDF..."
        ):

            try:

                number = process_pdf(
                    pdf_file
                )

                st.success(
                    f"PDF processed successfully! "
                    f"{number} chunks created."
                )

            except Exception as e:

                st.error(
                    f"Error processing PDF: {e}"
                )


# =========================================================
# GENERATE QUESTION
# =========================================================

st.header("🎤 Step 2: Generate Viva Question")


if st.button(
    "🤖 Generate Viva Question",
    type="primary"
):

    if not pdf_file:

        st.warning(
            "Please upload and process a PDF first."
        )

    elif not topic:

        st.warning(
            "Please enter a viva topic in the sidebar."
        )

    else:

        with st.spinner(
            "AI is generating your viva question..."
        ):

            try:

                context = retrieve_context(
                    topic
                )

                question = generate_question(
                    context,
                    topic
                )

                st.session_state.context = context

                st.session_state.question = question

                st.session_state.evaluation = ""

            except Exception as e:

                st.error(
                    f"Error generating question: {e}"
                )


# =========================================================
# DISPLAY QUESTION
# =========================================================

if st.session_state.question:

    st.success(
        "Viva question generated!"
    )

    st.markdown("### 📝 Viva Question")

    st.info(
        st.session_state.question
    )


# =========================================================
# STUDENT ANSWER
# =========================================================

if st.session_state.question:

    st.header("✍️ Step 3: Your Answer")

    answer = st.text_area(
        "Enter your answer below:",
        height=180,
        placeholder="Type your viva answer here..."
    )


    # =====================================================
    # EVALUATE
    # =====================================================

    if st.button(
        "📊 Evaluate My Answer",
        type="primary"
    ):

        if not answer.strip():

            st.warning(
                "Please enter your answer first."
            )

        else:

            with st.spinner(
                "AI is evaluating your answer..."
            ):

                try:

                    result = evaluate_answer(

                        st.session_state.question,

                        answer,

                        st.session_state.context
                    )

                    st.session_state.evaluation = result

                except Exception as e:

                    st.error(
                        f"Evaluation error: {e}"
                    )


# =========================================================
# DISPLAY EVALUATION
# =========================================================

if st.session_state.evaluation:

    st.header("📊 Step 4: AI Evaluation")

    st.markdown(
        st.session_state.evaluation
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 AI Viva Examiner | Full-Stack AI Project | RAG + Ollama"
)