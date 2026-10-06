import ollama


MODEL_NAME = "llama3.2"


def evaluate_answer(question, answer, context):

    prompt = f"""
You are an AI Viva Examiner.

Evaluate the student's answer using the study material.

STUDY MATERIAL:
{context}

QUESTION:
{question}

STUDENT ANSWER:
{answer}

Give the evaluation in this exact format:

Score: X/10
Correctness: ...
Feedback: ...
Expected Answer: ...

Rules:
- Score from 0 to 10.
- Give 10 for an excellent and complete answer.
- Give 7-9 for a mostly correct answer.
- Give 4-6 for a partially correct answer.
- Give 1-3 for a mostly incorrect answer.
- Give 0 if there is no relevant answer.
- Be fair and concise.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()