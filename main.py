from tkinter import *
from tkinter import ttk


def button_click_1():
    lbl_name['text']=int(entry_n1.get())+int(entry_n2.get())
def button_click_2():
    lbl_name['text']=int(entry_n1.get())-int(entry_n2.get())
def button_click_3():
    lbl_name['text']=int(entry_n1.get())*int(entry_n2.get())
root=Tk()
root.title('КАЛЬКУЛЯТОР')
root.geometry('350x350')
entry_n1 = ttk.Entry()
entry_n1.pack()
entry_n2 = ttk.Entry()
entry_n2.pack()
button_change_label_1 = Button(text='+',command=button_click_1)
button_change_label_1.pack()
button_change_label_2 = Button(text='-',command=button_click_2)
button_change_label_2.pack()
button_change_label_3 = Button(text='*',command=button_click_3)
button_change_label_3.pack()
lbl_name = Label(text='')
lbl_name.pack()
root.mainloop()





