# repository.py
import git

class Repository:
    def __init__(self, name, repo_url, clone_dir, branch_name, checkout_id=None):
        self.name = name
        self.repo_url = repo_url
        self.clone_dir = clone_dir
        self.branch_name = branch_name
        self.checkout_id = checkout_id
    
    def __del__(self):
        print(f"Deletion instance Repository: {self.name}")
    
    def prepare_repository(self):
        print(f"git clone {self.repo_url} {self.clone_dir}")
        repo = git.Repo.clone_from(self.repo_url, self.clone_dir, b=self.branch_name)
        if repo and self.checkout_id is not None:
            repo.git.checkout(self.checkout_id)
        
        if repo:
            return 1
        else:
            return 0