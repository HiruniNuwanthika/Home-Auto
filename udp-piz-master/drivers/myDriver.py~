#!/usr/bin/env python
###############################################################################
##
##  A sample device driver v0.01
##  @Copyright 2014 MySensors Research Project
##  SCoRe Lab (www.scorelab.org)
##  University of Colombo School of Computing
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from random import randint
import datetime
#import RPi.GPIO as GPIO
import time
import sqlite3 as lite
import sys
import requests
import data
import version1 
import version2
import version3
import version4
import version5
import version6
#import control



#following variables will ve used to handle the GPIO ports
GPIOLock=False
GPIOStatus=[False,False,False,False,False,False,False,False,
False,False,False,False,False,False,False,False]


class myDriver:
  
   def __init__(self):
      GPIOLock=False
      #Set the GPIO Ports
      #GPIO.setmode(GPIO.BOARD)
      #GPIO.setwarnings(False)
      #GPIO.setup(13,GPIO.OUT)
      #GPIO.setup(15,GPIO.OUT)
	#x=data.light();
   #In order to read the sensor values, separate functions should be implemented. 

  
	#if light ON in version1 is available, read the value return it 
   def readversion1_light_on(self):
		return version1.light_on()	     
	
	#if light OFF in version1 is available, read the value return it 
   def readversion1_light_off(self):
		return version1.light_off()

	#if light CHECK in version1 is available, read the value return it 
   def readversion1_light_check(self):
		return version1.light_check()
	
	#if fan ON in version1 is available, read the value return it 
   def readversion1_fan_on(self):
		return version1.fan_on()

	#if fan OFF in version1 is available, read the value return it 
   def readversion1_fan_off(self):
		return version1.fan_off()

	#if fan CHECK in version1 is available, read the value return it 
   def readversion1_fan_check(self):
		return version1.fan_check()

	#if Automatic light ON in version1 is available, read the value return it 
   def readversion1_autolight_on(self):
		return version1.autolight_on()

	#if Automatic light OFF in version1 is available, read the value return it 
   def readversion1_autolight_off(self):
		return version1.autolight_off()

	#if Automatic light CHECK in version1 is available, read the value return it 
   def readversion1_autolight_check(self):
		return version1.autolight_check()

	#if humidity CHECK in version1 is available, read the value return it 
   def readversion1_humid_check(self):
		 return version1.humid_check()

	#if temperature CHECK in version1 is available, read the value return it 
   def readversion1_temp_check(self):
		 return version1.temp_check()

	#if pir ACTIVATE in version1 is available, read the value return it 
   def readversion1_pir_on(self):
		 return version1.pir_on()

	#if pir DEACTIVATE in version1 is available, read the value return it 
   def readversion1_pir_off(self):
		 return version1.pir_off()

	#if pir CHECK in version1 is available, read the value return it 
   def readversion1_pir_check(self):
		 return version1.pir_check()

	#if vibration ACTIVATE in version1 is available, read the value return it 
   def readversion1_vibration_on(self):
		 return version1.vibration_on()

	#if vibration DEACTIVATE in version1 is available, read the value return it 
   def readversion1_vibration_off(self):
		 return version1.vibration_off()

	#if vibration CHECK in version1 is available, read the value return it 
   def readversion1_vibration_check(self):
		 return version1.vibration_check()

	#if door LOCK in version1 is available, read the value return it 
   def readversion1_door_lock(self):
		 return version1.door_lock()

	#if door UNLOCK in version1 is available, read the value return it 
   def readversion1_door_unlock(self):
		 return version1.door_unlock()

	#if door CHECK in version1 is available, read the value return it 
   def readversion1_door_check(self):
		 return version1.door_check()

	#if leak ACTIVATE in version1 is available, read the value return it 
   def readversion1_leak_on(self):
		 return version1.leak_on()

	#if leak DEACTIVATE in version1 is available, read the value return it 
   def readversion1_leak_off(self):
		 return version1.leak_off()

	#if leak CHECK in version1 is available, read the value return it 
   def readversion1_leak_check(self):
		 return version1.leak_check()

	#if smoke ACTIVATE in version1 is available, read the value return it 
   def readversion1_smoke_on(self):
		 return version1.smoke_on()

	#if smoke DEACTIVATE in version1 is available, read the value return it 
   def readversion1_smoke_off(self):
		 return version1.smoke_off()

	#if smoke CHECK in version1 is available, read the value return it 
   def readversion1_smoke_check(self):
		 return version1.smoke_check()





	#if light ON in version2 is available, read the value return it 
   def readversion2_light_on(self):
		return version2.light_on()	

	#if light OFF in version2 is available, read the value return it 
   def readversion2_light_off(self):
		return version2.light_off()	

	#if light CHECK in version2 is available, read the value return it 
   def readversion2_light_check(self):
		return version2.light_check()
	
	#if fan ON in version2 is available, read the value return it 
   def readversion2_fan_on(self):
		return version2.fan_on()

	#if fan OFF in version2 is available, read the value return it 
   def readversion2_fan_off(self):
		return version2.fan_off()

	#if fan CHECK in version2 is available, read the value return it 
   def readversion2_fan_check(self):
		return version2.fan_check()

	#if Automatic light ON in version2 is available, read the value return it 
   def readversion2_autolight_on(self):
		return version2.autolight_on()

	#if Automatic light OFF in version2 is available, read the value return it 
   def readversion2_autolight_off(self):
		return version2.autolight_off()

	#if Automatic light CHECK in version2 is available, read the value return it 
   def readversion2_autolight_check(self):
		return version2.autolight_check()

	#if humidity CHECK in version2 is available, read the value return it 
   def readversion2_humid_check(self):
		 return version2.humid_check()

	#if temperature CHECK in version2 is available, read the value return it 
   def readversion2_temp_check(self):
		 return version2.temp_check()

	#if pir ACTIVATE in version2 is available, read the value return it 
   def readversion2_pir_on(self):
		 return version2.pir_on()

	#if pir DEACTIVATE in version2 is available, read the value return it 
   def readversion2_pir_off(self):
		 return version2.pir_off()

	#if pir CHECK in version2 is available, read the value return it 
   def readversion2_pir_check(self):
		 return version2.pir_check()

	#if smoke ACTIVATE in version2 is available, read the value return it 
   def readversion2_smoke_on(self):
		 return version2.smoke_on()

	#if smoke DEACTIVATE in version2 is available, read the value return it 
   def readversion2_smoke_off(self):
		 return version2.smoke_off()

	#if smoke CHECK in version2 is available, read the value return it 
   def readversion2_smoke_check(self):
		 return version2.smoke_check()

	#if sound ACTIVATE in version2 is available, read the value return it 
   def readversion2_sound_on(self):
		 return version2.sound_on()

	#if sound DEACTIVATE in version2 is available, read the value return it 
   def readversion2_sound_off(self):
		 return version2.sound_off()

	#if sound CHECK in version2 is available, read the value return it 
   def readversion2_sound_check(self):
		 return version2.sound_check()

	#if door LOCK in version2 is available, read the value return it 
   def readversion2_door_lock(self):
		 return version2.door_lock()

	#if door UNLOCK in version2 is available, read the value return it 
   def readversion2_door_unlock(self):
		 return version2.door_unlock()

	#if door CHECK in version2 is available, read the value return it 
   def readversion2_door_check(self):
		 return version2.door_check()



	#if light ON in version3 is available, read the value return it 
   def readversion3_light_on(self):
		return version3.light_on()	

	#if light OFF in version3 is available, read the value return it 
   def readversion3_light_off(self):
		return version3.light_off()	

	#if light CHECK in version3 is available, read the value return it 
   def readversion3_light_check(self):
		return version3.light_check()
	
	#if fan ON in version3 is available, read the value return it 
   def readversion3_fan_on(self):
		return version3.fan_on()

	#if fan OFF in version3 is available, read the value return it 
   def readversion3_fan_off(self):
		return version3.fan_off()

	#if fan CHECK in version3 is available, read the value return it 
   def readversion3_fan_check(self):
		return version3.fan_check()

	#if Automatic light ON in version3 is available, read the value return it 
   def readversion3_autolight_on(self):
		return version3.autolight_on()
						
	#if Automatic light OFF in version3 is available, read the value return it 
   def readversion3_autolight_off(self):
		return version3.autolight_off()

	#if Automatic light CHECK in version3 is available, read the value return it 
   def readversion3_autolight_check(self):
		return version3.autolight_check()

	#if humidity CHECK in version3 is available, read the value return it 
   def readversion3_humid_check(self):
		 return version3.humid_check()

	#if temperature CHECK in version3 is available, read the value return it 
   def readversion3_temp_check(self):
		 return version3.temp_check()

	#if pir ACTIVATE in version3 is available, read the value return it 
   def readversion3_pir_on(self):
		 return version3.pir_on()

	#if pir DEACTIVATE in version3 is available, read the value return it 
   def readversion3_pir_off(self):
		 return version3.pir_off()

	#if pir CHECK in version3 is available, read the value return it 
   def readversion3_pir_check(self):
		 return version3.pir_check()

	#if smoke ACTIVATE in version3 is available, read the value return it 
   def readversion3_smoke_on(self):
		 return version3.smoke_on()

	#if smoke DEACTIVATE in version3 is available, read the value return it 
   def readversion3_smoke_off(self):
		 return version3.smoke_off()

	#if smoke CHECK in version3 is available, read the value return it 
   def readversion3_smoke_check(self):
		 return version3.smoke_check()

	#if sound ACTIVATE in version3 is available, read the value return it 
   def readversion3_sound_on(self):
		 return version3.sound_on()

	#if sound DEACTIVATE in version3 is available, read the value return it 
   def readversion3_sound_off(self):
		 return version3.sound_off()

	#if sound CHECK in version3 is available, read the value return it 
   def readversion3_sound_check(self):
		 return version3.sound_check()

	#if vibration ACTIVATE in version3 is available, read the value return it 
   def readversion3_vibration_on(self):
		 return version3.vibration_on()

	#if vibration DEACTIVATE in version3 is available, read the value return it 
   def readversion3_vibration_off(self):
		 return version3.vibration_off()

	#if vibration CHECK in version3 is available, read the value return it 
   def readversion3_vibration_check(self):
		 return version3.vibration_check()

	#if door LOCK in version3 is available, read the value return it 
   def readversion3_door_lock(self):
		 return version3.door_lock()

	#if door UNLOCK in version3 is available, read the value return it 
   def readversion3_door_unlock(self):
		 return version3.door_unlock()

	#if door CHECK in version3 is available, read the value return it 
   def readversion3_door_check(self):
		 return version3.door_check()



	#if light ON in version4 is available, read the value return it 
   def readversion4_light_on(self):
		return version4.light_on()	     
	
	#if light OFF in version4 is available, read the value return it 
   def readversion4_light_off(self):
		return version4.light_off()

	#if light CHECK in version4 is available, read the value return it 
   def readversion4_light_check(self):
		return version4.light_check()
	
	#if fan ON in version4 is available, read the value return it 
   def readversion4_fan_on(self):
		return version4.fan_on()

	#if fan OFF in version4 is available, read the value return it 
   def readversion4_fan_off(self):
		return version4.fan_off()

	#if fan CHECK in version4 is available, read the value return it 
   def readversion4_fan_check(self):
		return version4.fan_check()

	#if Automatic light ON in version4 is available, read the value return it 
   def readversion4_autolight_on(self):
		return version4.autolight_on()

	#if Automatic light OFF in version4 is available, read the value return it 
   def readversion4_autolight_off(self):
		return version4.autolight_off()

	#if Automatic light CHECK in version4 is available, read the value return it 
   def readversion4_autolight_check(self):
		return version4.autolight_check()

	#if humidity CHECK in version4 is available, read the value return it 
   def readversion4_humid_check(self):
		 return version4.humid_check()

	#if temperature CHECK in version4 is available, read the value return it 
   def readversion4_temp_check(self):
		 return version4.temp_check()

	#if pir ACTIVATE in version4 is available, read the value return it 
   def readversion4_pir_on(self):
		 return version4.pir_on()

	#if pir DEACTIVATE in version4 is available, read the value return it 
   def readversion4_pir_off(self):
		 return version4.pir_off()

	#if pir CHECK in version4 is available, read the value return it 
   def readversion4_pir_check(self):
		 return version4.pir_check()

	#if smoke ACTIVATE in version4 is available, read the value return it 
   def readversion4_smoke_on(self):
		 return version4.smoke_on()

	#if smoke DEACTIVATE in version4 is available, read the value return it 
   def readversion4_smoke_off(self):
		 return version4.smoke_off()

	#if smoke CHECK in version4 is available, read the value return it 
   def readversion4_smoke_check(self):
		 return version4.smoke_check()

	#if tank Valve ON in version4 is available, read the value return it 
   def readversion4_tankValve_on(self):
		 return version4.tankValve_on()

	#if tank Valve OFF in version4 is available, read the value return it 
   def readversion4_tankValve_off(self):
		 return version4.tankValve_off()

	#if tank Valve CHECK in version4 is available, read the value return it 
   def readversion_tankValve_check(self):
		 return version4.tankValve_check()

	#if rain ON in version4 is available, read the value return it 
   def readversion4_rain_on(self):
		 return version4.rain_on()

	#if rain OFF in version4 is available, read the value return it 
   def readversion4_rain_off(self):
		 return version4.rain_off()

	#if rain CHECK in version4 is available, read the value return it 
   def readversion4_rain_check(self):
		 return version4.rain_check()




	#if light ON in version5 is available, read the value return it 
   def readversion5_light_on(self):
		return version5.light_on()	     
	
	#if light OFF in version5 is available, read the value return it 
   def readversion5_light_off(self):
		return version5.light_off()

	#if light CHECK in version5 is available, read the value return it 
   def readversion5_light_check(self):
		return version5.light_check()
	
	#if fan ON in version5 is available, read the value return it 
   def readversion5_fan_on(self):
		return version5.fan_on()

	#if fan OFF in version5 is available, read the value return it 
   def readversion5_fan_off(self):
		return version5.fan_off()

	#if fan CHECK in version5 is available, read the value return it 
   def readversion5_fan_check(self):
		return version5.fan_check()

	#if Automatic light ON in version5 is available, read the value return it 
   def readversion5_autolight_on(self):
		return version5.autolight_on()

	#if Automatic light OFF in version5 is available, read the value return it 
   def readversion5_autolight_off(self):
		return version5.autolight_off()

	#if Automatic light CHECK in version5 is available, read the value return it 
   def readversion5_autolight_check(self):
		return version5.autolight_check()

	#if humidity CHECK in version5 is available, read the value return it 
   def readversion5_humid_check(self):
		 return version5.humid_check()

	#if temperature CHECK in version5 is available, read the value return it 
   def readversion5_temp_check(self):
		 return version5.temp_check()

	#if pir ACTIVATE in version5 is available, read the value return it 
   def readversion5_pir_on(self):
		 return version5.pir_on()

	#if pir DEACTIVATE in version5 is available, read the value return it 
   def readversion5_pir_off(self):
		 return version5.pir_off()

	#if pir CHECK in version5 is available, read the value return it 
   def readversion5_pir_check(self):
		 return version5.pir_check()

	#if smoke ACTIVATE in version5 is available, read the value return it 
   def readversion5_smoke_on(self):
		 return version5.smoke_on()

	#if smoke DEACTIVATE in version5 is available, read the value return it 
   def readversion5_smoke_off(self):
		 return version5.smoke_off()

	#if smoke CHECK in version5 is available, read the value return it 
   def readversion5_smoke_check(self):
		 return version5.smoke_check()

	#if rain ON in version5 is available, read the value return it 
   def readversion5_rain_on(self):
		 return version5.rain_on()

	#if rain OFF in version5 is available, read the value return it 
   def readversion5_rain_off(self):
		 return version5.rain_off()

	#if rain CHECK in version5 is available, read the value return it 
   def readversion5_rain_check(self):
		 return version5.rain_check()




	#if light ON in version6 is available, read the value return it 
   def readversion6_light_on(self):
		return version6.light_on()	     
	
	#if light OFF in version6 is available, read the value return it 
   def readversion6_light_off(self):
		return version6.light_off()

	#if light CHECK in version6 is available, read the value return it 
   def readversion6_light_check(self):
		return version6.light_check()
	
	#if fan ON in version6 is available, read the value return it 
   def readversion6_fan_on(self):
		return version6.fan_on()

	#if fan OFF in version6 is available, read the value return it 
   def readversion6_fan_off(self):
		return version6.fan_off()

	#if fan CHECK in version6 is available, read the value return it 
   def readversion6_fan_check(self):
		return version6.fan_check()

	#if Automatic light ON in version6 is available, read the value return it 
   def readversion6_autolight_on(self):
		return version6.autolight_on()

	#if Automatic light OFF in version6 is available, read the value return it 
   def readversion6_autolight_off(self):
		return version6.autolight_off()

	#if Automatic light CHECK in version6 is available, read the value return it 
   def readversion6_autolight_check(self):
		return version6.autolight_check()

	#if humidity CHECK in version6 is available, read the value return it 
   def readversion6_humid_check(self):
		 return version6.humid_check()

	#if temperature CHECK in version6 is available, read the value return it 
   def readversion6_temp_check(self):
		 return version6.temp_check()

	#if pir ACTIVATE in version6 is available, read the value return it 
   def readversion6_pir_on(self):
		 return version6.pir_on()

	#if pir DEACTIVATE in version6 is available, read the value return it 
   def readversion6_pir_off(self):
		 return version6.pir_off()

	#if pir CHECK in version6 is available, read the value return it 
   def readversion6_pir_check(self):
		 return version6.pir_check()

	#if smoke ACTIVATE in version6 is available, read the value return it 
   def readversion6_smoke_on(self):
		 return version6.smoke_on()

	#if smoke DEACTIVATE in version6 is available, read the value return it 
   def readversion6_smoke_off(self):
		 return version6.smoke_off()

	#if smoke CHECK in version6 is available, read the value return it 
   def readversion6_smoke_check(self):
		 return version6.smoke_check()

	#if vibration ON in version6 is available, read the value return it 
   def readversion6_vibration_on(self):
		 return version6.vibration_on()

	#if vibration OFF in version6 is available, read the value return it 
   def readversion6_vibration_off(self):
		 return version6.vibration_off()

	#if vibration CHECK in version6 is available, read the value return it 
   def readversion6_vibration_check(self):
		 return version6.vibration_check()

	#if soil valve ON in version6 is available, read the value return it 
   def readversion6_soilvalve_on(self):
		 return version6.soilvalve_on()

	#if soil valve OFF in version6 is available, read the value return it 
   def readversion6_soilvalve_off(self):
		 return version6.soilvalve_off()

	#if soil valve CHECK in version6 is available, read the value return it 
   def readversion6_soilvalve_check(self):
		 return version6.soilvalve_check()

	#if soil ON in version6 is available, read the value return it 
   def readversion6_soil_on(self):
		 return version6.soil_on()

	#if soil OFF in version6 is available, read the value return it 
   def readversion6_soil_off(self):
		 return version6.soil_off()

	#if soil CHECK in version6 is available, read the value return it 
   def readversion6_soil_check(self):
		 return version6.soil_check()




	#if light ON in version7 is available, read the value return it 
   def readversion7_light_on(self):
		return version7.light_on()	     
	
	#if light OFF in version7 is available, read the value return it 
   def readversion7_light_off(self):
		return version7.light_off()

	#if light CHECK in version7 is available, read the value return it 
   def readversion7_light_check(self):
		return version7.light_check()
	
	#if fan ON in version7 is available, read the value return it 
   def readversion7_fan_on(self):
		return version7.fan_on()

	#if fan OFF in version7 is available, read the value return it 
   def readversion7_fan_off(self):
		return version7.fan_off()

	#if fan CHECK in version7 is available, read the value return it 
   def readversion7_fan_check(self):
		return version7.fan_check()

	#if Automatic light ON in version7 is available, read the value return it 
   def readversion7_autolight_on(self):
		return version7.autolight_on()

	#if Automatic light OFF in version7 is available, read the value return it 
   def readversion7_autolight_off(self):
		return version7.autolight_off()

	#if Automatic light CHECK in version7 is available, read the value return it 
   def readversion7_autolight_check(self):
		return version7.autolight_check()

	#if humidity CHECK in version7 is available, read the value return it 
   def readversion7_humid_check(self):
		 return version7.humid_check()

	#if temperature CHECK in version7 is available, read the value return it 
   def readversion7_temp_check(self):
		 return version7.temp_check()

	#if pir ACTIVATE in version7 is available, read the value return it 
   def readversion7_pir_on(self):
		 return version7.pir_on()

	#if pir DEACTIVATE in version7 is available, read the value return it 
   def readversion7_pir_off(self):
		 return version7.pir_off()

	#if pir CHECK in version7 is available, read the value return it 
   def readversion7_pir_check(self):
		 return version7.pir_check()

	#if smoke ACTIVATE in version7 is available, read the value return it 
   def readversion7_smoke_on(self):
		 return version7.smoke_on()

	#if smoke DEACTIVATE in version7 is available, read the value return it 
   def readversion7_smoke_off(self):
		 return version7.smoke_off()

	#if smoke CHECK in version7 is available, read the value return it 
   def readversion7_smoke_check(self):
		 return version7.smoke_check()

	#if vibration ON in version7 is available, read the value return it 
   def readversion7_vibration_on(self):
		 return version7.vibration_on()

	#if vibration OFF in version7 is available, read the value return it 
   def readversion7_vibration_off(self):
		 return version7.vibration_off()

	#if vibration CHECK in version7 is available, read the value return it 
   def readversion7_vibration_check(self):
		 return version7.vibration_check()

	#if door LOCK in version7 is available, read the value return it 
   def readversion7_door_lock(self):
		 return version7.door_lock()

	#if door UNLOCK in version7 is available, read the value return it 
   def readversion7_door_unlock(self):
		 return version7.door_unlock()

	#if door CHECK in version7 is available, read the value return it 
   def readversion7_door_check(self):
		 return version7.door_check()

	#if window CHECK in version7 is available, read the value return it 
   def readversion7_window_check(self):
		 return version7.window_check()




	#if light ON in all versions is available, read the value return it 
   #def readcontrol_light_on(self):
	#	return control.light_on()	     
	
	#if light OFF in all versions is available, read the value return it 
   #def readcontrol_light_off(self):
	#	return control.light_off()

	#if Automatic light ON in all versions is available, read the value return it 
   #def readcontrol_autolight_on(self):
	#	return control.autolight_on()

	#if Automatic light OFF in version7 is available, read the value return it 
   #def readcontrol_autolight_off(self):
	#	return control.autolight_off()

	#if fan ON in all versions is available, read the value return it 
   #def readcontrol_fan_on(self):
	#	return contol.fan_on()

	#if fan OFF in all versions is available, read the value return it 
   #def readcontrol_fan_off(self):
	#	return control.fan_off()

	#if pir ACTIVATE in all versions is available, read the value return it 
   #def readcontrol_pir_on(self):
	#	 return control.pir_on()

	#if pir DEACTIVATE in all versions is available, read the value return it 
   #def readcontrol_pir_off(self):
	#	 return control.pir_off()

	#if smoke ACTIVATE in all versions is available, read the value return it 
   #def readcontrol_smoke_on(self):
	#	 return control.smoke_on()

	#if smoke DEACTIVATE in all versions is available, read the value return it 
   #def readcontrol_smoke_off(self):
	#	 return control.smoke_off()




   #If GPS is available, read the value return it         
   def readGPS(self):
      return randint(0,1000)
      
   #Read the device time and return it           
   def readTime(self):
       now = datetime.datetime.now()
       #print now.hour,now.minute,now.second
       return '%s,%s,%s' %(now.hour,now.minute,now.second)

   #Read the device date and return it           
   def readDate(self):
       now = datetime.datetime.now()
       #print now.hour,now.minute,now.second
       return '%s,%s,%s' %(now.year,now.month,now.day)
       
   #Read the GPIO port status and return it           
   def readGPIO(self,port):
       global GPIOStatus
       if GPIOStatus[port]:return 'ON'
       else: return 'OFF'
  
   #In order to handle GPIO ports, following functions should be implemented. 
   #For example, if Senze-> PUT #gpio2 @device, then switch 2 will be turned ON.
   def handleON(self,port):
       global GPIOLock
       global GPIOStatus
       #This function should implement the necessary action before it returns the value
       #Wait if someone is accessing the gpio ports
       c=1
       while(GPIOLock):
         time.sleep(c)
         c+=1
         if c>10: return 'ERROR'
       GPIOLock=True
       #Here we should include the function to turn on the switch
       #GPIO.setmode(GPIO.BOARD)
       #GPIO.setup(port,GPIO.OUT)
       #GPIO.output(port,1)
       GPIOStatus[port]=True
       #GPIO.cleanup()
       GPIOLock=False
       print port
       return 'ON'
   
   #For example, if Senze -> :PUT #gpio2 @device, then switch will be turned OFF
   def handleOFF(self,port):
       global GPIOLock
       global GPIOStatus
       #This function should implement necessary action before it returns the value
       #Wait if someone is accessing the device
       c=1
       while(GPIOLock):
         time.sleep(c)
         c+=1
         if c>10: return 'ERROR'
       GPIOLock=True
       #Here we should include the function to turn off the switch
       #GPIO.setmode(GPIO.BOARD)
       #GPIO.setup(port,GPIO.OUT)
       #GPIO.output(port,0)
       GPIOStatus[port]=False
       #GPIO.cleanup()
       GPIOLock=False
       print port
       return 'OFF'

'''
while True:
 gpio=myDriver()
 time.sleep(5)
 print gpio.handleON(15)
 gpio=myDriver()
 time.sleep(5)
 print gpio.handleOFF(15)


sen=myDriver()
print sen.handleON(1)
print sen.handleOFF(1)
print sen.readTp()
print sen.readGPS()
print sen.readTime()

'''
