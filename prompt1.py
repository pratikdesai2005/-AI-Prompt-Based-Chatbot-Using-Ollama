import ollama

prompt = input("Enter your prompt: ")

try:
    completion = ollama.chat(
        model="qwen3.5:0.8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False,
        options={
            "temperature": 0,
            "num_predict": 256
        }
    )

    answer = completion.message.content.strip()
    print("\nAI:", answer)

except Exception as e:
    print("Error:", e)