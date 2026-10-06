import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Hello, are you working?"
        }
    ]
)

print(response["message"]["content"])