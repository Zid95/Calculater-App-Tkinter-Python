from tkinter import *


calc = Tk()


calc.title('Basic Calculater')
calc.iconbitmap('Calc icon.ico')
calc.geometry('425x450+250+200')
calc.configure(bg='#272b2f')
calc.resizable(width=False, height=False)

my_input = StringVar()


my_operator = ""


def click_buttons(numbers):
    global my_operator
    my_operator += (str(numbers))
    my_input.set(my_operator)


def result_button():
    try:
        global my_operator
        result = str(eval(my_operator))
        my_input.set(result)
        my_operator = result

    except Exception as e:
        my_input.set(e)


def clear_button():
    global my_operator
    my_operator = ""
    my_input.set(my_operator)


text_result = Entry(calc, width=34, font=('Times', 14, 'bold'),
                    bg='powder blue', bd=6, textvariable=my_input, state='readonly')
text_result.place(x=39, y=50)

btn7 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='7', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons("7"))
btn7.place(x=40, y=105)


btn8 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='8', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(8))
btn8.place(x=130, y=105)


btn9 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='9', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(9))
btn9.place(x=220, y=105)

btn4 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='4', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(4))
btn4.place(x=40, y=190)


btn5 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='5', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(5))
btn5.place(x=130, y=190)


btn6 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='6', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(6))
btn6.place(x=220, y=190)


btn1 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='1', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(1))
btn1.place(x=40, y=275)


btn2 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='2', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(2))
btn2.place(x=130, y=275)


btn3 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='3', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(3))
btn3.place(x=220, y=275)

btn0 = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='0', bd=4, bg='#CEECF5', fg='black', command=lambda: click_buttons(0))
btn0.place(x=130, y=360)

btn_addition = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='+', bd=4, bg='orange', fg='black', command=lambda: click_buttons("+"))
btn_addition.place(x=310, y=105)

btn_subtraction = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='-', bd=4, bg='orange', fg='black', command=lambda: click_buttons("-"))
btn_subtraction.place(x=310, y=190)


btn_multiplication = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='*', bd=4, bg='orange', fg='black', command=lambda: click_buttons("*"))
btn_multiplication.place(x=310, y=275)

btn_division = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='/', bd=4, bg='orange', fg='black', command=lambda: click_buttons("/"))
btn_division.place(x=310, y=360)

btn_equal = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='=', bd=4, bg='orange', fg='black', command=result_button)
btn_equal.place(x=220, y=360)

btn_clear = Button(calc, padx=10, pady=2, width=4, height=2, font=(
    'Times', 16, 'bold'), text='C', bd=4, bg='orange', fg='black', command=clear_button)
btn_clear.place(x=40, y=360)


calc.mainloop()
