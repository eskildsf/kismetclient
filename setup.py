import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="kismetclient",
    version="0.6",
    author="Eskild Schroll-Fleischer",
    author_email="esf@studerende.dk",
    description=("A python client for the Kismet server protocol."),
    license="MIT",
    keywords="kismet client wifi",
    url="https://github.com/eskildsf/kismetclient",
    packages=['kismetclient'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
