from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/home")
def hello_worlde():
    return "<p>Hello, Worlde!</p>"
    
    
app.run(host="0.0.0.0", port=5000)