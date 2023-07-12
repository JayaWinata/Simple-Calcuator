import tkinter as tk

def add_calculation(str):
    global txt_input
    txt_input += str
    txt_temp.set(txt_input)

def clear():
    global txt_input
    txt_temp.set('')
    txt_input = ''

def equals():
    try:
        global txt_input
        txt_final.set(txt_input)
        txt_temp.set(eval(txt_input))
        txt_input = str(txt_temp.get())
    except:
        txt_temp.set('Error')
        txt_input = ''

def delete():
    global txt_input
    txt_input = txt_input[:-1]
    txt_temp.set(txt_input)

def press(button):
    button.invoke()

window = tk.Tk()
my_font = 'Adobe Fan Heiti Std B'
window.title('Simple Calculator')
window.geometry('270x430')
window.configure(bg='#070707')
window.resizable(False,False)
txt_input = ''
txt_temp = tk.StringVar()
txt_final = tk.StringVar()

label_final = tk.Label(window,textvariable=txt_final,height=1,width=35,font=(my_font,9),anchor='e',bg='#070707',fg='#909090').place(x=10,y=10)
label_preview = tk.Label(window,textvariable=txt_temp,height=2,width=20,font=(my_font,15),anchor='se',bg='#070707',fg='white').place(x=12,y=45)

# row 1
button_7 = tk.Button(window,text='7',height=2,width=5,font=35,command=lambda: add_calculation('7'),bg='#242424',fg='white').place(x=10,y=130)
button_8 = tk.Button(window,text='8',height=2,width=5,font=35,command=lambda: add_calculation('8'),bg='#242424',fg='white').place(x=75,y=130)
button_9 = tk.Button(window,text='9',height=2,width=5,font=35,command=lambda: add_calculation('9'),bg='#242424',fg='white').place(x=140,y=130)
button_divide = tk.Button(window,text='/',height=2,width=5,font=35,command=lambda: add_calculation('/'),bg='#242424',fg='white').place(x=205,y=130)
# row 2
button_4 = tk.Button(window,text='4',height=2,width=5,font=35,command=lambda: add_calculation('4'),bg='#242424',fg='white').place(x=10,y=190)
button_5 = tk.Button(window,text='5',height=2,width=5,font=35,command=lambda: add_calculation('5'),bg='#242424',fg='white').place(x=75,y=190)
button_6 = tk.Button(window,text='6',height=2,width=5,font=35,command=lambda: add_calculation('6'),bg='#242424',fg='white').place(x=140,y=190)
button_times = tk.Button(window,text='x',height=2,width=5,font=35,command=lambda: add_calculation('*'),bg='#242424',fg='white').place(x=205,y=190)
# row 3
button_1 = tk.Button(window,text='1',height=2,width=5,font=35,command=lambda: add_calculation('1'),bg='#242424',fg='white').place(x=10,y=250)
button_2 = tk.Button(window,text='2',height=2,width=5,font=35,command=lambda: add_calculation('2'),bg='#242424',fg='white').place(x=75,y=250)
button_3 = tk.Button(window,text='3',height=2,width=5,font=35,command=lambda: add_calculation('3'),bg='#242424',fg='white').place(x=140,y=250)
button_substract = tk.Button(window,text='-',height=2,width=5,font=35,command=lambda: add_calculation('-'),bg='#242424',fg='white').place(x=205,y=250)
# row 4
button_del = tk.Button(window,text='Del.',height=2,width=5,font=20,command=lambda: delete(),bg='#242424',fg='white').place(x=10,y=310)
button_0 = tk.Button(window,text='0',height=2,width=5,font=35,command=lambda: add_calculation('0'),bg='#242424',fg='white').place(x=75,y=310)
button_decimal = tk.Button(window,text='.',height=2,width=5,font=35,command=lambda: add_calculation('.'),bg='#242424',fg='white').place(x=140,y=310)
button_plus = tk.Button(window,text='+',height=2,width=5,font=35,command=lambda: add_calculation('+'),bg='#242424',fg='white').place(x=205,y=310)
# row 5
button_equals = tk.Button(window,text='=',height=2,width=19,font=35,command=lambda: equals(),bg='#242424',fg='white').place(x=10,y=370)
button_C = tk.Button(window,text='C',height=2,width=5,font=35,command=lambda: clear(),bg='#242424',fg='white').place(x=205,y=370)

window.bind('<Key-0>',lambda a: add_calculation('0'))
window.bind('<Key-1>',lambda a: add_calculation('1'))
window.bind('<Key-2>',lambda a: add_calculation('2'))
window.bind('<Key-3>',lambda a: add_calculation('3'))
window.bind('<Key-4>',lambda a: add_calculation('4'))
window.bind('<Key-5>',lambda a: add_calculation('5'))
window.bind('<Key-6>',lambda a: add_calculation('6'))
window.bind('<Key-7>',lambda a: add_calculation('7'))
window.bind('<Key-8>',lambda a: add_calculation('8'))
window.bind('<Key-9>',lambda a: add_calculation('9'))
window.bind('<Key-9>',lambda a: add_calculation('9'))
window.bind('<Key-x>',lambda a: add_calculation('*'))
window.bind('<Key-+>',lambda a: add_calculation('+'))
window.bind('<Key-/>',lambda a: add_calculation('/'))
window.bind('<minus>',lambda a: add_calculation('-'))
window.bind('<Key-c>',lambda a: clear())
window.bind('<Return>',lambda a: equals())
window.bind('<BackSpace>',lambda a: delete())
window.mainloop()
