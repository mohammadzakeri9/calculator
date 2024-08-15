#=============== modules ===============
from tkinter import *

#+++++++++++++++++++++++++++++ func & but +++++++++++++++++++++++++++
window = Tk()
window.config(bg='red')
window.resizable(FALSE,FALSE)
window.title("Calculator")
operator = ""

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def EqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

def clear():
    global operator
    operator =""
    text_input.set("")

text_input = StringVar()
#=============== 7/8/9/+ ===============
txtDisplay = Entry(window, font=('arial', 20, 'bold'), textvariable=text_input, bd=30,
                   insertwidth=4, bg='red', justify='right').grid(columnspan=4)
btn7 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
               text='7', command=lambda:btnClick(7) ).grid(row=1, column=0)
btn8 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
               text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
               text='9', command=lambda:btnClick(9)).grid(row=1, column=2)
addition = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
               text='+', command=lambda:btnClick('+')).grid(row=1, column=3)

#=============== 4/5/6/_ ===============
btn4 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue',font=('arial', 20, 'bold'),
              text='6', command=lambda:btnClick(6)).grid(row=2, column=2)
subtraction = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='_', command=lambda:btnClick('-')).grid(row=2, column=3)

#=============== 1/2/3/* ===============
btn1 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
                 text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='3', command=lambda:btnClick(3)).grid(row=3, column=2)
multiply = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='*', command=lambda:btnClick('*')).grid(row=3, column=3)

#=============== c/0/=// ===============
btnClear = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='C', command= clear).grid(row=4, column=0)
btn0 = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='0', command=lambda:btnClick(0)).grid(row=4, column=1)
btnEquals = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='=', command=EqualsInput).grid(row=4, column=2)
division = Button(window, padx=16, pady=16, bd=8, fg='yellow', bg='blue', font=('arial', 20, 'bold'),
              text='/', command=lambda:btnClick('/')).grid(row=4, column=3)

#=============== win_mainloop ===============
window.mainloop()