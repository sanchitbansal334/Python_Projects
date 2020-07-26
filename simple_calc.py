from tkinter import *


root = Tk()
#root.geometry('500x500')
root.title("Simple Calculator")

e=Entry(root , width =60 , borderwidth=5)
e.grid(row=0,column = 0 , columnspan=4,padx=10,pady=10)
global math
math=""
def button_click(number):
	curr = e.get()
	e.delete(0,END)
	e.insert(0,str(curr) + str(number))
def button_clr():
	e.delete(0,END)
def button_add():
	fir=e.get()
	global f_num 
	global math
	math="add"
	f_num= float(fir)
	e.delete(0,END)
def button_eq():
	sec = e.get()
	e.delete(0,END)
	if sec == "":
		e.insert(0,"ERROR")
	if math == "":
		e.insert(0,"ERROR")
	if math =="add":
		e.insert(0,f_num + float(sec))
	if math =="sub":
		e.insert(0,f_num - float(sec))
	if math =="mul":
		e.insert(0,f_num * float(sec))
	if math =="div":
		e.insert(0,f_num / float(sec))
	
def button_sub():
	fir=e.get()
	global f_num 
	global math
	math="sub"
	f_num= float(fir)
	e.delete(0,END)
def button_mul():
	fir=e.get()
	global f_num 
	global math
	math="mul"
	f_num= float(fir)
	e.delete(0,END)
def button_div():
	fir=e.get()
	global f_num 
	global math
	math="div"
	f_num= float(fir)
	e.delete(0,END)

b_1 = Button(root,text="1" , padx=40,pady=20,command=lambda: button_click(1))
b_2 = Button(root,text="2" , padx=40,pady=20,command=lambda: button_click(2))
b_3 = Button(root,text="3" , padx=40,pady=20,command=lambda: button_click(3))
b_4 = Button(root,text="4" , padx=40,pady=20,command=lambda: button_click(4))
b_5 = Button(root,text="5" , padx=40,pady=20,command=lambda: button_click(5))
b_6 = Button(root,text="6" , padx=40,pady=20,command=lambda: button_click(6))
b_7 = Button(root,text="7" , padx=40,pady=20,command=lambda: button_click(7))
b_8 = Button(root,text="8" , padx=40,pady=20,command=lambda: button_click(8))
b_9 = Button(root,text="9" , padx=40,pady=20,command=lambda: button_click(9))
b_0 = Button(root,text="0" , padx=88,pady=20,command=lambda: button_click(0))
b_add = Button(root,text="+" , padx=39,pady=52,command=lambda: button_add())
b_equal = Button(root,text="= " , padx=86,pady=20,command=lambda: button_eq())
b_clear = Button(root,text="Clear " , padx=28,pady=20,command=lambda: button_clr())
b_sub = Button(root,text="-" , padx=39,pady=52,command=lambda: button_sub())
b_mul = Button(root,text="*" , padx=40,pady=20,command=lambda: button_mul())
b_div = Button(root,text="/" , padx=40,pady=20,command=lambda: button_div())

b_1.grid(row=4 , column=0 )
b_2.grid(row=4 , column=1 )
b_3.grid(row=4 , column=2 )

b_4.grid(row=3 , column=0 )
b_5.grid(row=3 , column=1 )
b_6.grid(row=3 , column=2 )

b_7.grid(row=2 , column=0 )
b_8.grid(row=2 , column=1 )
b_9.grid(row=2 , column=2 )

b_0.grid(row=5 , column=0 ,columnspan=2)
b_add.grid(row=3 , column=3 ,rowspan=2 )

b_equal.grid(row=5 , column=2,columnspan=2 )
b_clear.grid(row=1 , column=0)

b_sub.grid(row=1 , column=3 ,rowspan=2)
b_mul.grid(row=1 , column=2 )
b_div.grid(row=1 , column=1 )

root.mainloop()