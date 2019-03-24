from flask import Flask
from flask_cors import CORS
from flask import send_from_directory
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['UPLOAD_FOLDER'] = os.getcwd() + '/server/static/music'

    # serving spa
    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory(os.getcwd() + '/server/dist/css', path)


    @app.route('/')
    def send_index():
        return send_from_directory(os.getcwd() + '/server/dist/', 'index.html')


    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory(os.getcwd() + '/server/dist/js',  path)


    @app.route('/img/<path:path>')
    def send_img(path):
        return send_from_directory(os.getcwd() + '/server/dist/img',  path)


    from server import upl_file

    app.register_blueprint(upl_file.bp)

    from server import concatenate_music

    app.register_blueprint(concatenate_music.bp)
    #app.add_url_rule('/', endpoint='index')
    return app
