from flask import Flask, request, render_template, url_for, redirect
from chatbot import ChatBot
import sqlite3
import random

GREETING_KEYWORDS = ["hello", "hi", "greetings", "yo"]
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*"]

app = Flask(__name__)

#Function to load database
def get_db():
    db = sqlite3.connect('chatbot.sqlite3')
    print('Opened database successfully')
    db.row_factory = sqlite3.Row
    return db

#Creating database table (1st run only)
def create_db():
    db = get_db()
    #previous chats table
    db.execute('CREATE TABLE chats (id INTEGER PRIMARY KEY AUTOINCREMENT, ' +\
               'chat VARCHAR(255))')
    db.close()

#create a fresh database 1st run only
#create_db()

#LOAD CHATBOT
chatbot = ChatBot()

#Index (home) page
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

####################################
## Approach taken here is to load all the chats from a database and display them before
## asking for a new input. I understand this is quite inefficient. However, I am
## unfortunately not proficient in javascript which would make displaying their
## response by just adding to a current messaage board much easier
## PLS HALP IF YOU GUD IN JS
###################################

#Chat page
@app.route('/chat/')
def chat():
    #Load all the chats till now
    db = get_db()
    chats = db.execute('SELECT * FROM chats').fetchall()
    db.close()

    return render_template('chat.html', chats=chats)

#Recording input and output
@app.route('/record/', methods=['POST'])
def record():
    chat_in = request.form['input']

    #Somehow handle the output. Using default now
    chat_out = chatbot.handle_message(chat_in)

    #Add to database
    db = get_db()
    db.execute('INSERT INTO chats (chat) VALUES (?)', (chat_in,))

    #Maybe for added functionality with responses?
    if type(chat_out) == str:
        db.execute('INSERT INTO chats (chat) VALUES (?)', (chat_out,))
    else:
        raise NotImplementedError
    
    db.commit()
    db.close()

    #Go back to chatting page
    return redirect(url_for('chat'))

#Running the app on local server port 5000
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
