# LogSerial-Python
tools for creating log of serial port using python
## How to use

run manually with nohup:<br>
*change `ttyUSB0` and `115200` to the serial port and baud rate according to your needs.*<br>
```$ nohup ./run_LogSerial.sh ttyUSB0 115200```

run automaticly with cron:<br>
`$ crontab -e`<br>
add the following line:<br>
*change `ttyUSB0` and `115200` to the serial port and baud rate according to your needs.*<br>
`@reboot . $HOME/.bashrc; <path_of_files>/run_LogSerial.sh ttyUSB0 115200`<br>
you can run many instances of this script in cron or manually, each for different port and different baud rate. in cron, just add more lines with different parameters.
