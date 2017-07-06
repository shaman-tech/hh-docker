from flask import Flask, send_file, render_template


import json
import urllib.request

app = Flask(__name__)

@app.route('/Greetings')
def bless_up():
    return 'Bless up'

@app.route('/')
def main():
    return send_file('./static/index.html')

@app.route('/result')
def render_site():
    #_json = urllib.request.urlopen('http://customer-service').read()
    _jsonDecode = {"customers":["T. Geddes Grant","IBM","Wysinco","United Fruit Company"]} #json.loads('{"customers":["T. Geddes Grant","IBM","Wysinco","United Fruit Company"]}')
    return render_template(index.html, result = _jsonDecode)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
