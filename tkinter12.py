# from tkinter import *
# win = Tk()
# win.mainloop()

# from tkinter import *
# win = Tk()
# win.title("window")
# win.iconbitmap('123.ico')
# win.mainloop()

# from tkinter import *
# win = Tk()
# win.title("window")
# win.iconbitmap('123.ico')
# win.maxsize(width=266,height=200)
# win.minsize(width=300,height=200)
# win.mainloop()
# from tkinter import *
# win = Tk()
# win.title("window")
# win.iconbitmap('123.ico')
# win.maxsize(width=266,height=200)
# win.minsize(width=300,height=200)
# win.configure(bg="red")
# header = Button(win,text="click",fg="red")
# header.pack(side=LEFT)
# entername = Entry(win,width=50,bg="black" , fg="white")
# entername.pack(side=LEFT)
# entername.insert (0,"enter name")
# win.mainloop()

# from tkinter import *
# root =Tk()
# def myclick():
#     mylabel = Label(root,text="look i just clicked" , fg="white",bg="black",font=50)
#     mylabel.pack()
# my_button = Button (root,text="click me",padx=10,pady=10,command=myclick,fg="blue")
# my_button.pack()
# root.mainloop()



'''from tkinter import *

root = Tk()

redButton = Button(root, text = "Left", fg="green")
# packing it in the screen for showing
redButton.pack(side=LEFT)'''



# greenButton = Button(root, text = "Right", fg="green")
# # packing it in the screen for showing

# greenButton.pack(side=RIGHT)


# blueButton = Button(root, text = "Top", fg="blue")

# # packing it in the screen for showing
# blueButton.pack(side=TOP)
 
# blackButton = Button(root, text = "Bottom", fg="black")
# # packing it in the screen for showing

# blackButton. pack(side=BOTTOM)

# root.mainloop()




'''from tkinter import *
from PIL import Image,ImageTk
window=Tk()
my_image= ImageTk.PhotoImage(Image.open("Capture.png"))
mylabel= Label(image=my_image)
mylabel.pack()

buttonquit=Button(window,text="exit",command=window.quit,width=20)
buttonquit.pack()
window.mainloop()'''


'''from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title('Hessage Box')
root.iconbitmap('123.ico')
def popup():
     #showinfo messagebox
     messagebox.showinfo("This is my Popup", "Hello World!")
Button (root, text= "Popup",command=popup).pack()
mainloop()
'''

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root=Tk()
def popup ():
    
    response = messagebox.askyesno("This is my Popup", "Hello World!")
    Label(root, text=response) .pack()
    if response == 1:
         Label(root, text="Clicked Yes"). pack ()
    else:
         Label(root, text="Clicked No").pack()
Button (root, text="Popup",command=popup).pack()

mainloop()


