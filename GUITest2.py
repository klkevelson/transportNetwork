from tkinter import *
import tkinter as Tk
import time
global StartTown
class InputWindow:
	
	def __init__(self):
		
	
		Label(root, text="Enter Starting Town").grid(row=0)
		Label(root, text="Enter Ending Town").grid(row=1)
		entry1 = Entry(root)
		entrt2 = Entry(root)
		entrt1.grid(row=0, column=1)
		entrt2.grid(row=1, column=1)
		##StartTown = entrt1.get()
		EndTown = entrt2.get()
		button3 = Button(root, text = "OK", command = getTown(entrt1.get()).grid(row=3, column=0))
	
	def getTown():
		StartTown = entrt1.get()
		return StartTown
	
class OutputWindow:

	def __init__(self):
		Window1 = Tk()
		
		 		
		button1 = Button(Window1, text = "See Animation", command = loadImage)
		button1.pack()		
	##	button2 = Button(Window1, text = "See Entry", command = loadWindow)
	##	button2.pack()
		listbox = Listbox(Window1)
		listbox.pack()
		listbox.insert(END, "List of Towns")
		##StartTown1 = myWin.getTown(StartTown)
		listbox.insert(END, StartTown)
		
	def loadImage():
		canvas = Canvas(Window1, width=300, height=300)
		canvas.pack()
		canvas.create_polygon(10,10,10,60,50,35)
		for i in range(0,60):
			canvas.move(1,5,0)
			root.update()
			time.sleep(0.1)
	
		
		
	
root = Tk()	
app = InputWindow()
app.mainloop()
	
