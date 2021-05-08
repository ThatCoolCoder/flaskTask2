from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return '<button onclick="alert(\'hi\')">Click me!</button>'

if __name__ == '__main__':
    app.run()