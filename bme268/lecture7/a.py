import os
from llama_cpp import Llama

script_dir = os.path.dirname(os.path.abspath(__file__))
model = Llama (model_path=r"C:\Users\smtty\OneDrive\Belgeler\bme268\slm.gguf",
                n_ctx=512, verbose=False)

while True:
    question = input("You: ").strip()

    if question.lower() == "q":
        print("Goodbye!")
        break
    elif len(question) == 0:
        print("Please enter a question.")
        continue
    elif len(question) > 200:
        print("Too long! Max 200 characters.")
        continue

    response = model.create_chat_completion(
        messages=[
            {"role": "user", "content": question}
        ],
        max_tokens=256
    )   
    print("AI:", response["choices"][0]["message"]["content"])