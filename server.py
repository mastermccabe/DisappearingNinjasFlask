from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",)

@app.route('/ninja')
def ninja():
    ninja = True
    return render_template("ninjas.html", ninja=ninja )



@app.route('/ninja/<color>')
def ninja_color(color):
    ninja = False
    return render_template("ninjas.html",color=color, ninja=ninja)

#
# def hello_world():
#     return render_template('index.html')
#
# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
