from tkinter import *


class ConversionGUI:
    def __init__(self, master):
        self.master = master
        master.title('Image Testing')

        self.image = PhotoImage(file='/Users/19ecornish/Downloads/IMG_5024.gif')

        self.ImageLabel = Label(master, image=self.image, width=40, height=30)
        self.ImageLabel.grid()


root = Tk()
root.geometry('600x400')
gui = ConversionGUI(root)
root.mainloop()