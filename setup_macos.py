"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

PYMEDPHYS_DIR = '/Users/stuartswerdloff/PythonProjects/pymedphys'
APP = ['qtpseudo/qtpseudo_main.py']
DATA_FILES = ['/Users/stuartswerdloff/PythonProjects/pymedphys/pymedphys/_imports/imports.py',
                 PYMEDPHYS_DIR + 'pymedphys/_imports/imports.py',
                 PYMEDPHYS_DIR +'pymedphys/_experimental/pseudonymisation/identifying_uids.json', 
                 PYMEDPHYS_DIR +'pymedphys/_data/zenodo.json' ,
                 PYMEDPHYS_DIR +'pymedphys/_data/urls.json' ,
                 PYMEDPHYS_DIR +'pymedphys/_data/hashes.json' ,
                 PYMEDPHYS_DIR +'pymedphys/_dicom/constants/baseline_repeaters_dictionary.json' ,
                 PYMEDPHYS_DIR +'pymedphys/_dicom/anonymise/identifying_keywords.json' ,
                 PYMEDPHYS_DIR +'pymedphys/_trf/decode/config.json' ,


]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
