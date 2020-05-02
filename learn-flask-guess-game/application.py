from flask import Flask, session, redirect, request, render_template
import random

app = Flask("learn-flask-guess-game")

def getRandomNumber():
    number = random.randint(1, 100)
    session['rand_number'] = number

@app.route("/guess", methods = ['POST'])
def guess():
    content = request.json
    number = int(content['number'])
    
    if number > 100 or number < 0:
        return "There is only a number between 0 and 100 in my mind."
    
    if number == session['rand_number']:
        getRandomNumber()
        return "You guessed the number. I have a new number in my mind."
    
    if number > session['rand_number']:
        return "Your guess is too high."
    
    if number < session['rand_number']:
        return "Your guess is too low."

@app.route("/")
def index():
    return render_template("templates/game.html")

app.run(host="0.0.0.0", port="5000")

