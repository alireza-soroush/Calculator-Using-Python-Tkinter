#import's
from tkinter import *
from PIL import Image,ImageTk
#Application
root = Tk()
root.title('Calculator')
root.iconbitmap('path') # All the images are in the images folder, just copy their path !!
root.geometry('350x550+600+200')
root.config(bg='black')
root.resizable(False,False)
#global variables
operation = StringVar()
result = ''
#adding images
# All the images are in the images folder, just copy their path !!
b1 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b2 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b3 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b4 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b5 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b6 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b7 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b8 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b9 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b0 = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_back = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_clear = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_divide = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_equal = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_minus = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_mult = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_plus = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_point = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_plus_minus = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))
b_quit = ImageTk.PhotoImage(Image.open('image path').resize(size=(80,80)))

#------------------------------------------## main ##-------------------------------------#
#---------------frame show result------------------#
frame_show_result = Frame(root,width=350,height=100,bg='black')
frame_show_result.pack()

#widget's
result_entry = Entry(frame_show_result,textvariable=operation,width=12,border=10,fg='black',bg='black',font=('Syflean',35,'bold'),justify='center',state='readonly')
result_entry.pack(pady=25)

#---------------frame buttons------------------#
frame_button = Frame(root,width=350,height=350,bg='black')
frame_button.pack()
#widget's
button_quit = Button(frame_button,image=b_quit,borderwidth=0,bg='black',activebackground='black',command=quit)
button_quit.grid(row=0,column=0)

button_clear = Button(frame_button,image=b_clear,borderwidth=0,bg='black',activebackground='black',command=lambda:clear())
button_clear.grid(row=0,column=1)

button_back = Button(frame_button,image=b_back,borderwidth=0,bg='black',activebackground='black',command=lambda:one_back())
button_back.grid(row=0,column=2)

button_divide = Button(frame_button,image=b_divide,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('/'))
button_divide.grid(row=0,column=3)

button_1 = Button(frame_button,image=b1,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('1'))
button_1.grid(row=1,column=0)

button_2 = Button(frame_button,image=b2,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('2'))
button_2.grid(row=1,column=1)

button_3 = Button(frame_button,image=b3,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('3'))
button_3.grid(row=1,column=2)

button_mult = Button(frame_button,image=b_mult,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('*'))
button_mult.grid(row=1,column=3)

button_4 = Button(frame_button,image=b4,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('4'))
button_4.grid(row=2,column=0)

button_5 = Button(frame_button,image=b5,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('5'))
button_5.grid(row=2,column=1)

button_6 = Button(frame_button,image=b6,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('6'))
button_6.grid(row=2,column=2)

button_minus = Button(frame_button,image=b_minus,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('-'))
button_minus.grid(row=2,column=3)

button_7 = Button(frame_button,image=b7,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('7'))
button_7.grid(row=3,column=0)

button_8 = Button(frame_button,image=b8,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('8'))
button_8.grid(row=3,column=1)

button_9 = Button(frame_button,image=b9,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('9'))
button_9.grid(row=3,column=2)

button_plus = Button(frame_button,image=b_plus,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('+'))
button_plus.grid(row=3,column=3)

button_plus_minus = Button(frame_button,image=b_plus_minus,borderwidth=0,bg='black',activebackground='black',command=lambda:plus_minus())
button_plus_minus.grid(row=4,column=0)

button_0 = Button(frame_button,image=b0,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('0'))
button_0.grid(row=4,column=1)

button_point = Button(frame_button,image=b_point,borderwidth=0,bg='black',activebackground='black',command=lambda:math_operation('.'))
button_point.grid(row=4,column=2)

button_equal = Button(frame_button,image=b_equal,borderwidth=0,bg='black',activebackground='black',command=lambda:equal_button())
button_equal.grid(row=4,column=3)

#functions
def math_operation(op):
    global result
    math_list = ['*','/','-','+']
    checker = result
    last = list(checker)
    if op == '.':
        for i in math_list: 
            pointblock = result.split(i)
            if '.' in pointblock[-1]:
                pass
            else:
                result+=op
                operation.set(result)
    if op != '.':
        try:
            if op in math_list and last[-1] in math_list:
                result = list(result)
                result.pop()
                result.append(op)
                result = "".join(result)
                operation.set(result)

            else:
                if op in math_list:
                    if last[-1] == '.':
                        pass
                    else:
                        equal_button()
                        result += op
                        operation.set(result)
                else:
                    result += op
                    operation.set(result)
        except IndexError:
            pass

def clear():
    global result
    operation.set('')
    result = ''

def equal_button():
    global result
    try:
        math = eval(result)
        if '.' in str(math):
            operation.set(round(float(math),5))
            result = operation.get()
        else:
            operation.set(math)
            result = operation.get()
    except SyntaxError:
        pass
    except ZeroDivisionError:
        operation.set('Error!')
        result = ''

def one_back():
    global result
    if len(result) > 0:
        result = list(result)
        result.pop(len(result)-1)
        result = "".join(result)
        operation.set(result)

def plus_minus():
    global result
    equal_button()
    try:
        if '.' in result:
            operation.set(str(float(operation.get()) *-1))
            result = operation.get()
        else:
            operation.set(str(int(operation.get()) *-1))
            result = operation.get()
    except ValueError:
        pass

#loop
root.mainloop()