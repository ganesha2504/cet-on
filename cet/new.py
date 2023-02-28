from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of questions and their answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["New York", "London", "Paris", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Everest", "K2", "Makalu", "Kangchenjunga"],
        "answer": "Everest"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    }
]

# Define a function to display the quiz
@app.route("/")
def quiz():
    return render_template("quiz.html", questions=questions)

# Define a function to grade the quiz
@app.route("/grade", methods=["POST"])
def grade():
    score = 0
    for q in questions:
        if request.form[q["question"]] == q["answer"]:
            score += 1
    return render_template("score.html", score=score)

if __name__ == "__main__":
    app.run()
