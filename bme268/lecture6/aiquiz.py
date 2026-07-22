from llama_cpp import Llama
import os

script_dir = os.path.dirname(os.path.abspath(__file__))     
model = Llama (model_path=r"C:\Users\smtty\OneDrive\Belgeler\bme268\slm.gguf",
                n_ctx=512, verbose=False)


topic = input("Enter a topic for the quiz: ")

response = model.create_chat_completion(
    messages=[
        {"role": "system", 
         "content": "Generate a quiz with 1 question and 4 options ( A, B, C, D). Include the correct answer at the end."},
        {"role" : "user", "content" : topic},
    ],
    max_tokens=512,
    temperature=0.7,
)

quiz_text = response["choices"][0]["message"]["content"]
print(quiz_text)

user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()

for line in quiz_text.split("\n"):
    if "Answer:" in line:
        correct = line.split("Answer:")[-1].strip()[0].upper()
        break

if user_answer == correct:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {correct}.")
