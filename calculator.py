from tkinter import*

root = Tk()
 

root.title('Простой калькулятор')
# что возвращаеться???ффф
def click_evant(event=None):
    tmp = 0
    assert type(event) == int
    CURRENT = entry_field.get()
    entry_field.delete(0,END)
    entry_field.insert(0 , str(CURRENT) + str(event))
    tmp = entry_field.get()
    print(tmp)
    return tmp


def clear_event():
    entry_field.delete(0 , END)

def add():
    pass

def resalt():
    pass

entry_field = Entry(root , width=40 , borderwidth=5)    
entry_field.grid(row=0 , column=0 , columnspan=3 , padx=10 , pady=10)
button_1 = Button(root , text='1' ,padx=40 , pady=20 , command=lambda: click_evant(1))
button_2 = Button(root , text='2' ,padx=40 , pady=20 , command=lambda: click_evant(2))
button_3 = Button(root , text='3' ,padx=40 , pady=20 , command=lambda: click_evant(3))
button_4 = Button(root , text='4' ,padx=40 , pady=20 , command=lambda: click_evant(4))
button_5 = Button(root , text='5' ,padx=40 , pady=20 , command=lambda: click_evant(5))
button_6 = Button(root , text='6' ,padx=40 , pady=20 , command=lambda: click_evant(6))
button_7 = Button(root , text='7' ,padx=40 , pady=20 , command=lambda: click_evant(7))
button_8 = Button(root , text='8' ,padx=40 , pady=20 , command=lambda: click_evant(8))
button_9 = Button(root , text='9' ,padx=40 , pady=20, command=lambda: click_evant(9))
button_0 = Button(root , text='0' ,padx=40 , pady=20, command=lambda: click_evant(0))
button_add = Button(root , text='+' , padx=39 , pady=20,command=add())
button_equal = Button(root , text='=' , padx=40 , pady=20,command=resalt())
button_clear = Button(root , text='Сброс' , padx=40 , pady=20, command=clear_event)

button_1.grid(row=1 , column=0)
button_2.grid(row=1 , column=1)
button_3.grid(row=1 , column=2)
button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)
button_7.grid(row=3 , column=0)
button_8.grid(row=3 , column=1)
button_9.grid(row=3 , column=2)
button_0.grid(row=4 , column=0)
button_add.grid(row=5 , column=0)
button_clear.grid(row=4 , column=1 , columnspan=2 , sticky="we")
button_equal.grid(row=5 , column=1 ,columnspan=2 , sticky="we")


root.mainloop()