from tkinter import*
from PIL import Image, ImageTk
import time

root = Tk()
global StartTown 

def drawList():	
	StartTown = "Rye"
	listbox = Listbox(root)
	
	listbox.insert(END, "List of Towns")
	listbox.insert(1, StartTown)
	listbox.insert(2, "Hoboken")
	listbox.insert(3, "Staten Island")
	listbox.insert(4, "Bronx")
	listbox.insert(5, "Scarsdale")
	listbox.pack()
	
def loadWindow():
	Window = Tk()
	
	Label(Window, text="Enter Starting Town").grid(row=0)
	Label(Window, text="Enter Ending Town").grid(row=1)
	
	StartingTown = e1 = Entry(Window)
	e2 = Entry(Window)
	e3 = Entry(Window)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	StartTown = e1.get()
	EndTown = e2.get()
	button4 = Button(Window, text = "OK", command = drawList).grid(row=3, column=0)
	button4.pack()
	
	

	
	
	

def loadImage():
	canvas = Canvas(root, width=300, height=300)
	canvas.pack()
	canvas.create_polygon(10,10,10,60,50,35)
	for i in range(0,60):
		canvas.move(1,5,0)
		root.update()
		time.sleep(0.1)
def loadMap():
	
	canvas = Canvas(root, width=300, height=300)
	
	
	load = Image.open("Map.png")
	render = ImageTk.PhotoImage(load)
	img = Label(root, image=render)
	img.image = render
	img.place(x=0,y=0)
	canvas.create_polygon(10,10,10,60,50,35)  
	canvas.pack()
	for i in range(0,60):
		
		canvas.move(2,5,0)
		root.update()
		time.sleep(0.1)
				
		
def GetCarbon():
	listbox = Listbox(root)
	
	listbox.insert(END, "List of Towns")
	listbox.insert(1, "Rye       Bike               0")
	listbox.insert(1, "Rye       Automobile   35 kg/s")
	listbox.insert(1, "Rye       Bus          12 kg/s")
	listbox.insert(2, "Hoboken   Automobile   35 kg/s")
	listbox.insert(2, "Hoboken   Bike         0 kg/s")
	listbox.insert(2, "Hoboken   Bus          12 kg/s")
	listbox.insert(3, "Staten Island")
	listbox.insert(4, "Bronx")
	listbox.insert(5, "Scarsdale")
	listbox.pack()
		
def loadRoute():
	loadMap()
	loadImage()
	

	
		
button1 = Button(root, text = "See Current Travel Route", command = loadImage)
button1.pack()		
button2 = Button(root, text = "See Entry", command = loadWindow)
button2.pack()

button3 = Button(root, text = "View Map", command = loadMap)
button3.pack()
button4 = Button(root, text = "View Both", command = loadRoute)
button4.pack()
button5 = Button(root, text = "Get Carbon Footprint", command = GetCarbon)
button5.pack()
root.mainloop()