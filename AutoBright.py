#    Copyright (C) 2013
#    Pranav Gupta, Harsh Gupta, Anil Kag, Sparsh Sinha, Himanshu Bansal

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------
#! /usr/env/python
import threading
import Image
import ImageStat
import cv
import time
import dbus
import sys
from PyQt4 import QtGui, QtCore
from screenAd import Ui_Manual

offset = 0
override_value  = 0
is_overridden = False
current_value = 0

threadLock = threading.Lock()

class form(QtGui.QMainWindow):
	def __init__(self,parent=None):
		global offset,override_value,is_overridden
	#	self.offset  = 0
	#	self.override_value = 0
	#	self.is_overridden = False
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Manual()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.ds,QtCore.SIGNAL("clicked()"),self.buttonclick)
		QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.startbuttonclick)
		
	def buttonclick(self):
		global offset,override_value,is_overridden,current_value
		override_value = self.ui.spinBox.value()
		offset = current_value - override_value
		is_overriden = True

	def startbuttonclick(self):
		global offset,override_value,is_overridden
		#override_value = self.adjust_brightness()


					
class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		

	def run(self):
		self.name
		# Get lock to synchronize threads
		threadLock.acquire()
		#print_time(self.name, self.counter, 3)
		# Free lock to release next thread
		self.adjust_brightness()
		threadLock.release()			

	#To reduce the frequent fluctuations, only cahge the value if the 
	#new value is more than PERSENT persent of the last set brightness
	def value_filter(self,avg,last_set):
		global offset,override_value,is_overridden
		PERSENT = 10

		if last_set == 0:
			return (avg/255)*100 + offset
		if abs(last_set - avg) < (last_set*(PERSENT)/100):
			return last_set + offset
		else:
			return (avg/255)*100 + offset

	def set_brightness_ubuntu(self,avg,last_set):
		global offset,override_value,is_overridden
		dbus_iface = 'org.gnome.SettingsDaemon.Power.Screen'
		bus_getObj_arg1 = 'org.gnome.SettingsDaemon'
		bus_getObj_arg2 = '/org/gnome/SettingsDaemon/Power'

		bus = dbus.SessionBus()
		proxy = bus.get_object(bus_getObj_arg1,bus_getObj_arg2)
		iface = dbus.Interface(proxy, dbus_interface=dbus_iface)

		value_to_set = self.value_filter(avg,last_set)

		try:
			iface.SetPercentage(value_to_set%100)
			#self.ui.spinBox.setValue(value_to_set)
			print "Set to ",value_to_set
		except:
			print "Error"

		return value_to_set

	def adjust_brightness(self):
		global offset,override_value,is_overridden,current_value
		image_file = "image.jpg"
		sleep_time_in_sec = 2

		#Getting capture object corresponding to webcam
		t = cv.CaptureFromCAM (0)
		value_to_set = 0
		while(1):

			if not is_overridden :
				while(1):
						if(cv.GrabFrame(t)):
								f = cv.QueryFrame (t)
								cv.SaveImage (image_file, f)
								break;
				image = cv.LoadImage(image_file);
				mat = cv.GetMat(image)
				sum_mat = 0
				count = 0
	
				for i in range(0,mat.rows/10):
					for j in range(0,mat.cols):
						(a,b,c) = mat[i,j]
						avg_tuple = (a+b+c)/3
						sum_mat += avg_tuple
						count += 1

				for i in range(mat.rows/10,mat.rows/2):
					for j in range(0,mat.cols/10):
						(a,b,c) = mat[i,j]
						avg_tuple = (a+b+c)/3
						sum_mat += avg_tuple
						count += 1

				for i in range(0,mat.rows/10):
					for j in range(mat.cols*9/10,mat.cols):
						(a,b,c) = mat[i,j]
						avg_tuple = (a+b+c)/3
						sum_mat += avg_tuple
						count += 1
		
		
				avg = sum_mat/count
				value_to_set = self.set_brightness_ubuntu(avg,value_to_set)
				current_value = value_to_set
			else:
				value_to_set = self.set_brightness_ubuntu(avg,value_to_set+offset)
				current_value = value_to_set
			time.sleep(sleep_time_in_sec)
	
			
if __name__=="__main__":
	
	thread1 = myThread(1,"Thread 1",1)
	thread1.start()
	
	app = QtGui.QApplication(sys.argv)
	f1 = form()
	f1.show()
	#f1.adjust_brightness()
	sys.exit(app.exec_())
	

