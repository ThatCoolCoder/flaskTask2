import json
import os.path

from flask import Flask, jsonify, request
app = Flask(__name__)

# The cwd starts off as / for some reason, so make the message file name absolute
CONTAINING_DIR = os.path.dirname(os.path.realpath(__file__))
MESSAGE_FILE_NAME = os.path.join(CONTAINING_DIR, 'messages.json')

def load_messages():
    if os.path.exists(MESSAGE_FILE_NAME):
        f = open(MESSAGE_FILE_NAME, 'r')
        messages = json.loads(f.read())
        f.close()
        return messages
    else:
        return []

def save_messages(messages):
    f = open(MESSAGE_FILE_NAME, 'w+')
    f.write(json.dumps(messages))
    f.close()

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
    return jsonify(load_messages())

@app.route('/send/', methods=['POST'])
def send():
    messages = load_messages()
    messages.append({'sender' : request.json['sender'], 'content' : request.json['content']})
    save_messages(messages)
    return ''

if __name__ == '__main__':
    app.run()