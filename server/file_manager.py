from uuid import uuid4
import uuid
import os
from os import listdir
from os.path import isfile, join
import json
import librosa

def get_bmp(file_path, bpm_guess=120):
    # on most tracks works fine w\ guess 120

    y, sr = librosa.load(file_path, sr=44000)
    hop_length = 512
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length, start_bpm=bpm_guess)

    return tempo, beats


def allowed_file(filename, ALLOWED_EXT):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def get_title(filename):
    return filename.split('.')[0]

class FileManager: 
    def __init__(self, base_path=None, av_ext=None):
        self.files = {}
        #print(os.path.isfile(os.getcwd() + '/files_backup.json'))

        
        if os.path.isfile(os.getcwd() + '/files_backup.json'):
            print('reading data from files_backup.json')
            with open('files_backup.json', 'r') as f:
                self.files = json.load(f)
        else:
            if base_path and av_ext:
                onlyfiles = [f for f in listdir(base_path) if isfile(join(base_path, f))]
                for file in onlyfiles:
                    if allowed_file(file, av_ext):
                        self.register_new_file(base_path + file, get_title(file))

            with open('files_backup.json', 'w') as outfile:
                json.dump(self.files, outfile)



    def register_new_file(self, file_path, file_title=None, file_properties=None):
        id_ = uuid4()
        id_ = str(id_)
        self.files[id_] = {
            'path': file_path
        }
        self.files[id_]['bpm'] = get_bmp(file_path)[0]
        if file_title:
            self.files[id_]['title'] = file_title
        else:
            self.files[id_]['title'] = get_title(file_path.split('/')[-1])
        if file_properties:
            self.files[id_]['properties'] = file_properties

        with open('files_backup.json', 'w') as outfile:
            json.dump(self.files, outfile)
        return id_

    def get_registred_files(self):
        return self.files


    def get_registred_file(self, file_id):
        return self.files[file_id]


    def fill_bpm(self):
        print('filling missing bpms')

        for id_, file in self.files.items():
            print('filling {}'.format(file['title']))
            if 'bpm' not in file:
                file['bpm'] = get_bmp(file['path'])[0]

        with open('files_backup.json', 'w') as outfile:
            json.dump(self.files, outfile)


if __name__ == '__main__':
    path = os.getcwd() + '/static/music/'
    ALLOWED_EXT = set(['wav', 'mp3'])
    fm = FileManager(path, ALLOWED_EXT)
    from audio import get_bmp
    fm.fill_bpm()
    print(fm.get_registred_files())