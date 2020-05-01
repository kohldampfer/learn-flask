from flask import Flask
app = Flask("learn-flask")

@app.route("/")
def hello_world():
	return 'Hello, world'

if __name__ == '__main__':
	app.run

