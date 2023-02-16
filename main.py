#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO
import time

def cpu_temp():
	thermal_zone = subprocess.Popen(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE)
	out, err = thermal_zone.communicate()
	cpu_temp = int(out.decode())/1000
	return cpu_temp

def check_temp():
	cpu = cpu_temp()
	if (float(cpu) > 70) and not GPIO.input(18):
		GPIO.output(18, True)
	elif float(cpu) <= 60  and GPIO.input(18):
		GPIO.output(18, False)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
while(1):	
	check_temp()
	time.sleep(5)
