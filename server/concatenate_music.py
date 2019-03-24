import librosa
from server.file_manager import FileManager
import os
import numpy as np
import subprocess
import json

def concat_music(ids, files, outputFile):
    res = []
    annotation = []
    curr_dur = 0

    for id_ in ids:
        y, sr = librosa.load(files[id_]['path'], sr=22050)
        res = np.concatenate((res, y))
        curr_dur += librosa.core.get_duration(y, 22050)

        annotation.append({
            'time': curr_dur, 
            'file': files[id_]
        })
    print(res)
    print(len(res))
    print(librosa.core.get_duration(res, 22050))
    librosa.output.write_wav('buf.wav', res, 22050)
    subprocess.call(["ffmpeg", "-y", "-i", "buf.wav", "-vn", "-ar", "22050", "-ac", "2", "-b:a", "192k", "-f", "mp3", outputFile])
    subprocess.call(['rm', 'buf.wav'])
    return annotation



if __name__ == '__main__':
    ALLOWED_EXT = set(['wav', 'mp3'])
    fm = FileManager(os.getcwd() + '/server/static/music/', ALLOWED_EXT)
    files = fm.get_registred_files()

    ids = list(files.keys())

    ann = concat_music(ids[2:4], files, 'static/libr_test.mp3')
    print(ann)
    

ALLOWED_EXT = set(['wav', 'mp3'])
fm = FileManager(os.getcwd() + '/server/static/music/', ALLOWED_EXT)
files = fm.get_registred_files()


from flask import Blueprint, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, send_file
from flask import current_app as app

bp = Blueprint('concat', __name__, url_prefix='/concat/')

@bp.route('/', methods=['GET', 'POST'])
def concat():
    if request.method == 'GET':
        return send_from_directory('static', 'libr_test.mp3')
    if request.method == 'POST':
        ids = request.get_json()['ids']
        print(os.getcwd())
        ann = concat_music(ids, files, 'server/static/libr_test.mp3')
        return json.dumps(ann)
    return None

