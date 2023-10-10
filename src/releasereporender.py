# releasereporender.py

import os
import yaml
from src.repository import Repository

class ReleaseRepoRender:
    def __init__(self, path, release_dir):
        self.release_dir = release_dir
        self.path = path
        with open(path, 'r') as file:
            self.data = yaml.safe_load(file)
            
    def __str__(self):
        str1 = ""
        return str1
    
    def prepare_repositories(self):
        for prj in self.data['Release']:
            if 'url' in prj:
                clone_dir = self.release_dir + "/" + prj['name']
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

