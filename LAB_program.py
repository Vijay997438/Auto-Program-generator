# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:28:35 2020

@author: Vijay
"""
import random
import csv
from tkinter import * ;
from tkinter.ttk import *
root2=Tk()
root2.configure(bg="orange")
"""C = Canvas(root2, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\Vijay\\vijj.png")
background_label = Label(root2, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)"""

root2.title("Auto Program Generator-CSE")
root2.geometry("500x300")
stude=[['USN','Program Assigned']]
def textfi(pgm,rl):
    rn="4SF17CS"+rl.upper()
    stude.append([rn,pgm])
    root3=Tk()
    root3.title("PROGRAM DISPLAY")
    root3.configure(bg="green")
    root3.geometry("700x200")
    lb1=Label(root3 , text="System Software and Compiler Design Laboratory-Department of CSE - Lab Internals "+"\n\n"+"\t \t Your Lab program is" +"\n\n"+""+pgm,font='Helvetica 9 bold')
    lb1.pack()
    root3.mainloop()
    print(stude)
def gen():
    n=random.randint(1,8)
    print("your Program is",n)
    l1=[" ","1.a) Write a LEX program to recognize valid arithmetic expression."+"\n b).Write YACC program to evaluate arithmetic expression " ,"2. Execute a program using YACC tool to recognize all stringsending with b preceded by na’s using the grammar a n b "] 
    l2=["4.Shift ReduceParsing techniquefor the grammar rules: E →E+T | T, T →T*F | F, F →(E) | id and parse the sentence: id + id * id","5. C/Java program to generate the machine code using Triples for the statement A = -B * (C +D)"]
    l3=["6 a)  Write a LEX program to eliminate comment lines in a C program "+"\n b)  YACC program to recognize valid identifier, operators and keywords","7.C/C++/Java program to simulate the working of Shortest remaining time and Round Robin (RR) scheduling algorithms"]
    l4=["8.C/C++/Java program to implement Banker’salgorithm.","9.Design, develop and implement a C/C++/Java program to implement page replacement algorithms LRU and FIFO. Assume suitable input required todemonstrate the results." ]
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)
    print(l1)
    root4=Tk()
    root4.title("Student Roll NUmber")
    root4.configure(bg="white")
    root4.geometry("300x200")
    roll_no=Label(root4,text="Enter student roll Number ")
    roll_no_g=Entry(root4)
    roll_no.pack()
    roll_no_g.pack()
    bt3=Button(root4,text='ok',command=lambda:textfi(l1[n],str(roll_no_g.get())))
    bt3.pack(side=TOP,pady=0)
def close():
   fname=batch_ent.get()+".csv"
   with open(fname,'w',newline='') as n_4:
    csv_writer=csv.writer(n_4,delimiter=",")
    for i in stude:
        csv_writer.writerow(i)
        
L1=Label(root2,text="Enter Batch")
L1.pack(side=TOP,pady=10)
batch_ent=Entry(root2)
batch_ent.pack(side=TOP,pady=10)
Bt1=Button(root2,text="generate",command=lambda:gen())
Bt1.pack(side=TOP,pady=20)
Bt1=Button(root2,text="Done",command=lambda:close())
Bt1.pack(side=TOP,pady=20)
Lab=Label(root2,text="Designed and Developed by Mr.Vijay C.P Assistant Professor-CSE-SCEM-Mangalore")
Lab.pack(side=BOTTOM)
root2.mainloop()
