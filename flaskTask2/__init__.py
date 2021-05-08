import shelve

from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    with open('main.html', 'r') as f:
        return f.read()
    return 'Unknown error'

@app.route('/get', methods=['POST'])
def get():
    return [1, 2, 3, 4]

if __name__ == '__main__':
    app.run()