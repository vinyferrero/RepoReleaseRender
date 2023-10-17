from setuptools import setup, find_packages

setup(
    name="rrr",
    version="0.0.1",
    description= "Tool generating an environment for a release depending on multiproject source code",
    author="Vincent Fontanella",
    license="MIT",
    url="https://github.com/vinyferrero/RepoReleaseRender",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0.1",
        "GitPython"
    ],
)
