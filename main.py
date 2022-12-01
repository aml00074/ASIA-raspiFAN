#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO

def cpu_temp():
	thermal_zone = subprocess.Popen(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE)
	out, err = thermal_zone.communicate()
	cpu_temp = int(out.decode())/1000
	return cpu_temp

def gpu_temp():
	measure_temp = subprocess.Popen([', que '], stdout=subprocess.PIPE)
	out, err = measure_temp.communicate()
	gpu_temp = out.decode().split('=')[1].split('\'')[0]
	return gpu_temp


def check_temp():
	cpu = cpu_temp()
	gpu = gpu_temp()
	if (float(cpu) > 45 or float(gpu) > 45) and not GPIO.input(7):
		GPIO.output(14, True)
	elif float(cpu) <= 40 and float(gpu) <= 40 and GPIO.input(7):
		GPIO.output(14, False)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14,GPIO.OUT)
check_temp()

print ("CPU: "+str(cpu_temp())+"º")
print ("GPU: "+str(gpu_temp())+"º")
