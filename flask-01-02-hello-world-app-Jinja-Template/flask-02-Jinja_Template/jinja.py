from flask import Flask, render_template

# app = Flask(__name__, template_folder="/")
# app = Flask(__name__, template_folder="/") DEFAULT FOLDER IS TEMPLATES UNDER FLASK-02
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name = "Elyes", lastname = "Ferjani")

# SUM INT 10 50 > 60
@app.route("/calc/<int:x>/<int:y>")
def calc(x, y):
    print(x, y)
    return render_template("body.html", x=x, y=y, sum = x + y)



# CONCATINATION 10 50 > 1050
# @app.route("/calc/<x>/<y>")

# @app.route("/calc/<x>/<y>")
# def calc(x, y):
#     print(x, y)
#     return render_template("body.html", x=x, y=y, sum = x + y)

# SUM OF CONVERTED STR 10 50 > 60
# @app.route("/calc/<x>/<y>")
# def calc(x, y):
#     print(x, y)
#     return render_template("body.html", x=x, y=y, sum = int(x) + int(y))



# IF WE DO NOT SET THE NEXT LINE IT WILL RUN FOREVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)