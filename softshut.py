#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
from time import sleep

# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
PinFOUR = 7
GPIO.setmode(GPIO.BCM) # Set pin numbering to board numbering
GPIO.setup(PinFOUR, GPIO.IN) # Set up PinFOUR as an input

while (GPIO.input(PinFOUR) == False): # While button not pressed
 GPIO.wait_for_edge(PinFOUR, GPIO.RISING) # Wait for a rising edge on PinFOUR
 sleep(0.1); # Sleep 100ms to avoid triggering a shutdown when a spike occured
 
sleep(2); # Sleep 2s to distinguish a long press from a short press

if (GPIO.input(PinFOUR) == False):
  call('reboot', shell=False) # Initiate OS Reboot
else:
 call('poweroff', shell=False) # Initiate OS Poweroff
