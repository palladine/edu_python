from tkinter import *
from tkinter import messagebox

root = Tk()
root.title ("GUI на питоне")
root.geometry ("320x500")


en = Entry (root, width = 30, #textvariable=info_b1_3
            )
en.pack()
en.grid(row=0, column=0, columnspan=3, padx=10)

#def get_info_b1_3():
 #   info_b1_3.get()

#info_b1_3 = StringVar()

def show_message():
    messagebox.showinfo("GUI Python", en.get())

btn_0 = Button(root, text = "0", font = "32", height = 2, width = 7, command = show_message)
btn_0.grid(row = 4, column = 1)
#Сдесь находятся другие кнопки
root.mainloop()