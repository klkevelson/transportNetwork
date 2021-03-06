from tkinter import*
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
import time

class Application(Frame):
      
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.centerWindow()
        self.createWidgets()
        self.user_list = []
        self.lat = 0
        self.long = 0
        
    
    def centerWindow(self):
        '''
        Center a 800 x 600 frame
        '''
        frame_width = 800
        frame_height = 600    
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        frame_xpos = (screen_width - frame_width)/2
        frame_ypos = (screen_height - frame_height)/2
        self.master.geometry('%dx%d+%d+%d' % (frame_width, frame_height, frame_xpos, frame_ypos))
    
    def createWidgets(self):
        
        label_values = ["Enter Person's Name", "Enter Starting Town", "Enter Ending Town", 
                         "Choose Transportation", "Valid Transportation includes: Bus, Train, or Car"]
        button_values = ["Add Person", "Quit", "Graph"]
          
        self.createGroups(Label, label_values, 0, 0)      
        self.entries = self.createEntries(4, 1)
        self.buttons = self.createGroups(Button, button_values, 5, 0)
        
        #Add any button bindings or commands
        self.buttons[0].bind("<Button-1>", lambda e: self.displayEntries(self.entries))
        self.buttons[1]["command"]= self.quit
        self.buttons[2].bind("<Button-1>", lambda e: self.loadRoute(self.lon, self.lat))
        

        
    def displayEntries(self, entries):
        self.window = Toplevel(self)
        self.window.geometry('%dx%d+%d+%d' % (300, 200, 0, 0))
        self.geolocator = Nominatim()
        self.start_town = entries[1].get()
        self.location = self.geolocator.geocode(self.start_town)
        self.user_entries = [entry.get() for entry in entries]
        self.user_entries.append(self.location.raw)
        self.lon, self.lat = self.location.raw["lon"], self.location.raw["lat"]

 
        if(len(self.user_list) == 0):
            self.user_list.append(self.user_entries)
            self.window.list = Listbox(self.window)
            for entry in self.user_entries:
                self.window.list.insert(END, entry)
            self.window.list.grid(row=8)
        else:
            self.user_list.append(self.user_entries)
            self.window.list = Listbox(self.window)
            self.temp_list = []
            list_size = 0
            for sublist in self.user_list:
                for item in sublist:
                    self.window.list.insert(END, item)
                    list_size += 1
            self.window.list.grid(row=list_size)
            
            
    def loadMap(self, lon, lat):
        self.load = Image.open("Map.png")
        self.width, self.height = self.load.size 
        self.window = Toplevel(self)
        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, 0, 0))
        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        self.render = ImageTk.PhotoImage(self.load)
        self.image = self.canvas.create_image(self.width, self.height, anchor="se", image=self.render)
        self.poly = self.canvas.create_polygon(lat,lon,10,60,50,35)
        self.window.update()
        for i in range(0,60):
            self.canvas.move(self.poly,0,1)
            self.window.update()
            time.sleep(0.1)
        
    def loadImage(self):
        pass
        
    def loadRoute(self, lon, lat):
        self.loadMap(lon, lat)
        self.loadImage()        
    
    def createGroups(self, tk_type, text_array, row, col):  
        self.item_list = [] 
        for label in text_array:
            self.item = tk_type(self, text=label)
            self.item.grid(row=row, column=col)
            self.item_list.append(self.item)
            row += 1
        return self.item_list
    
    def createEntries(self, amount, col):
        self.entry_list = []
        for i in range(amount):
            self.entry = Entry(self)
            self.entry.grid(row=i, column=col)
            self.entry_list.append(self.entry)
        return self.entry_list           
        
app = Application()       
app.mainloop()