from flask import Flask
app = Flask("learn-flask")

@app.route("/")
def hello_world():
	return 'Hello, world'

app.run(host="0.0.0.0", port="5000")

