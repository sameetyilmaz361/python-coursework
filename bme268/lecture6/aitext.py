from llama_cpp import Llama
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model = Llama (model_path=r"C:\Users\smtty\OneDrive\Belgeler\bme268\slm.gguf",
                n_ctx=512, verbose=False)

with open("c:/Users/smtty/OneDrive/Belgeler/bme268/article.txt", "r") as f:
    text = f.read()

response = model.create_chat_completion(
    messages=[
        {"role": "system", 
         "content": "Summarize the text in 2-3 sentences."},
        {"role": "user", "content": text},
    ],
    max_tokens=256,
)
print("Summary: ")
print(response["choices"][0]["message"]["content"])   