from flask import Flask, render_template

#WSGI - it is an intermediate server between backend and frontend
app = Flask(__name__)

@app.route('/', methods = ['GET', 'Post'])
def welcome():
    return "Welcome to Praxis"

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to Praxis {your_name}"

if __name__ == '__main__':

    app.run(debug = True, host = '0.0.0.0', port = 3400)

