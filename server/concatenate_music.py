import librosa
from server.file_manager import FileManager
import os
import numpy as np
import subprocess
import json

def concat_music(ids, files, outputFile):
    annotation = []
    curr_dur = 0
    dif = 25000

    y1, sr1 = librosa.load(files[ids[0]]['path'], sr=22050)
    y2, sr2 = librosa.load(files[ids[1]]['path'], sr=22050)
    res = np.zeros(len(y1) + len(y2))

    res[0: len(y1)] = y1[0: len(y1)].copy()
    res[len(y1) - 4 * dif: len(y1) - 3 * dif] += 0.6 * (y2[0:dif].copy())
    res[len(y1) - 3 * dif: len(y1) - 2 * dif] += 0.7 * (y2[dif:2 * dif].copy())
    res[len(y1) - 2 * dif: len(y1) - 1 * dif] += 0.8 * (y2[2 * dif:3 * dif].copy())
    res[len(y1) - dif: len(y1)] += 0.9 * (y2[3 * dif: 4 * dif].copy())
    res[len(y1):len(y1) + len(y2) - 4 * dif] = y2[4*dif:].copy()
    '''
    for id_ in ids:
        y, sr = librosa.load(files[id_]['path'], sr=22050)
        res = np.concatenate((res, y))
        curr_dur += librosa.core.get_duration(y, 22050)

        res[len(y) - 10000] += 

        annotation.append({
            'time': curr_dur, 
            'file': files[id_]
        })
    '''
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

