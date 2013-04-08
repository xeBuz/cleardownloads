#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import sys, time, configparser
from os import listdir, stat, rename, makedirs
from os.path import isfile, join, expanduser, exists
from datetime import datetime, timedelta
from gi.repository import Notify

conf_days = 30
conf_dir = "/Downloads/"
conf_dest_dir =  "Old_Downloads/"

def seach_files():
	files = []
	download_dir = expanduser("~") + conf_dir
	copy_dir = download_dir + conf_dest_dir

	create_dest_dir(copy_dir)	

	for f in listdir(download_dir):
		if isfile(join(download_dir,f)):
			files.append(f)

	now = time.mktime(time.localtime())
	for f in files:	
		last_access = time.mktime(time.gmtime(stat( download_dir + f).st_atime))
		t = (timedelta(seconds=now-last_access).days) 
		Notify.init("Downloads directory")
		if t > conf_days:
			move_file(f, download_dir, copy_dir)

def move_file(f, dir, dest):
	message=Notify.Notification.new("Cleaning downloads directory", 
			"Moving " + f,"dialog-information")
	message.show ()
	time.sleep(3)
	rename(dir+f, dest+f)

def load_conf():
	config = configparser.ConfigParser()
	config.read(expanduser("~") + ".cleardownloads.cfg")
	
	if validate_ini(config):
		conf_days = int(config['OPTIONS']['Days'])
		conf_dir = config['OPTIONS']['DownloadDirectory']
		conf_dest_dir = config['OPTIONS']['DestinationDirectory']

def validate_ini(f):
	return False

def create_dest_dir(dir):
	if not exists(dir):
		makedirs(dir)

if __name__ == "__main__":
	load_conf()
	seach_files()
