from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quote')
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"content": "Error retrieving quote", "author": ""})


if __name__ == '__main__':
    app.run(debug=True)