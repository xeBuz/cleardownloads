#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
setup(
    name='cleardownloads',
    version='0.1',
    author='Jesús F. Roldán',
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/cleardownloads',
    license='LICENSE.txt',
    description='Keep your Download directoy clean, moving old files to another directory',
    long_description=open('README.md').read(),
    requires=[('python-gobject', 'libnotify')],
    data_files=['config',['.cleardownloads']],
    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: BSD License",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Topic :: System :: Archiving"
    ]
) 

 