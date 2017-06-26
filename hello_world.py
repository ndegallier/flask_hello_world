from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Aww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/")
@app.route("/jedi/<name>/<last_name>")
def jedi(name, last_name):
        
    jedi_name = last_name.title()[:3] + name.title().lower()[:2]
        
    html = """
            <h1> Hello {}!
            </h1>
            <p> Your jedi name is {}.
            </p>
        """
    return html.format(name.title() + " " + last_name.title(), jedi_name.title())

    
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))