# RepoReleaseRender

## Description
3r Tool offers to regenerate an specific environment for a release

Most of projects needs different others projects/tools/api that can be internal or external of the project itself.
the version of differents tools needed for the release is a liability to recreate the same environment.

### Why it is important to be able to regenerate an environment of a release ? 
1. To reproduce a bug on a platform that is the same that the user have.
2. To be able to retrograde at anytime for production issues or quality issues
3. To avoid keeping a release heavy file stores to reinstall not fully automattically the project at the release 

## How does it works ?
The differents projects/tools/api needed for the project are saved into a yml file as described below:
```
Release:
  - repo:
    name: "needed_project"
    url: https://github.com/needed_project/needed_project.git
    branch: main
    tag: NEEDED_PROJECT_v1.0.0
  - repo:
    name: "needed_tool"
    url: https://github.com/needed_tool/needed_tool.git
    branch: need_tool_branch
    commit: abcdef0123456789abcdef0123456789abcdef01
  - repo:
    name: "needed_api"
    url: https://github.com/needed_api/needed_api.git
    branch: need_api_branch
````

The 3r tool will parse the yaml file and will regenerate the release according to the information shared into the file.
the mandatory fields are: 
- *name*
- *url*
- *branch*
> if there is no `commit` or `tag` defined into the yaml file so the 3r tool will set repository at the *HEAD* of the branch specified.
If it is defined then it will use `tag` over `commit` to set the repository.

## Example on how to use the 3r tool

```
# sample/test.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import rrr
from rrr import generate_release_environment
   
def main():
    print("Generating the environment of the release.")
    filepath = input("Enter the filepath of the release environmant file (yaml): ")
    dirpath = input("Enter the directory path where the release environmant should be generated: ")
    
    generate_release_environment(filepath, dirpath)
    print("the generation of the the environment of the release is terminated.")

if __name__ == '__main__':
        main()
```

## How to install the tool

### from github
```
pip install git+https://github.com/vinyferrero/RepoReleaseRender.git#egg=rrr
```

### from PyPI
```
In Progress
```
