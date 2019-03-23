from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


from flask import send_from_directory
import os


# upload file 
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_PATH = os.getcwd() + '/static/music'
ALLOWED_EXT = set(['wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


@app.route('/img', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



# serving spa
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