#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, time, configparser
from os import listdir, stat
from os.path import isfile, join, expanduser
from datetime import datetime, timedelta
from shutil import copy
from gi.repository import Notify

conf_days = 60
conf_dir = "/Downloads/"
conf_dest_dir =  "/Old_Downloads/"


def seach_files():
	files = []
	download_dir = expanduser("~") + conf_dir
	copy_dir = download_dir + conf_dest_dir
 
	for f in listdir(download_dir):
		if isfile(join(download_dir,f)):
			files.append(download_dir + f)

	now = time.mktime(time.localtime())
	for f in files:	
		last_access = time.mktime(time.gmtime(stat(f).st_atime))
		t = (timedelta(seconds=now-last_access).days) 
		Notify.init("Downloads directory")
		if t > conf_days:
			message=Notify.Notification.new("Cleaning downloads directory", 
					"Moving " + f,"dialog-information")
			message.show ()
			time.sleep(3)
			copy(f,copy_dir)


def load_conf():
	config = configparser.ConfigParser()
	config.read(expanduser("~") + ".cleardownloads")
	
	if validate_ini(config):
		conf_days = int(config['OPTIONS']['Days'])
		conf_dir = config['OPTIONS']['DownloadDirectory']
		conf_dest_dir = config['OPTIONS']['DestinationDirectory']


def validate_ini(f):
	return False


if __name__ == "__main__":
	load_conf()
	seach_files()