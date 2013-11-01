#from Tkinter import Tk, Frame, Menu
from Tkinter import Frame, Tk, BOTH, Text, Menu, END, Label, LEFT, Entry, Button
  
import tkFileDialog, tkMessageBox

import MySQLdb

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Simple menu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        

    def onExit(self):
        self.quit()

class Example2(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Submenu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)       
        
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)        
                

    def onExit(self):
        self.quit()
        
class Example3(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        
        
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):
      
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

class Example4(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent        
        self.initUI()

    def initUI(self):
      
        self.parent.title("Tkinter Entry Widget")
        
        self.parent["padx"] = 40
        self.parent["pady"] = 20   

        #Create a Label in textFrame
        self.entryLabel = Label(self.parent)
        self.entryLabel["text"] = "Artist:"
        self.entryLabel.pack(side=LEFT)

        # Create an Entry Widget in textFrame
        self.entryWidget = Entry(self.parent)
        self.entryWidget["width"] = 50
        self.entryWidget.pack(side=LEFT)

        self.txt = Text(self)

        self.pack()

        button1 = Button(self.parent, text="Submit1", command=self.displayText)
        button1.pack()

    def displayText(self):
        """ Display the Entry text value. """

        if self.entryWidget.get().strip() == "":
            tkMessageBox.showerror("Tkinter Entry Widget", "Enter a text value")
        else:
            tkMessageBox.showinfo("Tkinter Entry Widget", "Searching for artist =" \
                + self.entryWidget.get().strip())
            self.test3()

    def test3(self):
       search = "select artist, count(*) as countit from songs " \
           +  "where artist = " + '"' +self.entryWidget.get().strip()+ '"'
       self.txt.pack(fill=BOTH, expand=1)
        
       conn = MySQLdb.connect (host = "localhost",
                           user = "cs126",
                           passwd = "cs126",
                           db = "music")
       cursor = conn.cursor ()
       cursor.execute ( search )
                   
       row = cursor.fetchone ()
       while row != None:
          text =  "Songs: "
          for i in row:
              text = text + " " +str(i)
          text = text + '\n'
          self.txt.insert(END, text)
          row = cursor.fetchone ()
       cursor.close ()
       conn.close ()
     
def runit():
    root = Tk()
    app = Example4(root)
    root.mainloop()  
