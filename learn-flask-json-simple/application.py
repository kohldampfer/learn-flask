from flask import Flask, request, jsonify

app = Flask("learn-flask-json")

@app.route("/echo", methods = ['POST'] )
def echo():
    content = request.json
    return content['message']
    
app.run(host="0.0.0.0", port=5000, debug=True)