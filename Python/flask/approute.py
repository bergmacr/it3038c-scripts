from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def hello():
    #myname ='Cameron Bergman'
    return render_template("flask1.html") 
    # ,value=myName
@app.route("/hello", methods=['POST'])
def hello():
    return render_template("hello.html", myName=request.form['myName'])
