from tkinter import Tk, Label, Button
from random import randint
from tkinter import *

from time import sleep
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.value = 0
        self.buttonnr = 0
        self.right={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0 ,"9":0}
        self.wrong={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        master.title("A simple GUI")


        self.close_button = Button(master, text="Close", font=("Courier", 44), command=self.checkanwer)
        self.close_button.grid(row = 4, column = 3,columnspan=2,)
        self.greet_button = Button(master, text="1", font=("Courier", 44), command=lambda: self.randomnumber(0))
        self.greet_button.grid(row=0, column=0)
        self.greet_button = Button(master, text="2", font=("Courier", 44), command=lambda: self.randomnumber(1))
        self.greet_button.grid(row = 0, column = 1)
        self.greet_button = Button(master, text="3", font=("Courier", 44), command=lambda: self.randomnumber(2))
        self.greet_button.grid(row = 0, column = 2)
        self.greet_button = Button(master, text="4", font=("Courier", 44), command=lambda: self.randomnumber(3))
        self.greet_button.grid(row = 1, column = 0)
        self.greet_button = Button(master, text="5", font=("Courier", 44), command=lambda: self.randomnumber(4))
        self.greet_button.grid(row = 1, column = 1)
        self.greet_button = Button(master, text="6", font=("Courier", 44), command=lambda: self.randomnumber(5))
        self.greet_button.grid(row = 1, column = 2)
        self.greet_button = Button(master, text="7", font=("Courier", 44), command=lambda: self.randomnumber(6))
        self.greet_button.grid(row = 2, column = 0)
        self.greet_button = Button(master, text="8", font=("Courier", 44), command=lambda: self.randomnumber(7))
        self.greet_button.grid(row=2, column=1)
        self.greet_button = Button(master, text="9", font=("Courier", 44), command=lambda: self.randomnumber(8))
        self.greet_button.grid(row=2, column=2)


        self.entry1 = Entry(root,width=10, font=("Courier", 44) )
        self.entry1.grid(row = 4, column = 1)
    def changeColour(self, inputbutton,color):
        inputbutton["bg"]= color
        var = IntVar()
        root.after(2000, var.set, 1)
        root.wait_variable(var)
        inputbutton.grid_forget()

    def checkanwer(self):
        answer = self.entry1.get()
        self.check = Button(self.master, text="hej", font=("Courier", 44), command=lambda: self.randomnumber(8))
        self.check.grid(row=5, column=1)
        if f"{answer}" == f"{self.value}":
            self.check["text"] = "RIGTIGT"
            self.changeColour(self.check,"green")
            self.right[str(self.buttonnr)]+=1
        else:
            self.check["text"] = f"Forkert: {self.value}"
            self.changeColour(self.check, "red")
            self.wrong[str(self.buttonnr)] += 1
        self.entry1.delete(0, END)
        print(self.right, self.wrong)
    def randomnumber(self,amount):
        number = randint(1 * 10**amount, 10 * 10**amount)
        self.close_button["text"] = number
        var = IntVar()
        root.after(500, var.set, 1)
        root.wait_variable(var)
        self.close_button["text"]="HUSK"
        self.value = number
        self.buttonnr = amount
        self.buttonnr += 1



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


