from tkinter import *
import tkinter.font as tkFont
from Scraper import data_scraper
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('GUI')
        self.pack()
        self.create_widgets()
        self.images()
    def create_widgets(self):
        self.fontstyle = tkFont.Font(family = 'times',size=30)
        self.label = Label(self, justify = CENTER, padx = 10, pady=10, bg = "black", fg = "Yellow", text = "Type in an item", font = self.fontstyle).pack(side="top",fill = X)
        self.entry = Entry(self,width=180)
        self.entry.pack(side = 'left',pady=10)
        
        self.send = Button(self,text = 'send',command = lambda:self.sendbody(None))#Fake event parameter
        self.send.pack(side="left",pady=10)
        self.quit = Button(self, text="QUIT", fg="red", command = self.master.destroy)
        self.quit.pack(side="right",pady=10)
        root.bind("<Return>", self.sendbody)
        self.canvas = Canvas(root, width = 1000, height = 220)
        self.canvas.pack(side = 'bottom', fill = X)
        
    def sendbody(self,event):
    
        self.values = self.entry.get()
        self.ID = self.get_ID(self.values)
        self.dataobj = data_scraper(self.ID)
        self.dynamiclabel = displaylabel(self,self.dataobj.pricedata[0])
        self.dynamiclabel.pack()
        
        return self.dataobj
        
    def get_ID(self,value):
        with open('tradeableitems.txt','r') as file:
            for row in file:
                if row.split(',')[1].replace('\n','').lower().strip() == value:
                    _ID = row.split(',')[0]
                    return _ID
                    
    #def display_label(self,text):
        #text = f"{text[1]} is currently worth {text[0] GP}"
        #self.dynamiclabel = Label(,padx=10,pady=10,bg="black",fg = "Yellow",text = text)
        #self.dynamiclabel.pack(side = "bottom")

    def images(self):
    
        self.img = PhotoImage(file = "connectlost.gif")
        self.canvas.create_image(1000,100,anchor = E ,image = self.img)

class displaylabel(Frame):

    def __init__(self, master, display_data):
    
        Frame.__init__(self)
        self.master = master
        
        self.text = f"{display_data[1]} is currently worth {display_data[0]} GP"
        self.dynamiclabel = Label(self, padx=10, pady=10, bg="black", fg = "Yellow", text = self.text, font = tkFont.Font(family = 'times',size = 35))
        self.dynamiclabel.pack(side = "top")        
        
if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.minsize(width = '1000',height = '750')
    app.mainloop()