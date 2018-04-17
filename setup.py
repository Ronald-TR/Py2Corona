# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyforcorona',
    version='0.1.1',
    url='https://github.com/Ronald-TR/Py2Corona',
    license='MIT License',
    author='Ronald Rodrigues Farias',
    author_email='ronald-farias@outlook.com',
    keywords='python3 corona lua mobile game',
    description=u'Write python code, then compile to receive lua-Corona code.',
    packages=['Py2Corona'],
    install_requires=['pillow'],
    python_requires='>=3.6',
)