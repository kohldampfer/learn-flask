from flask import Flask, session, redirect, request, render_template
from flask_session import Session
import random
import os
import json

app = Flask("learn-flask-guess-game")
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = os.urandom(24)
# Session(app)

def getRandomNumber():
    number = random.randint(1, 100)
    session['rand_number'] = number
    print("Random number is {0}".format(session.get('rand_number')))

@app.route("/guess", methods = ['POST'])
def guess():
    content = request.json
    number = int(content['number'])
    
    session_number = session.get('rand_number')
    
    print("User send number {0}".format(number))
    print("Session number is {0}".format(session_number))
    
    if number > 100 or number < 0:
        return "There is only a number between 0 and 100 in my mind."
    
    if number == session_number:
        getRandomNumber()
        return "You guessed the number. I have a new number in my mind."
    
    if number > session_number:
        return "Your guess is too high."
    
    if number < session_number:
        return "Your guess is too low."

@app.route("/")
def index():
    if not session.get('rand_number'):
        getRandomNumber()
    return render_template("game.html")

app.run(host="0.0.0.0", port="5000")

