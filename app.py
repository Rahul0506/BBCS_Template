from flask import Flask, request,render_template
import random

GREETING_KEYWORDS = ["hello", "hi", "greetings", "yo"]
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*"]

app = Flask(__name__)

def RespondToGreeting(sentence):
    for word in sentence:
        if word.lower() in GREETING_KEYWORDS:
            return GREETING_RESPONSES[random.randint(0,2)]
    return "Sorry, I do not understand you."

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.form["message"].split(" ")
        return render_template("index.html", result=RespondToGreeting(result))
    else: #'GET'
        return render_template("index.html", result=-1)
