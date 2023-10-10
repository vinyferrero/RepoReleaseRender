# sample/test;py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.releasereporender import ReleaseRepoRender
   
def main():
    rrr = ReleaseRepoRender("3r.yml", "/home/viny/Documents/VinyTech/Rrr")
    rrr.prepare_repositories()

if __name__ == '__main__':
        main()