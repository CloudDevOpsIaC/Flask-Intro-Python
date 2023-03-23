# MODULE IN PYTHON IS A FILE
# Flask is a function 
from flask import Flask
# __name__ IS A RUNTIME VARIABLE, A SPECIAL ONE
app = Flask(__name__)

# ROUTE DECORATOR
# example.com/
# DECORATOR @app.route("/")
@app.route("/")
def home():
    return "Hello world 1"

@app.route('/support')
def support():
    return "<h1 style='color: red'>Support Team email is support@example.com</h1>"

@app.route("/profile/<username>")
def profile(username):
    return f"Welcom {username}"

@app.route('/calculate/<int:x>/<int:y>')
def calculate(x,y):
    return f'Sum of {x} and {y} is {x + y}'

if __name__ =="__main__":
    app.run(host="0.0.0.0", port = 3000, debug = False)


