"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['home.py']
DATA_FILES = ['qq.py', 'kandian.py', 'dbfunc.py', 'gfunc.py', 'DBHelper', 'CustomWidget']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
