from tkinter import *
from dbhelper import DBHelper
from tkinter import messagebox
from tabulate import tabulate
from tkinter import ttk
import prettytable


class expenseTracker:

    def __init__(self):
        # when the file is run,the constructor of DBHelper is called , and the file gets connected to database

        self.db = DBHelper()

        self.constructGUI()


    def constructGUI(self):
        self.root = Tk()

        self.root.title("Expense Tracker")
        self.root.minsize(350, 550)
        self.root.maxsize(350, 550)

        self.root.configure(background="#c6e5d9")
        # to load the icon
        self.root.iconbitmap(r'C:\Users\acer\PycharmProjects\expensetracker\icon\money1.ico')

        self.loadLoginGUI()
        self.root.mainloop()

    # clearing the GUI
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def loadLoginGUI(self):

        self.clear()

        self.title=Label(self.root,text="EXPENSE TRACKER",bg="#c6e5d9",fg="#013750")
        self.title.configure(font=("Arial",26,"bold"))
        self.title.pack(pady=(30,30))

        self.frame1=Frame(self.root)
        self.frame1.pack(pady=(15,15))

        self.emailLabel=Label(self.frame1,text="Enter email",bg="#c6e5d9",fg="#031634")
        self.emailLabel.configure(font=("Times", 14))
        self.emailLabel.pack(side=LEFT)


        self.emailInput=Entry(self.frame1)
        self.emailInput.pack(side=RIGHT,ipadx=25,ipady=5)

        self.frame2=Frame(self.root)
        self.frame2.pack(pady=(10,15))


        self.loginBtn=Button(self.root,text="Login",bg="#fff",fg="#031634",command=lambda : self.doLogin())
        self.loginBtn.pack(pady=(10,15))


        self.passwordLabel=Label(self.frame2,text="Enter Password",bg="#c6e5d9",fg="#031634")
        self.passwordLabel.configure(font=("Times", 14))
        self.passwordLabel.pack(side=LEFT)

        self.passwordInput=Entry(self.frame2)
        self.passwordInput.pack(side=RIGHT,ipadx=25,ipady=5)


        self.title2=Label(self.root,text="Don't have an account? Register Now",bg="#c6e5d9",fg="#031634")
        self.title2.pack()

        self.registerBtn=Button(self.root,text="Register",bg="#fff",fg="#031634",command=lambda:self.loadRegisterGUI())
        self.registerBtn.pack(pady=(15,5))

    def doLogin(self):


        email = self.emailInput.get()
        password = self.passwordInput.get()

        data = self.db.checkLogin(email, password)
        #print(data)


        if len(data) > 0:

            self.user_id=data[0][0]
            self.name=data[0][1]

            self.userProfileGUI()



        else:
            messagebox.showerror("Error", "Incorrect Credentials")


    def userProfileGUI(self):

        self.clear()

        self.headerMenu()



        self.title = Label(self.root, text="EXPENSE TRACKER", bg="#c6e5d9", fg="#013750")
        self.title.configure(font=("Arial", 26, "bold"))
        self.title.pack(pady=(30,30))



        self.title1=Label(self.root,text="Hi! "+ self.name, bg="#c6e5d9", fg="#5b7c8d")
        self.title1.configure(font=("Times",24,"bold"))
        self.title1.pack(pady=(30,30))

        self.frame1=Frame(self.root)
        self.frame1.pack(pady=(20,20))




        self.display=Label(self.frame1,text="Your total Spending till now(Rs.)",bg="#c6e5d9",fg="#031634")
        self.display.configure(font=("Times",18))
        self.display.pack(side=TOP)



        self.result=self.totalSpending()
        #print(self.result)
        self.display2=Label(self.frame1,text=str(self.result))
        self.display2.configure(font=("Times",20))
        self.display2.pack(side=BOTTOM)



    def headerMenu(self):

        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)

        filemenu.add_command(label="Go back to Homepage", command= lambda : self.homePage())
        filemenu.add_command(label="Logout",command=lambda :self.logout())

        helpmenu=Menu(menu)
        menu.add_cascade(label="File",menu=helpmenu)
        helpmenu.add_command(label="Add Expenses", command=lambda: self.addExpensesHere())
        helpmenu.add_command(label="Edit Expenses", command=lambda: self.editExpensesHere())
        helpmenu.add_command(label="Delete Expenses", command=lambda: self.deleteExpensesHere())
        helpmenu.add_command(label="View Expenses", command=lambda: self.viewExpenses())

        aboutmenu=Menu(menu)
        menu.add_cascade(label="Help",menu=aboutmenu)
        aboutmenu.add_command(label="About",command=lambda :self.viewabout())




    def addExpensesHere(self,mode=1):

        self.clear( )
        self.headerMenu()

        self.title = Label(self.root, text="EXPENSE TRACKER", bg="#c6e5d9", fg="#013750")
        self.title.configure(font=("Arial", 26, "bold"))
        self.title.pack(pady=(30, 30))

        self.frame1=Frame(self.root)
        self.frame1.pack(pady=(5,15))

        self.expenseType = Label(self.frame1, text="Enter Expense Type", bg="#c6e5d9", fg="#013750")
        self.expenseType.pack(side=LEFT)

        self.expenseTypeInput = Entry(self.frame1, bg="#fff", fg="#000")
        self.expenseTypeInput.pack(side=RIGHT)


        self.frame2 = Frame(self.root)
        self.frame2.pack(pady=(5, 15))

        if mode==1 or mode==3:
            self.amountSpent = Label(self.frame2, text=" Enter Amount Spent(Rs.)", bg="#c6e5d9", fg="#013750")
            self.amountSpent.pack(side=LEFT)

            self.amountSpentInput = Entry(self.frame2, bg="#fff", fg="#000")
            self.amountSpentInput.pack(side=RIGHT)


        if mode==2:
            self.amountSpent = Label(self.frame2, text=" Enter Changed Amount Spent(Rs.)", bg="#c6e5d9", fg="#013750")
            self.amountSpent.pack(side=LEFT)

            self.amountSpentInput = Entry(self.frame2, bg="#fff", fg="#000")
            self.amountSpentInput.pack(side=RIGHT)

        self.frame3 = Frame(self.root)
        self.frame3.pack(pady=(5, 15))

        self.dateofExpenditure = Label(self.frame3, text=" Enter Date (dd-mm-yyyy)", bg="#c6e5d9", fg="#013750")
        self.dateofExpenditure.pack(side=LEFT)

        self.dateofExpenditureInput= Entry(self.frame3, bg="#fff", fg="#000")
        self.dateofExpenditureInput.pack(side=RIGHT)


        if mode==1:
            self.addExpenseBtn = Button(self.root, text="ADD", bg="#fff", fg="#033649",
                                        command=lambda: self.doAddExpense())
            self.addExpenseBtn.pack()

        if mode==2:
            self.editExpenseBtn = Button(self.root, text="EDIT", bg="#fff", fg="#033649",
                                        command=lambda: self.doeditExpenses())
            self.editExpenseBtn.pack()

        if mode == 3:
            self.deleteExpenseBtn = Button(self.root, text="DELETE", bg="#fff", fg="#033649",
                                         command=lambda: self.dodeleteExpenses())
            self.deleteExpenseBtn.pack()




    def editExpensesHere(self):

        self.clear()
        self.addExpensesHere(mode=2)

    def deleteExpensesHere(self):

        self.clear()
        self.addExpensesHere(mode=3)

    def doAddExpense(self):


        expenseType=self.expenseTypeInput.get()
        amountSpent=self.amountSpentInput.get()
        date=self.dateofExpenditureInput.get()




        response=self.db.performAddExpense(self.user_id,expenseType,amountSpent,date)


        if response==1:
            check=self.db.checkexpenses(self.user_id,expenseType,amountSpent,date)
            #print(check)
            if check==0:
                messagebox.showinfo("Success", "Expense added successfully")


        else:
            messagebox.showerror("error","some error occurred")



    def totalSpending(self):


        data=self.db.performtotalSpending(self.user_id)
        result=data[0][0]
        #print(result)
        if result==None:
            return 0
        else:
            return result

    def viewabout(self):
        self.clear()

        self.title = Label(self.root, text="ABOUT", bg="#c6e5d9", fg="#013750")
        self.title.configure(font=("Arial", 26, "bold"))
        self.title.pack(pady=(30, 30))

        about="This is an expense tracker application where you can track all your expenses.\n " \
              "You can add, delete, edit and view your expenses. \n\n\n" \
              "Created by-SHREYA SUR \n" \
              "Created on-09.09.2020"
        self.msg=Message(self.root,text=about,bg="#c6e5d9", fg="#013750")
        self.msg.configure(font=("Arial",18))
        self.msg.pack()


    def doeditExpenses(self):

        expenseType = self.expenseTypeInput.get()
        amountSpent = self.amountSpentInput.get()
        date = self.dateofExpenditureInput.get()

        response = self.db.editExpenses(expenseType,amountSpent,date,self.user_id)

        if response==1:

            messagebox.showinfo("Success", "Expenses edited successfully")

        else:
            messagebox.showerror("Error", "Some error occurred")

    def dodeleteExpenses(self):

        expenseType = self.expenseTypeInput.get()
        amountSpent = self.amountSpentInput.get()
        date = self.dateofExpenditureInput.get()

        response = self.db.deleteExpenses(self.user_id,expenseType, amountSpent, date)

        if response == 1:

            messagebox.showinfo("Success", "expenses deleted successfully")

        else:
            messagebox.showerror("Error", "Data entered doesn't exist")

    def viewExpenses(self):

        self.clear()

        self.title = Label(self.root, text="EXPENSE TRACKER", bg="#c6e5d9", fg="#013750")
        self.title.configure(font=("Arial", 26, "bold"))
        self.title.pack(pady=(30, 30),side=TOP)



        data=self.db.performViewExpenses(self.user_id)

        self.frame=Frame(self.root)
        self.frame.pack()

        self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3), height=15, show="headings")
        self.tree.pack(side='left')

        self.tree.heading(1, text="Expense Type")
        self.tree.heading(2, text="Amount")
        self.tree.heading(3, text="Date")

        self.tree.column(1, width=100)
        self.tree.column(2, width=100)
        self.tree.column(3, width=100)

        self.scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scroll.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=self.scroll.set)

        for i in range(len(data)):
            self.tree.insert('', 'end', values=(data[i][1],data[i][2], data[i][3]))


        if len(data)==0:
            messagebox.showerror("Error","No rows added yet")


   # loading the homepage
    def homePage(self):

        self.clear()
        self.userProfileGUI()

    def logout(self):
        # we are destroying the entire window and recreating so that the header menu does'nt reappear.
        self.root.destroy()
        self.constructGUI()

    def loadRegisterGUI(self):

        self.clear()
        self.title = Label(self.root, text="EXPENSE TRACKER", bg="#c6e5d9", fg="#013750")
        self.title.configure(font=("Arial", 26, "bold"))
        self.title.pack(pady=(30, 30))

        self.nameLabel = Label(self.root, text="Enter Name",bg="#c6e5d9", fg="#013750")
        self.nameLabel.pack()

        self.nameInput = Entry(self.root)
        self.nameInput.pack()

        self.emailLabel = Label(self.root, text="Enter email", bg="#c6e5d9", fg="#013750")
        self.emailLabel.pack()

        self.emailInput = Entry(self.root)
        self.emailInput.pack()

        self.passwordLabel = Label(self.root, text="Enter Password",bg="#c6e5d9", fg="#013750")
        self.passwordLabel.pack()

        self.passwordInput = Entry(self.root)
        self.passwordInput.pack()


        self.register = Button(self.root, text="Register", bg="#fff", fg="#033649", command=lambda: self.doRegister())
        self.register.pack(pady=(10, 10))

        self.frame = Frame(self.root)
        self.frame.pack(pady=(10))

        self.message = Label(self.frame, text="Go Back To Login", bg="#c6e5d9", fg="#033649")
        self.message.pack(side=LEFT)

        self.loginBtn = Button(self.frame, text="Login", command=lambda: self.loadLoginGUI())
        self.loginBtn.pack(side=RIGHT)


    def doRegister(self):

        name = self.nameInput.get()
        email = self.emailInput.get()
        password = self.passwordInput.get()


        # call dbhelper

        response = self.db.performRegistration(name, email, password)

        if (response == 1):
            messagebox.showinfo("Registration Successful", "Completed!")

        else:
            messagebox.showerror("Error", "Failed!")



obj=expenseTracker()



