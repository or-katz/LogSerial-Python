#!/bin/bash

# add execution permission by:
# $ chmod +x run_LogSerial.sh
# use this script to run it automaticly from cron or run it with nohup:
# $ crontab -e
# insert the following line and adjust it to your needs (path, port, and baud rate):
# @reboot . $HOME/.bashrc; ~/MyProject/LogSerial/run_LogSerial.sh ttyUSB0 115200
# run it manually by:
# $ nohup ./run_LogSerial.sh ttyUSB0 115200



sleep 40
# change the path to where the script is
cd ~/MyProject/LogSerial

while true; do
sleep 1
kill -9 $(ps aux|grep "[L]ogSerial.py $1 $2" |awk '{print $2}') > /dev/null 2>&1
sleep 1
python -u LogSerial.py "$1" "$2"
done

