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