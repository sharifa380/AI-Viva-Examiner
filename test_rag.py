from rag_engine import (
    process_pdf,
    retrieve_context
)


pdf_path = input(
    "Enter the path of your PDF: "
)


with open(
    pdf_path,
    "rb"
) as pdf_file:

    chunks = process_pdf(
        pdf_file
    )


print(
    "\nPDF processed successfully!"
)

print(
    "Number of chunks:",
    chunks
)


query = input(
    "\nEnter your question: "
)


context = retrieve_context(
    query
)


print(
    "\n========== RETRIEVED CONTEXT ==========\n"
)

print(context)