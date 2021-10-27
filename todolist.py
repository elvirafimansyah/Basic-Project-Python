#struktur dasar tkinter 
# untuk gui
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('450x550')
win.title("To Do List")
win.config(bg="#9991ff")
win.iconbitmap("e:/Belajar Coding/todolist.ico")
win.resizable(0,0)

my_frame = Frame(win)
my_frame.pack(pady=10)

#membuat list box
my_list = Listbox(my_frame, font="Arial 22", width=25, height=5, bg="SystemButtonFace", fg="#464646", bd=0, highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack()

my_list.pack(side=LEFT, fill=BOTH)

stuff = []
# menambahkan contoh list ke Listbox
for item in stuff:
    my_list.insert(END, item)

# membuat scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT)

#menambahkan scroll bar 
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview )

#membuat kotak entri untuk menambahkan items ke list
my_entry = Entry(win, font="Helvetica 18", width=28, borderwidth=3)
my_entry.pack(pady=20)

# membuat tombol frame 
button_frame = Frame(win)
button_frame.pack(pady=20)

#membuat fungsi item
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # menambahkan garis di selection bar
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646") 
    # menambahkan garis di selection bar
    my_list.selection_clear(0, END)

def delete_cross():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        
        count += 1

# membuat beberapa tombol
delete_button = Button(button_frame, text="Hapus Item",pady=7,width=30,bg="#8CFF78",fg="black", command=delete_item)
add_button = Button(button_frame, text="Tambah Item",pady=7,width=30,bg="#FFEE91",fg="black", command=add_item)
cross_off_button = Button(button_frame, text="Selesai/Coret Item",pady=7,width=30,bg="#8CFF78",fg="black", command=cross_off_item)
uncross_button = Button(button_frame, text="Hapus Coret Item",pady=7,width=30,bg="#FFEE91",fg="black", command=uncross_item)
deletecross_button = Button(button_frame, text="Hapus Coretan",pady=7,width=30,bg="#8CFF78",fg="black", command=delete_cross)
quit_button = Button(win, text="Keluar",padx=10, pady=5,bg="#85BDFF", command=win.quit)

delete_button.grid(row=0, column=3)
add_button.grid(row=1, column=3)
cross_off_button.grid(row=2, column=3)
uncross_button.grid(row=3, column=3)
deletecross_button.grid(row=4, column=3)
quit_button.pack()

win.mainloop()

