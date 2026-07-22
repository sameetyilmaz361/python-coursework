from llama_cpp import Llama
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model = Llama (model_path=r"C:\Users\smtty\OneDrive\Belgeler\bme268\slm.gguf",
                n_ctx=512, verbose=False)

question = "Tell me a fun fact about the human brain."
for temp in [0.1, 0.7, 1.5]:
    response = model.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": question},
        ],
        max_tokens=100,
        temperature=temp,
    )

    answer = response["choices"][0]["message"]["content"]
    print(f"Temperature {temp}: {answer}\n")
  