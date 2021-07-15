conram=0
def edit(text):
	print(text)
def data(text):
	input(text)
def Calculator(text,textouput):
	try:
		b2=eval(text)
		print(textouput+str(b2))
	except:
		raise SyntaxError
def wait(number):
	import time
	time.sleep(number)
def command(text):
	import os
	os.system(text)
def dfcl():
	import os
	clear=lambda: os.system('cls')
def gtM():
	import pyautogui
	x,y=pyautogui.position()
def random(s,s1):
	from random import randint
	randint(int(s),int(s1))
def function(path,name):
	import os
	os.chdir(path)
	os.system(name)
def ow_input(python_version,text):
	if python_version=="3":
		input(text)
	if python_version=="2":
		raw_input(text)
def Playsound(name):
	from playsound import playsound
	playsound(name)
def oz_input(text):
	try:
		input(text)
	except:
		raw_input(text)
def output(text):
	print(text)
def PyCodeText(mode,text):
	from rich.console import Console
	console = Console()
	console.print("["+mode+"]"+text+"["+mode+"]")
def emty():
	pass
def PyCodeMesage(title,text,mode):
	import ctypes
	ctypes.windll.user32.MessageBoxW(0, text, title, mode)
def install(module):
	try:
		import os
		os.system('pip install '+module)
	except:
		raise SyntaxError
def listmodule():
	try:
		import os
		os.system('pip list')
	except:
		raise SyntaxError
def error(error):
	raise error
def speech(text):
	try:
		import pyttsx3
		import speech_recognition
		from datetime import date
		import datetime

		bot_brain = text
		bot_mouth = pyttsx3.init()
		bot_mouth.say(bot_brain)
		bot_mouth.runAndWait()
	except:
		print("Please install pyttsx3,speech_recognition")
def cpath(path):
	import os
	os.chdir(path)
def mouse_controls(mode,x,y):
	import pyautogui
	if mode=="move":	
		pyautogui.moveTo(x,y)
	if mode=="rightclick":
		pyautogui.click(button='right')
	if mode=="leftclick":
		pyautogui.click(button='left')
	if mode=="clickXY":
		pyautogui.click(x,y)
def key_controls(key):
	import pyautogui
	pyautogui.press(key)
def text_controls(text):
	import pyautogui
	pyautogui.typewrite(text)
def autoclick():
	from AutoClick import AutoClick
	AutoClick()
def time():
	from datetime import date

	today = date.today()

	# dd/mm/YY
	d1 = today.strftime("%d/%m/%Y")
	print(d1)
def time2():
	# Textual month, day and year	
	d2 = today.strftime("%B %d, %Y")
	print(d2)
def time3():
	# mm/dd/y
	d3 = today.strftime("%m/%d/%y")
	print(d3)
def time4():
	# Month abbreviation, day and year	
	d4 = today.strftime("%b-%d-%Y")
	print(d4)
def battery():
	import psutil
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	plugged = "Plugged In" if plugged else "Not Plugged In"
	print(percent+'% | '+plugged)
def unicode_pt(text):
	print(ord(text))
def run(app):
	import os
	os.system('start /wait '+app)
def Mouse_skin(image_cursor):
	import win32api
	import time
	import win32gui
	import win32con
	import ctypes


	hold = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 
	                          0, 0, win32con.LR_SHARED )
	hsave = ctypes.windll.user32.CopyImage(hold, win32con.IMAGE_CURSOR, 
	                                       0, 0, win32con.LR_COPYFROMRESOURCE)
	hcursor = win32gui.LoadImage(0, image_cursor, 
	                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
	ctypes.windll.user32.SetSystemCursor(hcursor, 32512)
from tkinter import *
from tkinter import Frame
def PyCodeScreen(self,title,size,fm,cover):
	import tkinter as tk
	self.title(title)
	self.geometry(size)
	if cover==True:
		self.attributes('-fullscreen', True)
	else:
		self.attributes('-fullscreen',False)
	if fm==False:
		self.resizable(width=False,height=False)
	if fm==True:
		pass
def show(self):
	self.mainloop()
def LB(Frame,text,x,y):
	labelPanterRoot=Label(Frame,text=text).place(x=x,y=y)
def icon(self,file):
	self.iconbitmap(file)
def tbox(self,width,font,variable,x,y):
	Box = Entry(self,width = width,font =font,textvariable=variable).place(x=x,y=y)
class Ex32(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("Gn.gif")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
def background_colors(Frame,color):
	Frame.configure(color)
def open_fs(self):
	import webbrowser
	webbrowser.open(self)
def exe(file,mode):
	import os
	os.system('pyinstaller '+mode+" "+file)
def auto_py_to_exe():
	import os
	os.system('auto-py-to-exe')
def recoreder(filename,duration):
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio as wv 
    freq = 44100
      
    duration = int(duration)
    recording = sd.rec(int(duration * freq), 
                       samplerate=freq, channels=2)
      
    sd.wait()
      
    wv.write(filename, recording, freq, sampwidth=2)
def dels(file):
	import os
	os.remove(file)
def Cr_folder(folder):
	import os
	os.mkdir(folder)
def Del_folder(folder):
	import os
		
	try:
		os.rmdir(folder)
		print("Compelete!")
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror))
def Dek_folder(folder):
	import os
	import sys
	import shutil
	# Get directory name


	## Try to remove tree; if failed show an error using try...except on screen
	try:
		shutil.rmtree(folder)
		print("Compelete!")
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror))
def Dels_file(file):
	import os

	## If file exists, delete it ##
	if os.path.isfile(file):
		os.remove(file)
		print("Compelete!")
	else:    ## Show an error ##
		print("Error: %s file not found" % file)	
def Sc_pt(repair_time,filename):
	import time
	import imutils
	import pyautogui
	import cv2
	import ctypes
	# Another Type
	ctypes.windll.user32.MessageBoxW(0, "Click Ok to start", "Info",0)
	pyautogui.screenshot(filename)
	# we can then load our screenshot from disk in OpenCV format
	image = cv2.imread(filename)
	cv2.imshow("Photo", imutils.resize(image, width=1000))
	cv2.waitKey(0)
def exit():
	import sys
	sys.exit()
