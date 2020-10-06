from setuptools import setup, find_packages

setup(
    name='qtpseudo',
    version='0.1',
    url='https://github.com/sjswerdloff/qtpseudo.git',
    author='Stuart Swerdloff',
    author_email='sjswerdloff@gmail.com',
    description='A PyQt5 based GUI front end for PyMedPhys pseudonymisation',
    packages=find_packages(),    
    install_requires=['PyQt5 >= 5.9', 'pymedphys >= 0.33'],
)
