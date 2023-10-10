from src.releasereporender import ReleaseRepoRender
   
def main():
    rrr = ReleaseRepoRender("3r.yml")
    rrr.prepare_repositories()

if __name__ == '__main__':
        main()