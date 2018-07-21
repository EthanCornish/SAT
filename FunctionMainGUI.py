from tkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title('Flash Card')

        self.FmePage1ViewSet = Frame(master)
        self.FmePage1ViewSet.grid(column=0, row=0, columnspan=3)

        # Widget 1
        self.LblSet = Label(self.FmePage1ViewSet, text='setName', bg='orange')
        self.LblSet.grid(row=0, column=0, rowspan=1, columnspan=3)

        # Widget 2
        self.FmeTableView = Frame(self.FmePage1ViewSet, bg='grey')
        self.FmeTableView.grid(row=2, column=1)

        #self.border = []
        #for i in range(0,21):
        #    for j in range(0,7):
        #        if not (i % 2) or not (j % 2):
        #            print('i =', i)
        #            self.lblTest = Label(self.FmeTableView, text='.', width=5,height=1, bg='blue', fg='blue')
        #            self.lblTest.grid(row=i,column=j)
        #            self.border.append(self.lblTest)
        #        if not (j % 2):
        #            self.lblTest = Label(self.FmeTableView, text='.', width=3, height=1, bg='red', fg='red')
        #            self.lblTest.grid(row=i, column=j)
        #            self.border.append(self.lblTest)
        #
        #        self.LblTermHeader = Label(self.FmeTableView, text='Term', width=15, height=1)
        #        self.LblTermHeader.grid(row=1, column=1)

        # Widget 3
        self.BtnCreate = Button(self.FmePage1ViewSet, text='Create Set')
        self.BtnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)

        # Widget 4
        self.MbSelect = Menubutton(self.FmePage1ViewSet, text='Select Set')
        self.MbSelect.grid(row=2, column=5, rowspan=1, columnspan=3)

        # Widget 5
        self.FmeOptions = Frame(self.FmePage1ViewSet, bg='Blue')
        self.FmeOptions.grid(row=3,column=5,rowspan=3,columnspan=4)

        # Widget 6
        self.BtnView = Button(self.FmePage1ViewSet, text='View Set')
        self.BtnView.grid(row=5, column=5, rowspan=1, columnspan=3)

        # Widget 7
        self.BtnDelete = Button(self.FmePage1ViewSet, text='Delete Set')
        self.BtnDelete.grid(row=10, column=5, rowspan=1, columnspan=1)

        # Widget 8
        self.BtnHelp = Button(self.FmePage1ViewSet, text='Help', bg='blue')
        self.BtnHelp.grid(row=10, column=8, rowspan=1, columnspan=1)

        # Blank Spaces

        blanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 11], [1, 11], [0, 1, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
         [1, 7, 9, 11], [1, 7, 9, 10, 11], [1, 7, 9, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
        countBlank = 0
        print('(column, row)')
        while countBlank < 9:
            for i in blanks[countBlank]:
                print(countBlank, ',', i)
                self.LblBlank = Label(self.FmePage1ViewSet, height='1', width='10', bg='green', text='abc')
                self.LblBlank.grid(row=i, column=countBlank)
            countBlank += 1
            print('\n')



root = Tk()
root.geometry('800x600')
my_gui = GUI(root)
root.mainloop()


