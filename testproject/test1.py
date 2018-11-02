#!python

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import accelerometer
import socket
#import time
# integrating client to app
#testing latency
#import datetime
#import module
lst = []
class AppLayout(BoxLayout):
	def __init__(self):
		super(AppLayout,self).__init__()
		self.sensor_status = True
		self.conn_status = True
		self.host = ''
		self.port = 9999
		#create file to test latency
		self.fh = open(r'/storage/emulated/0/logclient.txt','a')

	def connect_button(self):
		if self.conn_status:
			self.host = str(self.ids.hostname.text)
			try:
				self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				try:
					self.client_socket.connect((self.host,self.port))
					self.ids.client_status.text = 'Now you can Start Sending Data'
					self.ids.togglebutton.text = 'start Sending'
					self.conn_status = False
					self.ids.server_button.text = 'Close SOcket'
				except:
					self.ids.client_status.text = 'Connection Failed'

			except :
				self.ids.client_status.text = 'Server is NOt up!!'

		else:
			#self.ids.client_status.text = 'Error Creating Socket'
			self.client_socket.close()
			self.conn_status = True
			self.ids.server_button.text = 'Create Socket'
			self.ids.client_status.text = 'Welcome'

	def do_toggle(self):
		if self.sensor_status:
			try:
				accelerometer.enable()
				#increase the value of denominator to get more accurate /real time values
				Clock.schedule_interval(self.get_acceleration,1.0/3)
				self.sensor_status = False
				self.ids.togglebutton.text = 'Stop'
				self.ids.value.text = 'Sending data to host'
			except:
				self.ids.value.text = 'Try Again Later'
		else:
		  self.sensor_status = True
		  self.ids.togglebutton.text = 'Start'
		  self.ids.value.text = 'start again'
		  accelerometer.disable()
		  Clock.unschedule(self.get_acceleration)
		  self.fh.close()
	def get_acceleration(self,dt):
		#add time stamp to sending data to test latency
		txt: ''
		dt = datetime.datetime.now()
		try:
			txt = str(accelerometer.acceleration[0])

		except:
			txt = 'Failed'
		self.client_socket.send(txt.encode())
		#self.fh.write(txt+'-'+str(dt.minute)+':'+str(dt.second)+'\n')

class AccelerometerApp(App):
	def build(self):
		return AppLayout()
if __name__=="__main__":
	AccelerometerApp().run()
