###Brooklyn to Morristown

import tkinter as Tk
from PIL import Image, ImageTk
import time

Window = Tk.Tk()


###This is calculated by determining the emissions per mile, the average trip speed(usually 60mph,) a little unit conversion, and a 20% weighting factor(1.2) for additional CO2 emissions as car ages(assume vehicle is 5 years old)

label1 = Tk.Label(Window, text = "Carbon Footprint = 16.6 kg/s")
label1.pack()

canvas = Tk.Canvas(Window)
background_image=Tk.PhotoImage(file="Map.png")
canvas.pack(fill=Tk.BOTH, expand=1)
image = canvas.create_image(0,0, anchor=Tk.NW, image=background_image)
line = canvas.create_line(10,10,100,35,fill="blue")
canvas.create_polygon(270,160,260,160,250,130)  ###These are the coordinates for Brooklyn



for i in range(0,15):
		canvas.move(3,-5,2)
		Window.update()
		time.sleep(0.1)
		
for i in range(0,5):
		
		canvas.move(3,-5,-5)  ###This is another line that you need to experiment with to get the travel route correct
		Window.update()
		time.sleep(0.1)
		
for i in range(0,10):
		
		canvas.move(3,-5,0)  ###This is another line that you need to experiment with to get the travel route correct
		Window.update()
		time.sleep(0.1)
		
for i in range(0,11):
		
		canvas.move(3,-5,-6)   ###This is another line that you need to experiment with to get the travel route correct
		Window.update()
		time.sleep(0.1)
Window.wm_geometry("794x370")
Window.title('Map')
Window.mainloop()