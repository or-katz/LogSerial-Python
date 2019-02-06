#!/usr/bin/python

import logging
from logging.handlers import RotatingFileHandler
import sys
import serial
import os

# Number of files to keep and size in MB
NumberOfFiles = 10
FileSize = 5



if not os.path.exists('Logs'):
    os.makedirs('Logs')


log_formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(message)s', datefmt="%d/%m/%Y %H:%M:%S")

logFile = 'Logs/SerialLog_'+ sys.argv[1] + '.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=FileSize*1024*1024, 
                                 backupCount=NumberOfFiles, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(my_handler)

#while True:
#    app_log.info("data")
	
	
	
with serial.Serial("/dev/"+sys.argv[1], sys.argv[2]) as ser:
    for line in ser:
        app_log.info(line.strip())
