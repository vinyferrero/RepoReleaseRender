from setuptools import setup, find_packages

setup(
    name="rrr",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0.1",
        "GitPython"
    ],
)
