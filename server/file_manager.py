from uuid import uuid4
import uuid
import os
from os import listdir
from os.path import isfile, join

def allowed_file(filename, ALLOWED_EXT):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def get_title(filename):
    return filename.split('.')[0]

class FileManager: 
    def __init__(self, base_path=None, av_ext=None):
        self.files = {}
        
        if base_path and av_ext:
            onlyfiles = [f for f in listdir(base_path) if isfile(join(base_path, f))]
            for file in onlyfiles:
                if allowed_file(file, av_ext):
                    self.register_new_file(base_path + file, get_title(file))



    def register_new_file(self, file_path, file_title=None, file_properties=None):
        id_ = uuid4()
        id_ = str(id_)
        self.files[id_] = {
            'path': file_path
        }
        
        if file_title:
            self.files[id_]['title'] = file_title
        if file_properties:
            self.files[id_]['properties'] = file_properties
        return id_

    def get_registred_files(self):
        return self.files


    def get_registred_file(self, file_id):
        print("get reg files")
        print(self.files)
        return self.files[file_id]

if __name__ == '__main__':
    path = os.getcwd() + '/static/music/'
    ALLOWED_EXT = set(['wav', 'mp3'])
    fm = FileManager(path, ALLOWED_EXT)

    print(fm.get_registred_files())