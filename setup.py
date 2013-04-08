#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup
from os.path import expanduser
from crontab import CronTab

def set_crontab():
    system_cron = CronTab()
    user_cron = CronTab('root')
    file_cron = CronTab(tabfile='filename.tab')
    mem_cron = CronTab(tab="""
    * * * * * command
    """)


setup(
    name='cleardownloads',
    version='1.0a',
    author='Jesús F. Roldán',
    packages=[''],
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/cleardownloads',
    license='LICENSE.txt',
    description='Keep your Download directoy clean, moving old files to another directory',
    long_description=open('README.md').read(),
    install_requires=["python-gobject", "libnotify", "python-crontab"],
    data_files=[(expanduser("~"), ['.cleardownloads.cfg'])],
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

 