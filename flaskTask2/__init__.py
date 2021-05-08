from flask import Flask, jsonify, request
app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def homepage():
    data = 'Error: Unknown error'
    f = None
    try:
        f = app.open_resource('main.html', 'r')
        data = f.read()
    except Exception as e:
        data = 'Error reading file: ' + str(e)
    finally:
        if f is not None:
            f.close()
        return data
    

@app.route('/get/', methods=['POST'])
def get():
    return jsonify(messages)

@app.route('/send/', methods=['POST'])
def send():
    messages.append({'sender' : request.json['sender'], 'content' : request.json['content']})
    return ''

if __name__ == '__main__':
    app.run()