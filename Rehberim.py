from tkinter import *
import vtmodul
window = Tk()
window.title("İletişim Rehberi")
window.iconbitmap('rehber.ico')
window.configure(bg='#C5CAE9')

def view_command():
    lb.delete(0,END)
    for row in vtmodul.viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in vtmodul.search(ad=ad.get(),mobil=mobil.get(),mail=mail.get(),adres=adres.get()):
        lb.insert(END,row)

def add_command():
    vtmodul.add(ad.get(),mobil.get(),mail.get(),adres.get())
    lb.delete(0,END)
    lb.insert(END,ad.get(),mobil.get(),mail.get(),adres.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

    except IndexError:
        pass

def update_command():
    vtmodul.update(selected_tuple[0],ad.get(),mobil.get(),mail.get(),adres.get())
    view_command()

def delete_command():
    vtmodul.delete(selected_tuple[0])
    view_command()

def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    

l1 = Label(window,bg="#C5CAE9",text="Ad :")
l1.grid(row=0,column=0,columnspan=2)
l2 = Label(window,bg="#C5CAE9",text="Telefon Numarası :")
l2.grid(row=1,column=0,columnspan=2)
l3 = Label(window,bg="#C5CAE9",text="Mail Adresi :")
l3.grid(row=2,column=0,columnspan=2)
l4 = Label(window,bg="#C5CAE9",text="Adres/Konum :")
l4.grid(row=3,column=0,columnspan=2)


ad=StringVar()
e1 = Entry(window,textvariable=ad,width=60)
e1.grid(row=0,column=1,columnspan=10)

mobil=StringVar()
e2 = Entry(window,textvariable=mobil,width=60)
e2.grid(row=1,column=1,columnspan=10)

mail=StringVar()
e3 = Entry(window,textvariable=mail,width=60)
e3.grid(row=2,column=1,columnspan=10)

adres=StringVar()
e4 = Entry(window,textvariable=adres,width=60)
e4.grid(row=3,column=1,columnspan=10)


b1 = Button(window,text="Ekle",width=12,bg="#388E3C",fg="white",command=add_command)
b1.grid(row=5,column=0)

b2 = Button(window,text="Güncelle",width=12,bg="#5C6BC0",fg="white",command=update_command)
b2.grid(row=5,column=1)

b3 = Button(window,text="Ara",width=12,bg="#5C6BC0",fg="white",command=search_command)
b3.grid(row=5,column=2)

b4 = Button(window,text="Tümünü Göster",bg="#5C6BC0",fg="white",width=12,command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Sil",width=12,bg="#B71C1C",fg="white",command=delete_command)
b5.grid(row=5,column=4)

b7 = Button(window,text="Temizle",width=12,bg="#F44336",fg="white",command=clear_command)
b7.grid(row=5,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=6,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=6,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
