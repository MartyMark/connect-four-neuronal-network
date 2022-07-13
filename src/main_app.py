from flask import Flask
from flask import request
from flask import jsonify

from src.train_command import train

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    response = {
        'response': board
    }
    return jsonify(response)


train()

"""
if __name__ == "__main__":
    get('http://api.open-notify.org/iss-pass.json', {'lat': '45', 'lon': '180'})

    post('https://httpbin.org/post', data={'key': 'value'})

    #put('https://httpbin.org/put', data={'key': 'value'})"""
