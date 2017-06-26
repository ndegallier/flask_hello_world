from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('base.html')

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello.html', name=name)

@app.route("/jedi/<name>/<last_name>")
def jedi(name, last_name):
    
    jedi_name = last_name.title()[:3] + name.title().lower()[:2]
    
    return render_template('jedi.html', name=name, last_name=last_name, jedi_name=jedi_name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)