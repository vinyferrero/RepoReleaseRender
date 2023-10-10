# releasereporender.py

import os
import yaml
from repository import Repository

class ReleaseRepoRender:
    def __init__(self, path):
        with open(path, 'r') as file:
            self.data = yaml.safe_load(file)
            self.folder = self.__get_folder()
            
    def __str__(self):
        str1 = ""
        return str1
    
    def prepare_repositories(self):
        if self.folder is not None:
            for prj in self.data['Release']:
                if 'url' in prj:
                    clone_dir = self.folder + "/" + prj['name']
                    # instanciation project
                    if 'tag' in prj:
                        repository = Repository(prj['name'], prj['url'], clone_dir, prj['branch'], prj['tag'])
                    elif 'commit' in prj:
                        repository = Repository(prj['name'], prj['url'], clone_dir, prj['branch'], prj['commit'])
                    else:
                        repository = Repository(prj['name'], prj['url'], clone_dir, prj['branch'])
                    
                    #preparation of the project
                    if repository.prepare_repository() == 1:
                        print(f"create project {prj['name']} successful")
                    else:
                        print(f"create project {prj['name']} failed")
                    
                    #deletion of the temporary instance of the project
                    del repository
                    
    
    def create_release_folder(self, folder):
        # Check whether the specified path exists or not
        isExist = os.path.exists(folder)
        if isExist:
            # remove directory because it has to be empty
            print(len(os.listdir(folder)))
            if len(os.listdir(folder)) > 0:
                self.__delete_files_in_directory(folder)
            os.rmdir(folder)    
        os.makedirs(folder)
    
    def __delete_files_in_directory(self, directory_path, folder):
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif len(os.listdir(file_path)) > 0:
                    self.__delete_files_in_directory(file_path)
                else:
                    os.rmdir(folder) 
            print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files.")
            
    def __get_folder(self):
        for elt in self.data['Release']:
            print(elt)
            if 'folder' in elt:
                print(elt['folder'])
                return elt['folder']