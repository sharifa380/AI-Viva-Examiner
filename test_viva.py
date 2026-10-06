from rag_engine import retrieve_context
from ollama_client import generate_viva_question


print("AI VIVA EXAMINER")
print("================")
print()


# Get topic from user
topic = input(
    "Enter viva topic: "
)


# Retrieve information from PDF
print("\nSearching PDF...")


context = retrieve_context(
    topic,
    top_k=5
)


if not context:

    print("No relevant information found.")

else:

    print("Relevant information found!")

    print("\nGenerating viva question...")


    question = generate_viva_question(
        context,
        difficulty="Medium"
    )


    print()
    print("==============================")
    print("       VIVA QUESTION")
    print("==============================")
    print()

    print(question)