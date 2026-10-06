from rag_engine import retrieve_context
from ollama_client import generate_viva_question
from evaluate import evaluate_answer


print()
print("===================================")
print("       AI VIVA EXAMINER")
print("===================================")
print()


topic = input("Enter viva topic: ")


print()
print("Searching study material...")

context = retrieve_context(
    topic,
    top_k=5
)

if not context:
    print("No relevant information found.")
    exit()


print("Study material found.")
print()
print("Generating viva question...")


question = generate_viva_question(
    context,
    difficulty="Medium"
)


print()
print("===================================")
print("          VIVA QUESTION")
print("===================================")
print()

print(question)

print()
print("-----------------------------------")
print()

answer = input("Enter your answer: ")


print()
print("Evaluating your answer...")
print()


result = evaluate_answer(
    question,
    answer,
    context
)


print("===================================")
print("          AI EVALUATION")
print("===================================")
print()

print(result)

print()
print("===================================")