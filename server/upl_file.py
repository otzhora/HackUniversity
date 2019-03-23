from flask import Blueprint, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import current_app as app
import os 

bp = Blueprint('upload', __name__, url_prefix='/img')

ALLOWED_EXT = set(['wav'])
 
def allowed_file(filename, ALLOWED_EXT=ALLOWED_EXT):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


@bp.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('upload.uploaded_file',
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


@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)