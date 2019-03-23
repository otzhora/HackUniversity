import librosa
from file_manager import FileManager
import os
import numpy as np

def concat_music(ids, files, outputFile):
    res = []
    annotation = []
    curr_dur = 0

    for id_ in ids:
        y, sr = librosa.load(files[id_]['path'], sr=44100)
        res = np.concatenate((res, y))
        curr_dur += librosa.core.get_duration(y, 44100)

        annotation.append({
            'time': curr_dur, 
            'file': files[id_]
        })
    print(res)
    print(len(res))
    print(librosa.core.get_duration(res, 44100))
    librosa.output.write_wav(outputFile, res, 44100)
    return annotation



if __name__ == '__main__':
    ALLOWED_EXT = set(['wav', 'mp3'])
    fm = FileManager(os.getcwd() + '/server/static/music/', ALLOWED_EXT)
    files = fm.get_registred_files()

    ids = list(files.keys())

    ann = concat_music(ids[5:8], files, 'libr_test.wav')
    print(ann)
    