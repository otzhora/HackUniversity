from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


from flask import send_from_directory
import os

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(os.getcwd() + '/dist/css', path)


@app.route('/')
def send_index():
    return send_from_directory(os.getcwd() + '/dist/', 'index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.getcwd() + '/dist/js',  path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(os.getcwd() + '/dist/img',  path)
if __name__ == '__main__':
    app.run()