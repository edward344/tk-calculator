#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

class App(object):
    def __init__(self,master):
        master.title("TkCalculator")
        self.number = "0"
        self.label = Label(master,text=self.number,font=("Helvetica",14),width=17,height=3,anchor=E)
        self.label.pack()
        
        self.prevVal = 0
        self.newVal = 0
        self.operator = ""
        self.resultVal = 0
        
        frame1 = Frame(master)
        frame1.focus_set()
        frame1.bind("<Key>",self.key_callback)
        frame1.bind("<Return>",self.return_callback)
        frame1.bind("<Escape>",self.escape_callback)
        self.button7 = Button(frame1,text="7",width=5,height=2,command=self.button7)
        self.button7.pack(side=LEFT)
        self.button8 = Button(frame1,text="8",width=5,height=2,command=self.button8)
        self.button8.pack(side=LEFT)
        self.button9 = Button(frame1,text="9",width=5,height=2,command=self.button9)
        self.button9.pack(side=LEFT)
        self.button_plus = Button(frame1,text="+",width=5,height=2,command=self.addition)
        self.button_plus.pack(side=LEFT)
        frame1.pack()
        
        frame2 = Frame(master)
        self.button4 = Button(frame2,text="4",width=5,height=2,command=self.button4)
        self.button4.pack(side=LEFT)
        self.button5 = Button(frame2,text="5",width=5,height=2,command=self.button5)
        self.button5.pack(side=LEFT)
        self.button6 = Button(frame2,text="6",width=5,height=2,command=self.button6)
        self.button6.pack(side=LEFT)
        self.button_minus = Button(frame2,text="-",width=5,height=2,command=self.substraction)
        self.button_minus.pack(side=LEFT)
        frame2.pack()
        
        frame3 = Frame(master)
        self.button1 = Button(frame3,text="1",width=5,height=2,command=self.button1)
        self.button1.pack(side=LEFT)
        self.button2 = Button(frame3,text="2",width=5,height=2,command=self.button2)
        self.button2.pack(side=LEFT)
        self.button3 = Button(frame3,text="3",width=5,height=2,command=self.button3)
        self.button3.pack(side=LEFT)
        self.button_multiply = Button(frame3,text="x",width=5,height=2,command=self.multiplication)
        self.button_multiply.pack(side=LEFT)
        frame3.pack()
        
        frame4 = Frame(master)
        self.button0 = Button(frame4,text="0",width=5,height=2,command=self.button0)
        self.button0.pack(side=LEFT)
        self.button_point = Button(frame4,text=".",width=5,height=2,command=self.append_point)
        self.button_point.pack(side=LEFT)
        self.button_equal = Button(frame4,text="=",width=5,height=2,command=self.calculate)
        self.button_equal.pack(side=LEFT)
        self.button_divide = Button(frame4,text="/",width=5,height=2,command=self.division)
        self.button_divide.pack(side=LEFT)
        frame4.pack()


    def button1(self):
        self.append_number("1")
        
    def button2(self):
        self.append_number("2")
        
    def button3(self):
        self.append_number("3")
        
    def button4(self):
        self.append_number("4")
        
    def button5(self):
        self.append_number("5")
        
    def button6(self):
        self.append_number("6")
        
    def button7(self):
        self.append_number("7")
        
    def button8(self):
        self.append_number("8")
        
    def button9(self):
        self.append_number("9")
        
    def button0(self):
        self.append_number("0")
        
    def append_number(self,number):
        if self.number == "0":
            self.number = number
        elif len(self.number) <= 15:
            self.number += number
            
        self.newVal = float(self.number)
        
        self.label.config(text=self.number)
        
    def append_point(self):
        if not "." in self.number:
            self.number += "."
        
        self.label.config(text=self.number)
        
    def key_callback(self,event):
        if event.char.isdigit():
            self.append_number(event.char)
        elif event.char == ".":
            self.append_point()
        elif event.char == "+":
            self.addition()
        elif event.char == "-":
            self.substraction()
        elif event.char == "*":
            self.multiplication()
        elif event.char == "/":
            self.division()
            
            
    def return_callback(self,event):
        self.calculate()
        
    def escape_callback(self,event):
        self.newVal = 0
        self.prevVal = 0
        self.resultVal = 0
        self.number = "0"
        self.label.config(text="0")
            
    
    def addition(self):
        self.prevVal = self.newVal
        self.operator = "+"
        self.number = "0"
        
    def substraction(self):
        self.prevVal = self.newVal
        self.operator = "-"
        self.number = "0"
        
    def multiplication(self):
        self.prevVal = self.newVal
        self.operator = "*"
        self.number = "0"
        
    def division(self):
        self.prevVal = self.newVal
        self.operator = "/"
        self.number = "0"
        
    def get_display_number(self,number):
        str_number = str(number)
        if str_number[-2:] == ".0":
            return str_number[:-2]
        else:
            return str_number
        
    def calculate(self):
        if self.operator == "+":
            self.resultVal = self.prevVal + self.newVal
            self.newVal = self.resultVal
            self.number = "0"
            self.label.config(text=self.get_display_number(self.resultVal))
            
        elif self.operator == "-":
            self.resultVal = self.prevVal - self.newVal
            self.newVal = self.resultVal
            self.number = "0"
            self.label.config(text=self.get_display_number(self.resultVal))
            
        elif self.operator == "*":
            self.resultVal = self.prevVal * self.newVal
            self.newVal = self.resultVal
            self.number = "0"
            self.label.config(text=self.get_display_number(self.resultVal))
            
        elif self.operator == "/":
            try:
                self.resultVal = self.prevVal / self.newVal
                self.newVal = self.resultVal
                self.number = "0"
                self.label.config(text=self.get_display_number(self.resultVal))
            except ZeroDivisionError:
                self.resultVal = 0
                self.newVal = 0
                self.prevVal = 0
                self.number = "0"
                self.label.config(text="Math error")
            
        
         
def main():
    root = Tk()
    root.resizable(False,False)
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

