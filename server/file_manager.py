from uuid import uuid4
import uuid
import os

class FileManager: 
    def __init__(self):
        self.files = {}


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
    fm = FileManager()

    fold_path = os.getcwd() + 'static/music/'

    file1 = 'test1_output.wav'
    file2 = 'test2.wav'

    fm.register_new_file(fold_path + file1, 'test')

    print(fm.get_registred_files())

    fm.register_new_file(fold_path + file2, 'test2', {'test': 'et'})

    files = fm.get_registred_files()
    print(files)
    print(list(files.keys())[1])
    
    print(fm.get_registred_file(list(files.keys())[1]))