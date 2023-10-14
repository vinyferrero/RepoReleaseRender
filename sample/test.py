# sample/test.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import src
from src import generate_release_environment
   
def main():
    print("Generating the environment of the release.")
    generate_release_environment("3r.yml", "/home/viny/Documents/VinyTech/Rrr")
    print("the generation of the the environment of the release is terminated.")

if __name__ == '__main__':
        main()