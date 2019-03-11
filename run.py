#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import string
import os

GPIO.cleanup()

reader = SimpleMFRC522.SimpleMFRC522()
repeat = True

def write():
	text = raw_input('New data:')
	print("Now place your tag to write")
	reader.write(text)
	print("Written")

def read():
	os.system('clear')
	decide = raw_input("What would you like to do? READ or WRITE \n")
	if decide=="WRITE":
		write()
	else:
	        print("\n"+"Please hover your RFID key tag over the blue RFID reader.")
		id, text = reader.read()
		containsInt = False
		for x in text:
			if x == "0" or  x == "1" or x == "2" or x =="3" or x == "4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9":
				containsInt = True

		if containsInt:
			print("Invalid tag. Please type in your first and last name or your hacker name.\n")
			write()
		else:
	        	print("\n"+"Welcome to the InfoSec Lab, "+ text + "\n")
			print("IIIIIIIIII                   ffffffffffffffff                   SSSSSSSSSSSSSSS"+"\n"+"I::::::::I                  f::::::::::::::::f                SS:::::::::::::::S"+"\n"+"I::::::::I                 f::::::::::::::::::f              S:::::SSSSSS::::::S"+"\n"+"II::::::II                 f::::::fffffff:::::f              S:::::S     SSSSSSS"+"\n"+"  I::::Innnn  nnnnnnnn     f:::::f       ffffffooooooooooo   S:::::S                eeeeeeeeeeee        cccccccccccccccc"+"\n"+"  I::::In:::nn::::::::nn   f:::::f           oo:::::::::::oo S:::::S              ee::::::::::::ee    cc:::::::::::::::c"+"\n"+"  I::::In::::::::::::::nn f:::::::ffffff    o:::::::::::::::o S::::SSSS          e::::::eeeee:::::ee c:::::::::::::::::c"+"\n"+"  I::::Inn:::::::::::::::nf::::::::::::f    o:::::ooooo:::::o  SS::::::SSSSS    e::::::e     e:::::ec:::::::cccccc:::::c"+"\n"+"  I::::I  n:::::nnnn:::::nf::::::::::::f    o::::o     o::::o    SSS::::::::SS  e:::::::eeeee::::::ec::::::c     ccccccc"+"\n"+"  I::::I  n::::n    n::::nf:::::::ffffff    o::::o     o::::o       SSSSSS::::S e:::::::::::::::::e c:::::c"+"\n"+"  I::::I  n::::n    n::::n f:::::f          o::::o     o::::o            S:::::Se::::::eeeeeeeeeee  c:::::c"+"\n"+"  I::::I  n::::n    n::::n f:::::f          o::::o     o::::o            S:::::Se:::::::e           c::::::c     ccccccc"+"\n"+"II::::::IIn::::n    n::::nf:::::::f         o:::::ooooo:::::oSSSSSSS     S:::::Se::::::::e          c:::::::cccccc:::::c"+"\n"+"I::::::::In::::n    n::::nf:::::::f         o:::::::::::::::oS::::::SSSSSS:::::S e::::::::eeeeeeee   c:::::::::::::::::c"+"\n"+"I::::::::In::::n    n::::nf:::::::f          oo:::::::::::oo S:::::::::::::::SS   ee:::::::::::::e    cc:::::::::::::::c"+"\n"+"IIIIIIIIIInnnnnn    nnnnnnfffffffff            ooooooooooo    SSSSSSSSSSSSSSS       eeeeeeeeeeeeee      cccccccccccccccc")
	       		ts = time.ctime()
	       		f=open("/home/pi/Desktop/enterancerecord.txt","a+")
	        	f.write(text.strip() + "\t" + ts +"\n")
	        	f.close
	        	time.sleep(5)

def mainLoop():
	while repeat:
		read()

mainLoop()
