#!/usr/bin/env python

###############################################################################
##
##  My Sensor UDP Client v1.0
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

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import datetime

import socket
import time
import sys
import thread
import os.path
lib_path = os.path.abspath('../utils')
sys.path.append(lib_path)
lib_path = os.path.abspath('../drivers')
sys.path.append(lib_path)
from myCrypto import *
from myDriver import *
from myCamDriver import *
from senz import *

buf=''
aesKeys={}

class myHandler(DatagramProtocol):
  
    def __init__(self,transport,device,senz):
        self.tp= transport
        self.senz = senz
        self.device=device
        #self._reactor=reactor
        #self.ip=reactor.resolve(host)

    def saveRootKey(self,capubkey):
        cry = myCrypto(name=self.senz.sender)
        cry.saveRSAPubKey(capubkey)

    def registrationDone(self):
        cry = myCrypto(name=self.device)
        state="INITIAL"
        if 'msg' in self.senz.sensors and 'pubkey' in self.senz.sensors:
            if cry.verifySENZE(self.senz,self.senz.data['pubkey']):
                if 'REG_DONE' in self.senz.data['msg']:
                    self.saveRootKey(self.senz.data['pubkey'])
                    state='READY'
                    print (self.device + " was created at the server.")
                    print ("You should execute the program again with READY state.")
                elif 'REG_ALR' in self.senz.data['msg']:
                    print (self.device + " was already created at the server.")
                    state="READY"
                else:
                    print ("This user name is already taken")
                    print ("You can try it again with different username")
                    print ("The system halted!")
            else:
                print ("SENZE Verification failed")
        else:
            print ("Unknown server response")
        return state

    def sendDatagram(self, senze):
        cry = myCrypto(name=self.device)
        senze = cry.signSENZE(senze)
        print(senze)
        self.tp.write(senze)

    #Senze response should be built as follows by calling the functions in the driver class
    def sendDataSenze(self,sensors,data,recipient):
        response='DATA'
        driver=myDriver()
        cry=myCrypto(self.device)
        for sensor in sensors:
            
			#If light on in version1 is requested  
            if "version1_light_on" == sensor:
                response ='%s #version1_light_on %s' %(response,driver.readversion1_light_on())

			#If light off in version1 is requested 
            elif "version1_light_off" == sensor:
                response ='%s #version1_light_off %s' %(response,driver.readversion1_light_off())

			#If light check in version1 is requested  
            elif "version1_light_check" == sensor:
                response ='%s #version1_light_check %s' %(response,driver.readversion1_light_check())

			#If fan on in version1 is requested 
            elif "version1_fan_on" == sensor:
                response ='%s #version1_fan_on %s' %(response,driver.readversion1_fan_on())

			#If fan off in version1 is requested 
            elif "version1_fan_off" == sensor:
                response ='%s #version1_fan_off %s' %(response,driver.readversion1_fan_off())

			#If fan check in version1 is requested 
            elif "version1_fan_check" == sensor:
                response ='%s #version1_fan_check %s' %(response,driver.readversion1_fan_check())

			#If automatic light on in version1 is requested 
            elif "version1_autolight_on" == sensor:
                response ='%s #version1_autolight_on %s' %(response,driver.readversion1_autolight_on())

			#If automatic light off in version1 is requested 
            elif "version1_autolight_off" == sensor:
                response ='%s #version1_autolight_off %s' %(response,driver.readversion1_autolight_off())

			#If automatic light check in version1 is requested 
            elif "version1_autolight_check" == sensor:
                response ='%s #version1_autolight_check %s' %(response,driver.readversion1_autolight_check())

			#If temp check in version1 is requested
            elif "version1_temp_check" == sensor:
                response ='%s #version1_temp_check %s' %(response,driver.readversion1_temp_check())

			#If humidity check in version1 is requested
            elif "version1_humid_check" == sensor:
                response ='%s #version1_humid_check %s' %(response,driver.readversion1_humid_check())

			#If pir sensor on in version1 is requested
            elif "version1_pir_on" == sensor:
                response ='%s #version1_pir_on %s' %(response,driver.readversion1_pir_on())

			#If pir sensor off in version1 is requested
            elif "version1_pir_off" == sensor:
                response ='%s #version1_pir_off %s' %(response,driver.readversion1_pir_off())

			#If pir sensor check in version1 is requested
            elif "version1_pir_check" == sensor:
                response ='%s #version1_pir_check %s' %(response,driver.readversion1_pir_check())
						
			#If vibration sensor on in version1 is requested
            elif "version1_vibration_on" == sensor:
                response ='%s #version1_vibration_on %s' %(response,driver.readversion1_vibration_on())

			#If vibration sensor off in version1 is requested
            elif "version1_vibration_off" == sensor:
                response ='%s #version1_vibration_off %s' %(response,driver.readversion1_vibration_off())

			#If vibration sensor check in version1 is requested
            elif "version1_vibration_check" == sensor:
                response ='%s #version1_vibration_check %s' %(response,driver.readversion1_vibration_check())

			#If door lock in version1 is requested
            elif "version1_door_lock" == sensor:
                response ='%s #version1_door_lock %s' %(response,driver.readversion1_door_lock())

			#If door unlock in version1 is requested
            elif "version1_door_unlock" == sensor:
                response ='%s #version1_door_unlock %s' %(response,driver.readversion1_door_unlock())

			#If door check in version1 is requested
            elif "version1_door_check" == sensor:
                response ='%s #version1_door_check %s' %(response,driver.readversion1_door_check())

			#If leakage sensor on in version1 is requested
            elif "version1_leak_on" == sensor:
                response ='%s #version1_leak_on %s' %(response,driver.readversion1_leak_on())

			#If leakage sensor off in version1 is requested
            elif "version1_leak_off" == sensor:
                response ='%s #version1_leak_off %s' %(response,driver.readversion1_leak_off())

			#If leakage sensor check in version1 is requested
            elif "version1_leak_check" == sensor:
                response ='%s #version1_leak_check %s' %(response,driver.readversion1_leak_check())

			#If smoke sensor on in version1 is requested
            elif "version1_smoke_on" == sensor:
                response ='%s #version1_smoke_on %s' %(response,driver.readversion1_smoke_on())

			#If smoke sensor off in version1 is requested
            elif "version1_smoke_off" == sensor:
                response ='%s #version1_smoke_off %s' %(response,driver.readversion1_smoke_off())

			#If smoke sensor check in version1 is requested
            elif "version1_smoke_check" == sensor:
                response ='%s #version1_smoke_check %s' %(response,driver.readversion1_smoke_check())



			#If light on in version2 is requested  
            elif "version2_light_on" == sensor:
                response ='%s #version2_light_on %s' %(response,driver.readversion2_light_on())

			#If light off in version2 is requested 
            elif "version2_light_off" == sensor:
                response ='%s #version2_light_off %s' %(response,driver.readversion2_light_off())

			#If light check in version2 is requested  
            elif "version2_light_check" == sensor:
                response ='%s #version2_light_check %s' %(response,driver.readversion2_light_check())

			#If fan on in version2 is requested 
            elif "version2_fan_on" == sensor:
                response ='%s #version2_fan_on %s' %(response,driver.readversion2_fan_on())

			#If fan off in version2 is requested 
            elif "version2_fan_off" == sensor:
                response ='%s #version2_fan_off %s' %(response,driver.readversion2_fan_off())

			#If fan check in version2 is requested 
            elif "version2_fan_check" == sensor:
                response ='%s #version2_fan_check %s' %(response,driver.readversion2_fan_check())

			#If automatic light on in version2 is requested 
            elif "version2_autolight_on" == sensor:
                response ='%s #version2_autolight_on %s' %(response,driver.readversion2_autolight_on())

			#If automatic light off in version2 is requested 
            elif "version2_autolight_off" == sensor:
                response ='%s #version2_autolight_off %s' %(response,driver.readversion2_autolight_off())

			#If automatic light check in version2 is requested 
            elif "version2_autolight_check" == sensor:
                response ='%s #version2_autolight_check %s' %(response,driver.readversion2_autolight_check())

			#If temp check in version2 is requested
            elif "version2_temp_check" == sensor:
                response ='%s #version2_temp_check %s' %(response,driver.readversion2_temp_check())

			#If humidity check in version2 is requested
            elif "version2_humid_check" == sensor:
                response ='%s #version2_humid_check %s' %(response,driver.readversion2_humid_check())

			#If pir sensor on in version2 is requested
            elif "version2_pir_on" == sensor:
                response ='%s #version2_pir_on %s' %(response,driver.readversion2_pir_on())

			#If pir sensor off in version2 is requested
            elif "version2_pir_off" == sensor:
                response ='%s #version2_pir_off %s' %(response,driver.readversion2_pir_off())

			#If pir sensor check in version2 is requested
            elif "version2_pir_check" == sensor:
                response ='%s #version2_pir_check %s' %(response,driver.readversion2_pir_check())
						
			#If smoke sensor on in version1 is requested
            elif "version2_smoke_on" == sensor:
                response ='%s #version2_smoke_on %s' %(response,driver.readversion2_smoke_on())

			#If smoke sensor off in version2 is requested
            elif "version2_smoke_off" == sensor:
                response ='%s #version2_smoke_off %s' %(response,driver.readversion2_smoke_off())

			#If smoke sensor check in version2 is requested
            elif "version2_smoke_check" == sensor:
                response ='%s #version2_smoke_check %s' %(response,driver.readversion2_smoke_check())

			#If sound sensor on in version1 is requested
            elif "version2_sound_on" == sensor:
                response ='%s #version2_sound_on %s' %(response,driver.readversion2_sound_on())

			#If sound sensor off in version2 is requested
            elif "version2_sound_off" == sensor:
                response ='%s #version2_sound_off %s' %(response,driver.readversion2_sound_off())

			#If sound sensor check in version2 is requested
            elif "version2_sound_check" == sensor:
                response ='%s #version2_sound_check %s' %(response,driver.readversion2_sound_check())

			#If door lock in version2 is requested
            elif "version2_door_lock" == sensor:
                response ='%s #version2_door_lock %s' %(response,driver.readversion2_door_lock())

			#If door unlock in version2 is requested
            elif "version1_door_unlock" == sensor:
                response ='%s #version1_door_unlock %s' %(response,driver.readversion2_door_unlock())

			#If door check in version2 is requested
            elif "version2_door_check" == sensor:
                response ='%s #version2_door_check %s' %(response,driver.readversion2_door_check())



			#If light on in version3 is requested  
            elif "version3_light_on" == sensor:
                response ='%s #version3_light_on %s' %(response,driver.readversion3_light_on())

			#If light off in version3 is requested 
            elif "version3_light_off" == sensor:
                response ='%s #version3_light_off %s' %(response,driver.readversion3_light_off())

			#If light check in version3 is requested  
            elif "version3_light_check" == sensor:
                response ='%s #version3_light_check %s' %(response,driver.readversion3_light_check())

			#If fan on in version3 is requested 
            elif "version3_fan_on" == sensor:
                response ='%s #version3_fan_on %s' %(response,driver.readversion3_fan_on())

			#If fan off in version3 is requested 
            elif "version3_fan_off" == sensor:
                response ='%s #version3_fan_off %s' %(response,driver.readversion3_fan_off())

			#If fan check in version3 is requested 
            elif "version3_fan_check" == sensor:
                response ='%s #version3_fan_check %s' %(response,driver.readversion3_fan_check())

			#If automatic light on in version3 is requested 
            elif "version3_autolight_on" == sensor:
                response ='%s #version3_autolight_on %s' %(response,driver.readversion3_autolight_on())

			#If automatic light off in version3 is requested 
            elif "version3_autolight_off" == sensor:
                response ='%s #version3_autolight_off %s' %(response,driver.readversion3_autolight_off())

			#If automatic light check in version3 is requested 
            elif "version3_autolight_check" == sensor:
                response ='%s #version3_autolight_check %s' %(response,driver.readversion3_autolight_check())

			#If temp check in version3 is requested
            elif "version3_temp_check" == sensor:
                response ='%s #version3_temp_check %s' %(response,driver.readversion3_temp_check())

			#If humidity check in version3 is requested
            elif "version3_humid_check" == sensor:
                response ='%s #version3_humid_check %s' %(response,driver.readversion3_humid_check())

			#If pir sensor on in version3 is requested
            elif "version3_pir_on" == sensor:
                response ='%s #version3_pir_on %s' %(response,driver.readversion3_pir_on())

			#If pir sensor off in version3 is requested
            elif "version3_pir_off" == sensor:
                response ='%s #version3_pir_off %s' %(response,driver.readversion3_pir_off())

			#If pir sensor check in version3 is requested
            elif "version3_pir_check" == sensor:
                response ='%s #version3_pir_check %s' %(response,driver.readversion3_pir_check())
						
			#If smoke sensor on in version3 is requested
            elif "version3_smoke_on" == sensor:
                response ='%s #version3_smoke_on %s' %(response,driver.readversion3_smoke_on())

			#If smoke sensor off in version3 is requested
            elif "version3_smoke_off" == sensor:
                response ='%s #version3_smoke_off %s' %(response,driver.readversion3_smoke_off())

			#If smoke sensor check in version3 is requested
            elif "version3_smoke_check" == sensor:
                response ='%s #version3_smoke_check %s' %(response,driver.readversion3_smoke_check())

			#If sound sensor on in version3 is requested
            elif "version3_sound_on" == sensor:
                response ='%s #version3_sound_on %s' %(response,driver.readversion3_sound_on())

			#If sound sensor off in version3 is requested
            elif "version3_sound_off" == sensor:
                response ='%s #version3_sound_off %s' %(response,driver.readversion3_sound_off())

			#If sound sensor check in version3 is requested
            elif "version3_sound_check" == sensor:
                response ='%s #version3_sound_check %s' %(response,driver.readversion3_sound_check())

			#If vibration sensor on in version3 is requested
            elif "version3_vibration_on" == sensor:
                response ='%s #version3_vibration_on %s' %(response,driver.readversion3_vibration_on())

			#If vibration sensor off in version3 is requested
            elif "version3_vibration_off" == sensor:
                response ='%s #version3_vibration_off %s' %(response,driver.readversion3_vibration_off())

			#If vibration sensor check in version3 is requested
            elif "version3_vibration_check" == sensor:
                response ='%s #version3_vibration_check %s' %(response,driver.readversion3_vibration_check())

			#If door lock in version3 is requested
            elif "version3_door_lock" == sensor:
                response ='%s #version3_door_lock %s' %(response,driver.readversion3_door_lock())

			#If door unlock in version3 is requested
            elif "version3_door_unlock" == sensor:
                response ='%s #version3_door_unlock %s' %(response,driver.readversion3_door_unlock())

			#If door check in version3 is requested
            elif "version3_door_check" == sensor:
                response ='%s #version3_door_check %s' %(response,driver.readversion3_door_check())



			#If light on in version4 is requested  
            elif "version4_light_on" == sensor:
                response ='%s #version4_light_on %s' %(response,driver.readversion4_light_on())

			#If light off in version4 is requested 
            elif "version4_light_off" == sensor:
                response ='%s #version4_light_off %s' %(response,driver.readversion4_light_off())

			#If light check in version4 is requested  
            elif "version4_light_check" == sensor:
                response ='%s #version4_light_check %s' %(response,driver.readversion4_light_check())

			#If fan on in version4 is requested 
            elif "version4_fan_on" == sensor:
                response ='%s #version4_fan_on %s' %(response,driver.readversion4_fan_on())

			#If fan off in version4 is requested 
            elif "version4_fan_off" == sensor:
                response ='%s #version4_fan_off %s' %(response,driver.readversion4_fan_off())

			#If fan check in version4 is requested 
            elif "version4_fan_check" == sensor:
                response ='%s #version4_fan_check %s' %(response,driver.readversion4_fan_check())

			#If automatic light on in version4 is requested 
            elif "version4_autolight_on" == sensor:
                response ='%s #version4_autolight_on %s' %(response,driver.readversion4_autolight_on())

			#If automatic light off in version4 is requested 
            elif "version4_autolight_off" == sensor:
                response ='%s #version4_autolight_off %s' %(response,driver.readversion4_autolight_off())

			#If automatic light check in version4 is requested 
            elif "version4_autolight_check" == sensor:
                response ='%s #version4_autolight_check %s' %(response,driver.readversion4_autolight_check())

			#If temp check in version4 is requested
            elif "version4_temp_check" == sensor:
                response ='%s #version4_temp_check %s' %(response,driver.readversion4_temp_check())

			#If humidity check in version4 is requested
            elif "version4_humid_check" == sensor:
                response ='%s #version4_humid_check %s' %(response,driver.readversion4_humid_check())

			#If pir sensor on in version4 is requested
            elif "version4_pir_on" == sensor:
                response ='%s #version4_pir_on %s' %(response,driver.readversion4_pir_on())

			#If pir sensor off in version3 is requested
            elif "version4_pir_off" == sensor:
                response ='%s #version4_pir_off %s' %(response,driver.readversion4_pir_off())

			#If pir sensor check in version3 is requested
            elif "version4_pir_check" == sensor:
                response ='%s #version4_pir_check %s' %(response,driver.readversion4_pir_check())
						
			#If smoke sensor on in version4 is requested
            elif "version4_smoke_on" == sensor:
                response ='%s #version4_smoke_on %s' %(response,driver.readversion4_smoke_on())

			#If smoke sensor off in version4 is requested
            elif "version4_smoke_off" == sensor:
                response ='%s #version4_smoke_off %s' %(response,driver.readversion4_smoke_off())

			#If smoke sensor check in version4 is requested
            elif "version4_smoke_check" == sensor:
                response ='%s #version4_smoke_check %s' %(response,driver.readversion4_smoke_check())

			#If tankValve sensor on in version4 is requested
            elif "version4_tankValve_on" == sensor:
                response ='%s #version4_tankValve_on %s' %(response,driver.readversion4_tankValve_on())

			#If tankValve sensor off in version4 is requested
            elif "version4_tankValve_off" == sensor:
                response ='%s #version4_tankValve_off %s' %(response,driver.readversion4_tankValve_off())

			#If tankValve sensor check in version4 is requested
            elif "version4_tankValve_check" == sensor:
                response ='%s #version4_tankValve_check %s' %(response,driver.readversion4_tankValve_check())

			#If rain sensor on in version4 is requested
            elif "version4_rain_on" == sensor:
                response ='%s #version4_rain_on %s' %(response,driver.readversion4_rain_on())

			#If rain sensor off in version4 is requested
            elif "version4_rain_off" == sensor:
                response ='%s #version4_rain_off %s' %(response,driver.readversion4_rain_off())

			#If rain sensor check in version4 is requested
            elif "version4_rain_check" == sensor:
                response ='%s #version4_rain_check %s' %(response,driver.readversion4_rain_check())



			#If light on in version5 is requested  
            elif "version5_light_on" == sensor:
                response ='%s #version5_light_on %s' %(response,driver.readversion5_light_on())

			#If light off in version5 is requested 
            elif "version5_light_off" == sensor:
                response ='%s #version5_light_off %s' %(response,driver.readversion5_light_off())

			#If light check in version5 is requested  
            elif "version5_light_check" == sensor:
                response ='%s #version5_light_check %s' %(response,driver.readversion5_light_check())

			#If fan on in version5 is requested 
            elif "version5_fan_on" == sensor:
                response ='%s #version5_fan_on %s' %(response,driver.readversion5_fan_on())

			#If fan off in version5 is requested 
            elif "version5_fan_off" == sensor:
                response ='%s #version5_fan_off %s' %(response,driver.readversion5_fan_off())

			#If fan check in version5 is requested 
            elif "version5_fan_check" == sensor:
                response ='%s #version5_fan_check %s' %(response,driver.readversion5_fan_check())

			#If automatic light on in version5 is requested 
            elif "version5_autolight_on" == sensor:
                response ='%s #version5_autolight_on %s' %(response,driver.readversion5_autolight_on())

			#If automatic light off in version5 is requested 
            elif "version5_autolight_off" == sensor:
                response ='%s #version5_autolight_off %s' %(response,driver.readversion5_autolight_off())

			#If automatic light check in version5 is requested 
            elif "version5_autolight_check" == sensor:
                response ='%s #version5_autolight_check %s' %(response,driver.readversion5_autolight_check())

			#If temp check in version5 is requested
            elif "version5_temp_check" == sensor:
                response ='%s #version5_temp_check %s' %(response,driver.readversion5_temp_check())

			#If humidity check in version5 is requested
            elif "version5_humid_check" == sensor:
                response ='%s #version5_humid_check %s' %(response,driver.readversion5_humid_check())

			#If pir sensor on in version5 is requested
            elif "version5_pir_on" == sensor:
                response ='%s #version5_pir_on %s' %(response,driver.readversion5_pir_on())

			#If pir sensor off in version5 is requested
            elif "version5_pir_off" == sensor:
                response ='%s #version5_pir_off %s' %(response,driver.readversion5_pir_off())

			#If pir sensor check in version is requested
            elif "version5_pir_check" == sensor:
                response ='%s #version5_pir_check %s' %(response,driver.readversion5_pir_check())
						
			#If smoke sensor on in version5 is requested
            elif "version5_smoke_on" == sensor:
                response ='%s #version5_smoke_on %s' %(response,driver.readversion5_smoke_on())

			#If smoke sensor off in version5 is requested
            elif "version5_smoke_off" == sensor:
                response ='%s #version5_smoke_off %s' %(response,driver.readversion5_smoke_off())

			#If smoke sensor check in version5 is requested
            elif "version5_smoke_check" == sensor:
                response ='%s #version5_smoke_check %s' %(response,driver.readversion5_smoke_check())

			#If rain sensor on in version5 is requested
            elif "version5_rain_on" == sensor:
                response ='%s #version5_rain_on %s' %(response,driver.readversion5_rain_on())

			#If rain sensor off in version5 is requested
            elif "version5_rain_off" == sensor:
                response ='%s #version5_rain_off %s' %(response,driver.readversion5_rain_off())

			#If rain sensor check in version5 is requested
            elif "version5_rain_check" == sensor:
                response ='%s #version5_rain_check %s' %(response,driver.readversion5_rain_check())



			#If light on in version6 is requested  
            elif "version6_light_on" == sensor:
                response ='%s #version6_light_on %s' %(response,driver.readversion6_light_on())

			#If light off in version6 is requested  
            elif "version6_light_off" == sensor:
                response ='%s #version6_light_off %s' %(response,driver.readversion6_light_off())

			#If light check in version6 is requested  
            elif "version6_light_check" == sensor:
                response ='%s #version6_light_check %s' %(response,driver.readversion6_light_check())

			#If fan on in version6 is requested 
            elif "version6_fan_on" == sensor:
                response ='%s #version6_fan_on %s' %(response,driver.readversion6_fan_on())

			#If fan off in version6 is requested 
            elif "version6_fan_off" == sensor:
                response ='%s #version6_fan_off %s' %(response,driver.readversion6_fan_off())

			#If fan check in version6 is requested 
            elif "version6_fan_check" == sensor:
                response ='%s #version6_fan_check %s' %(response,driver.readversion6_fan_check())

			#If automatic light on in version6 is requested 
            elif "version6_autolight_on" == sensor:
                response ='%s #version6_autolight_on %s' %(response,driver.readversion6_autolight_on())

			#If automatic light off in version6 is requested 
            elif "version6_autolight_off" == sensor:
                response ='%s #version6_autolight_off %s' %(response,driver.readversion6_autolight_off())

			#If automatic light check in version6 is requested 
            elif "version6_autolight_check" == sensor:
                response ='%s #version6_autolight_check %s' %(response,driver.readversion6_autolight_check())

			#If temp check in version6 is requested
            elif "version6_temp_check" == sensor:
                response ='%s #version6_temp_check %s' %(response,driver.readversion6_temp_check())

			#If humidity check in version6 is requested
            elif "version6_humid_check" == sensor:
                response ='%s #version6_humid_check %s' %(response,driver.readversion6_humid_check())

			#If pir sensor on in version6 is requested
            elif "version6_pir_on" == sensor:
                response ='%s #version6_pir_on %s' %(response,driver.readversion6_pir_on())

			#If pir sensor off in version6 is requested
            elif "version6_pir_off" == sensor:
                response ='%s #version6_pir_off %s' %(response,driver.readversion6_pir_off())

			#If pir sensor check in version6 is requested
            elif "version6_pir_check" == sensor:
                response ='%s #version6_pir_check %s' %(response,driver.readversion6_pir_check())
						
			#If smoke sensor on in version6 is requested
            elif "version6_smoke_on" == sensor:
                response ='%s #version6_smoke_on %s' %(response,driver.readversion6_smoke_on())

			#If smoke sensor off in version6 is requested
            elif "version6_smoke_off" == sensor:
                response ='%s #version6_smoke_off %s' %(response,driver.readversion6_smoke_off())

			#If smoke sensor check in version6 is requested
            elif "version6_smoke_check" == sensor:
                response ='%s #version6_smoke_check %s' %(response,driver.readversion6_smoke_check())

			#If soilvalve sensor on in version6 is requested
            elif "version6_soilvalve_on" == sensor:
                response ='%s #version6_soilvalve_on %s' %(response,driver.readversion6_soilvalve_on())

			#If soilvalve sensor off in version6 is requested
            elif "version6_soilvalve_off" == sensor:
                response ='%s #version6_soilvalve_off %s' %(response,driver.readversion6_soilvalve_off())

			#If soilvalve sensor check in version6 is requested
            elif "version6_soilvalve_check" == sensor:
                response ='%s #version6_soilvalve_check %s' %(response,driver.readversion6_soilvalve_check())

			#If vibration sensor on in version6 is requested
            elif "version6_vibration_on" == sensor:
                response ='%s #version6_vibration_on %s' %(response,driver.readversion6_vibration_on())

			#If vibration sensor off in version6 is requested
            elif "version6_vibration_off" == sensor:
                response ='%s #version6_vibration_off %s' %(response,driver.readversion6_vibration_off())

			#If vibration sensor check in version6 is requested
            elif "version6_vibration_check" == sensor:
                response ='%s #version6_vibration_check %s' %(response,driver.readversion6_vibration_check())

			#If soil sensor on in version6 is requested
            elif "version6_soil_on" == sensor:
                response ='%s #version6_soil_on %s' %(response,driver.readversion6_soil_on())

			#If soil sensor off in version6 is requested
            elif "version6_soil_off" == sensor:
                response ='%s #version6_soil_off %s' %(response,driver.readversion6_soil_off())

			#If soilvalve sensor check in version6 is requested
            elif "version6_soil_check" == sensor:
                response ='%s #version6_soil_check %s' %(response,driver.readversion6_soil_check())





			#If light on in version7 is requested  
            elif "version7_light_on" == sensor:
                response ='%s #version7_light_on %s' %(response,driver.readversion7_light_on())

			#If light off in version7 is requested  
            elif "version7_light_off" == sensor:
                response ='%s #version7_light_off %s' %(response,driver.readversion7_light_off())

			#If light check in version7 is requested  
            elif "version7_light_check" == sensor:
                response ='%s #version7_light_check %s' %(response,driver.readversion7_light_check())

			#If fan on in version7 is requested 
            elif "version7_fan_on" == sensor:
                response ='%s #version7_fan_on %s' %(response,driver.readversion7_fan_on())

			#If fan off in version7 is requested 
            elif "version7_fan_off" == sensor:
                response ='%s #version7_fan_off %s' %(response,driver.readversion7_fan_off())

			#If fan check in version7 is requested 
            elif "version7_fan_check" == sensor:
                response ='%s #version7_fan_check %s' %(response,driver.readversion7_fan_check())

			#If automatic light on in version7 is requested 
            elif "version7_autolight_on" == sensor:
                response ='%s #version7_autolight_on %s' %(response,driver.readversion7_autolight_on())

			#If automatic light off in version7 is requested 
            elif "version7_autolight_off" == sensor:
                response ='%s #version7_autolight_off %s' %(response,driver.readversion7_autolight_off())

			#If automatic light check in version7 is requested 
            elif "version7_autolight_check" == sensor:
                response ='%s #version7_autolight_check %s' %(response,driver.readversion7_autolight_check())

			#If temp check in version7 is requested
            elif "version7_temp_check" == sensor:
                response ='%s #version7_temp_check %s' %(response,driver.readversion7_temp_check())

			#If humidity check in version7 is requested
            elif "version7_humid_check" == sensor:
                response ='%s #version7_humid_check %s' %(response,driver.readversion7_humid_check())

			#If pir sensor on in version7 is requested
            elif "version7_pir_on" == sensor:
                response ='%s #version7_pir_on %s' %(response,driver.readversion7_pir_on())

			#If pir sensor off in version7 is requested
            elif "version7_pir_off" == sensor:
                response ='%s #version7_pir_off %s' %(response,driver.readversion7_pir_off())

			#If pir sensor check in version7 is requested
            elif "version7_pir_check" == sensor:
                response ='%s #version7_pir_check %s' %(response,driver.readversion7_pir_check())
						
			#If smoke sensor on in version7 is requested
            elif "version7_smoke_on" == sensor:
                response ='%s #version7_smoke_on %s' %(response,driver.readversion7_smoke_on())

			#If smoke sensor off in version7 is requested
            elif "version7_smoke_off" == sensor:
                response ='%s #version7_smoke_off %s' %(response,driver.readversion7_smoke_off())

			#If smoke sensor check in version7 is requested
            elif "version7_smoke_check" == sensor:
                response ='%s #version7_smoke_check %s' %(response,driver.readversion7_smoke_check())

			#If vibration sensor on in version7 is requested
            elif "version7_vibration_on" == sensor:
                response ='%s #version6_vibration_on %s' %(response,driver.readversion7_vibration_on())

			#If vibration sensor off in version7 is requested
            elif "version7_vibration_off" == sensor:
                response ='%s #version7_vibration_off %s' %(response,driver.readversion7_vibration_off())

			#If vibration sensor check in version7 is requested
            elif "version7_vibration_check" == sensor:
                response ='%s #version7_vibration_check %s' %(response,driver.readversion7_vibration_check())

			#If door lock in version7 is requested
            elif "version7_door_lock" == sensor:
                response ='%s #version7_door_lock %s' %(response,driver.readversion7_door_lock())

			#If door unlock in version7 is requested
            elif "version7_door_unlock" == sensor:
                response ='%s #version7_door_unlock %s' %(response,driver.readversion7_door_unlock())

			#If door check in version7 is requested
            elif "version7_door_check" == sensor:
                response ='%s #version7_door_check %s' %(response,driver.readversion7_door_check())

			#If window check in version7 is requested
            elif "version7_window_check" == sensor:
                response ='%s #version7_window_check %s' %(response,driver.readversion7_window_check())




			#If light on in all versions is requested  
            elif "control_light_on" == sensor:
                response ='%s #control_light_on %s' %(response,driver.readcontrol_light_on())

			#If light off in all versions is requested  
            elif "control_light_off" == sensor:
                response ='%s #control_light_off %s' %(response,driver.readcontrol_light_off())

			#If automatic light on in all versions is requested 
            elif "control_autolight_on" == sensor:
                response ='%s #control_autolight_on %s' %(response,driver.readcontrol_autolight_on())

			#If automatic light off in all versions is requested 
            elif "control_autolight_off" == sensor:
                response ='%s #control_autolight_off %s' %(response,driver.readcontrol_autolight_off())

			#If fan on in all versions is requested 
            elif "control_fan_on" == sensor:
                response ='%s #control_fan_on %s' %(response,driver.readcontrol_fan_on())

			#If fan off in all versions is requested 
            elif "control_fan_off" == sensor:
                response ='%s #control_fan_off %s' %(response,driver.readcontrol_fan_off())

			#If pir sensor on in all versions is requested
            elif "control_pir_on" == sensor:
                response ='%s #control_pir_on %s' %(response,driver.readcontrol_pir_on())

			#If pir sensor off in all versions is requested
            elif "control_pir_off" == sensor:
                response ='%s #control_pir_off %s' %(response,driver.readcontrol_pir_off())

			#If smoke sensor on in all versions is requested
            elif "control_smoke_on" == sensor:
                response ='%s #control_smoke_on %s' %(response,driver.readcontrol_smoke_on())

			#If smoke sensor off in all versions is requested
            elif "control_smoke_off" == sensor:
                response ='%s #control_smoke_off %s' %(response,driver.readcontrol_smoke_off())




            #If AES key is requested
            elif "key" == sensor:
                if recipient not in aesKeys:
                    aeskey=""
                    #Generate AES Key
                    if cry.generateAES(driver.readTime()):
                        aeskey=cry.key
                        #Save AES key
                        aesKeys[recipient]=aeskey
                else:
                    aeskey=aesKeys[recipient]
                #AES key is encrypted by the recipient public key
                rep=myCrypto(recipient)
                encKey=rep.encryptRSA(b64encode(aeskey))
                response ='%s #key %s' %(response,encKey)

            #If photo is requested
            elif "photo" == sensor:
                cam=myCamDriver()
                cam.takePhoto()
                photo=cam.readPhotob64()

                response ='%s #photo ON @%s' %(response,recipient)
                self.sendDatagram(response)
                n = 256
                res=[photo[k:k+n] for k in xrange(0, len(photo),n)]
                for s in res:
                    response='DATA #photo %s @%s' %(s,recipient)
                    self.sendDatagram(response)
                response ='DATA #photo OFF'

            #If time is requested
            elif "time" == sensor:
                response ='%s #time %s' %(response,driver.readTime())

            #If date is requested
            elif "date" == sensor:
                response ='%s #date %s' %(response,driver.readDate())

            #If gps is requested
            elif "gps" == sensor:
                #if AES key is available, gps data will be encrypted
                gpsData='%s' %(driver.readGPS())
                if recipient in aesKeys:
                    rep=myCrypto(recipient)
                    rep.key=aesKeys[recipient]
                    gpsData=rep.encrypt(gpsData)
                response ='%s #gps %s' %(response,gpsData)
		

           #If gpio is requested
            elif "gpio" in sensor:
                m=re.search(r'\d+$',sensor)
                pinnumber=int(m.group())
                print pinnumber
                response ='%s #gpio%s %s' %(response,pinnumber,driver.readGPIO(port=pinnumber))

	
            else:
                response ='%s #%s NULL' %(response,sensor)
       
        response="%s @%s" %(response,recipient)
        self.sendDatagram(response)
        
	 
		


    #Handle the GPIO ports by calling the functions in the driver class
    def handlePUTSenze(self,sensors,data,recipient):
       response='DATA'
       driver=myDriver()
       cry=myCrypto(self.device)
       for sensor in sensors:
          #If GPIO operation is requested
          if "gpio" in sensor:
              pinnumber=0
              #search for gpio pin number
              m=re.search(r'\d+$',sensor)
              if m :
                 pinnumber=int(m.group())
            
              if pinnumber>0 and pinnumber<=16:
                 if data[sensor]=="ON":
                     ans=driver.handleON(port=pinnumber)
                 else:
                     ans=driver.handleOFF(port=pinnumber)
                 response='%s #gpio%s %s' %(response,pinnumber,ans)
              else: 
                 response='%s #gpio%d UnKnown' %(response,pinnumber)
          elif "time" in sensors:
              print "Received time :",data["time"]
          else:
              response='%s #%s UnKnown' %(response,sensor)
       print "******",response
       response="%s @%s" %(response,recipient)
       self.sendDatagram(response)


    def handleServerResponse(self,senz):
        data=senz.getData()
        sensors=senz.getSensors()
        cmd=senz.getCmd()
        print "-----------------"
        if cmd=="DATA":
           if 'msg' in sensors and 'UserRemoved' in data['msg']:
              cry=myCrypto(self.device)
              try:
                 os.remove(cry.pubKeyLoc)
                 os.remove(cry.privKeyLoc)
                 print "Device was successfully removed"
              except OSError:
                 print "Cannot remove user configuration files"

           elif 'pubkey' in sensors and data['pubkey']!="" and 'name' in sensors and data['name']!="":
                 recipient=myCrypto(data['name'])
                 if recipient.saveRSAPubKey(data['pubkey']):
                    print "Public key==> "+data['pubkey']+" Saved."
                 else:
                    print "Error: Saving the public key."


    def handleDeviceResponse(self,senz):
        sender=senz.getSender()
        data=senz.getData()
        sensors=senz.getSensors()
        cmd=senz.getCmd()
        print "---<<<<>>>>----------"
        global buf,aesKeys
        if cmd=="DATA":
            for sensor in sensors:
                print sensor+"==>"+data[sensor]
       
                if sensor=='photo':
                    if data['photo']=='ON':
                        buf=''	
                    elif data['photo']=='OFF':
                        cam=myCamDriver()
                        cam.savePhoto(buf,"photo.jpg")
                        #cam.showPhoto("photo.jpg")
                        thread.start_new_thread(cam.showPhoto,("photo.jpg",))
                        buf=''
                    else:
                        buf="%s%s" %(buf,data['photo'])

                #Received and saved the AES key
                elif sensor=='key' and data['key']!="":
                    #Key need to be decrypted by using the private key
                    cry=myCrypto(self.device)
                    dec=cry.decryptRSA(data['key'])
                    aesKeys[sender]=b64decode(dec)
                
                #Decrypt and show the gps data
                elif sensor=='gps' and data['gps']!="":
                    gpsData=data['gps']
                    if sender in aesKeys:
                        rep=myCrypto(sender)
                        rep.key=aesKeys[sender]
                        gpsData=rep.decrypt(gpsData)
                    print "** GPS=>"+gpsData


        elif cmd=="SHARE":
           print "This should be implemented"

        elif cmd=="UNSHAR":
           print "This should be implemented"

        elif cmd=="GET":
           #If GET Senze was received. The device must handle it.
           reactor.callLater(1,self.sendDataSenze,sensors=sensors,data=data,recipient=sender) 
        elif cmd=="PUT":
           reactor.callLater(1,self.handlePUTSenze,sensors=sensors,data=data,recipient=sender)
        else:
           print "Unknown command"
