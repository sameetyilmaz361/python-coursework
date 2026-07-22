from llama_cpp import Llama
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model = Llama (model_path=r"C:\Users\smtty\OneDrive\Belgeler\bme268\slm.gguf",
                n_ctx=512, verbose=False)

response = model.create_chat_completion(
    messages=[{"role": "user", "content": "Explain gravity in simple terms."}],
    max_tokens=256,
)
answer = response["choices"][0]["message"]["content"]
print("AI:", answer)
reason = response["choices"][0]["finish_reason"]
print(f"Finish reason: {reason}")