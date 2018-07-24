from tkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title('Flash Card')

        self.FmePage1ViewSet = Frame(master)
        self.FmePage1ViewSet.grid(column=0, row=0, columnspan=3)

        # Widget 1
        self.LblSet = Label(self.FmePage1ViewSet, text='setName', bg='orange', width=32)
        self.LblSet.config(font=('Arial', 32, 'bold underline'))
        self.LblSet.grid(row=0, column=0, rowspan=1, columnspan=4)

        # Widget 2

        # Creating the Frame
        self.FmeTableView = Frame(self.FmePage1ViewSet)
        # Grid line is below as it uses a variable to determine rowspan
        #   self.FmeTableView.grid(row=2, column=1, rowspan=self.noCards, columnspan=3)

        # Header for 'Term' Column
        self.LblTermHeader = Label(self.FmeTableView, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Header for 'Definition' Column
        self.LblDefHeader = Label(self.FmeTableView, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Header for 'Image' Column
        self.LblImgHeader = Label(self.FmeTableView, text='Image', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 18, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)

        # Setting the content for the 'Term' Column
        self.terms = ['term1', 'term2', 'term3', 'term4', 'term5', 'term6', 'term7', 'term8', 'term9']

        # Defining a temporary variable to store the number of card for determining table size
        self.noCards = (len(self.terms)*2)+3

        self.FmeTableView.grid(row=2, column=1, rowspan=(len(self.terms)*3)+(len(self.terms))+3, columnspan=3)

        count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.LblTerm = Label(self.FmeTableView, text=self.terms[count], anchor='w', width=12, height=3)
                self.LblTerm.config(font=('Times', 14))
                self.LblTerm.grid(row=i, column=1)
                count += 1

        # Setting the content for the 'Definition' Column
        self.terms = ['def1', 'def2', 'def3', 'def4', 'def5', 'def6', 'def7', 'def8', 'def9']
        count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.LblDef = Label(self.FmeTableView, text=self.terms[count], anchor='w', width=22, height=3)
                self.LblDef.config(font=('Times', 14))
                self.LblDef.grid(row=i, column=3)
                count += 1

        # Setting the content for the 'Image' Column
        self.terms = ['img1', 'img2', 'img3', 'img4', 'img5', 'Img6', 'img7', 'img8', 'img9']
        count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.LblImg = Label(self.FmeTableView, text=self.terms[count], anchor='w', width=12, height=3)
                self.LblImg.config(font=('Times', 14))
                self.LblImg.grid(row=i, column=5)
                count += 1

        # Setting border around table
        self.border = []
        for i in range(0, self.noCards):
            for j in range(0,7):
                # Even row and column = 0, 2, 4, 6 (even)
                if (i % 2) == 0 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i,column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (term)
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 3 (def)
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableView, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (img)
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

        # Widget 3
        self.BtnCreate = Button(self.FmePage1ViewSet, text='Create Set', width=24)
        self.BtnCreate.config(font=('Times', 16))
        self.BtnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)

        # Widget 4
        self.VarEditSaveBtnText = StringVar()
        self.VarEditSaveBtnText.set('View')
        self.VarEditSaveBtnBool = IntVar()
        self.BtnEditSave = Button(self.FmePage1ViewSet, textvariable=self.VarEditSaveBtnText, width=24, command=self.EditSaveBtn)
        self.BtnEditSave.config(font=('Times', 16))
        self.BtnEditSave.grid(row=2, column=5, rowspan=1, columnspan=3)


        # Widget 5

        # The header
        self.MbSelect = Menubutton(self.FmePage1ViewSet, text='Select Set', width=24)
        self.MbSelect.config(font=('Times', 16))
        self.MbSelect.grid(row=3, column=5, rowspan=1, columnspan=3)

        # Options
        self.MbOption1 = Menu(self.MbSelect)#, text='Option 1', command=self.MenuCommand)
        self.MbOption1Lbl = StringVar()
        self.MbOption1Lbl.set('Option1')
        self.MbOption1.add_command(label='Option1', command=self.MenuCommand)


        # Widget 6

        # Creating the Frame
        self.FmeOptions = Frame(self.FmePage1ViewSet)
        self.FmeOptions.grid(row=4, column=5, columnspan=3, rowspan=5)

        # Default Side

        # Default side label
        self.LblDefaultSide = Label(self.FmeOptions, text='Default Side:', anchor=W)
        self.LblDefaultSide.config(font=('Times', 16))
        self.LblDefaultSide.grid(row=0, column=0)

        # Variable for default side
        self.VarDefaultSideInput = IntVar()

        self.VarDefaultSideInput = 3

        # Radio Buttons for default side
        self.RbDefaultSideTerm = Radiobutton(self.FmeOptions, text='Term', variable=self.VarDefaultSideInput, value=1, anchor=W, width=8)
        self.RbDefaultSideTerm.config(font=('Times', 14))
        self.RbDefaultSideDef = Radiobutton(self.FmeOptions, text='Definition', variable=self.VarDefaultSideInput, value=2, anchor=W, width=10)
        self.RbDefaultSideDef.config(font=('Times', 14))
        self.RbDefaultSideImg = Radiobutton(self.FmeOptions, text='Image', variable=self.VarDefaultSideInput, value=3, anchor=W, width=7)
        self.RbDefaultSideImg.config(font=('Times', 14))

        # Setting 'Term' as the default option
        self.RbDefaultSideTerm.select()

        self.RbDefaultSideTerm.grid(row=1, column=0)
        self.RbDefaultSideDef.grid(row=1,column=1)
        self.RbDefaultSideImg.grid(row=1,column=2)

        # View Full/Star

        # View Full/Star Label
        self.LblViewFullStar = Label(self.FmeOptions, text='View:', anchor=W, width=8)
        self.LblViewFullStar.config(font=('Times', 16))
        self.LblViewFullStar.grid(row=2,column=0)

        # Variable for ViewFullStar
        self.VarViewFullStarInput = IntVar()

        # Radio Buttons for ViewFullStar
        self.RbViewFull = Radiobutton(self.FmeOptions, text='Full Set', variable=self.VarViewFullStarInput, value=1, width=8, anchor=W)
        self.RbViewFull.config(font=('Times', 14))
        self.RbViewStar = Radiobutton(self.FmeOptions, text='Starred Cards Only', variable=self.VarViewFullStarInput, value=16, anchor=W)
        self.RbViewStar.config(font=('Times', 14))

        # Setting 'Full' as the default option
        self.RbViewFull.select()

        self.RbViewFull.grid(row=3,column=0)
        self.RbViewStar.grid(row=3,column=1, columnspan=2)

        # Card Order

        # Card Order Label
        self.LblCardOrder = Label(self.FmeOptions, text='Card Order:', anchor=W)
        self.LblCardOrder.config(font=('Times', 16))
        self.LblCardOrder.grid(row=4,column=0)

        # Variable for Card Order
        self.VarCardOrderInput = IntVar()

        # Radio Buttons for Card Order
        self.RbCardOrderOrg = Radiobutton(self.FmeOptions, text='Original', variable=self.VarCardOrderInput, value=1, anchor=W)
        self.RbCardOrderOrg.config(font=('Times', 14))
        self.RbCardOrderRnd = Radiobutton(self.FmeOptions, text='Random', variable=self.VarCardOrderInput, value=2, anchor=W)
        self.RbCardOrderRnd.config(font=('Times', 14))

        # Setting 'Original' as the default option
        self.RbCardOrderOrg.select()

        self.RbCardOrderOrg.grid(row=5, column=0)
        self.RbCardOrderRnd.grid(row=5,column=1)

        # Widget 7
        self.BtnView = Button(self.FmePage1ViewSet, text='View Set', width=24)
        self.BtnView.config(font=('Times', 16))
        self.BtnView.grid(row=9, column=5, rowspan=1, columnspan=3)

        # Widget 8
        self.BtnDelete = Button(self.FmePage1ViewSet, text='Delete Set')
        self.BtnView.config(font=('Times', 16))
        self.BtnDelete.grid(row=11, column=5, rowspan=1)

        # Widget 9
        self.BtnHelp = Button(self.FmePage1ViewSet, text='Help', width=8)
        self.BtnHelp.config(font=('Times', 16))
        self.BtnHelp.grid(row=11, column=7, rowspan=1)

        # Blank Spaces

        blanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
         [1, 10], [1, 11], [1, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
        self.countBlank = 0
        while self.countBlank < 9:
            for i in blanks[self.countBlank]:
                self.LblBlank = Label(self.FmePage1ViewSet, height=1, width=8, bg='green', text='abc')
                self.LblBlank.config(font=('Arial', 10))
                # self.LblBlank = Label(self.FmePage1ViewSet, height=1, width=8)
                self.LblBlank.grid(row=i, column=self.countBlank)
            self.countBlank += 1

    def EditSaveBtn(self):
        status = self.VarEditSaveBtnBool.get()

        # If in view mode change to edit mode and change text
        if status == 0:
            status = 1
            self.VarEditSaveBtnText.set('Edit')
        # If in edit mode change to view mode and change text
        elif status == 1:
            status = 0
            self.VarEditSaveBtnText.set('View')
        print('status =', status)
        self.VarEditSaveBtnBool.set(status)
        return

    def MenuCommand(self):
        print('Option Clicked')
        return



root = Tk()
root.geometry('1000x800')
my_gui = GUI(root)
root.mainloop()



