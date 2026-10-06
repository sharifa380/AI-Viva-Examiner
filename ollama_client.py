import ollama


MODEL_NAME = "llama3.2"


def generate_viva_question(context, difficulty="Medium"):
    """
    Generate one viva question using
    retrieved PDF context.
    """

    prompt = f"""
You are an AI Viva Examiner.

You must create ONE viva question
for an engineering student.

Use the following information retrieved
from the student's study material.

STUDY MATERIAL:
{context}

DIFFICULTY:
{difficulty}

Rules:
1. Ask only ONE question.
2. The question must be based on the study material.
3. Do not give the answer.
4. Do not add explanations.
5. Return only the question.

Generate the viva question now.
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