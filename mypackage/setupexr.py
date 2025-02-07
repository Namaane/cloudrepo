
from setuptools import setup, find_packages

setup(
    name='mypackageexr',
    version='0.1',
    packages=find_packages(exclude=['testsexr*']),
    license='MIT',
    description='EDSA example python package difrent route',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Namaane/cloudrepo.git',
    author='Thapelo',
    author_email='namaanekhakhe@gmail.com'
)