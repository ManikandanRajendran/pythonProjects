import urllib.parse
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import clipboard


root = Tk()
root.geometry("800x400")
root.title('URL Encoder and Decoder')
root.configure(bg='light blue')
Img1 = 'images/exit.png'
Img2 = 'images/clear.png'
image = Image.open(Img1)
img = image.resize((50, 50), Image.ANTIALIAS)
exitImg = ImageTk.PhotoImage(img)
image = Image.open(Img2)
img = image.resize((50, 50), Image.ANTIALIAS)
clearImg = ImageTk.PhotoImage(img)
output = Entry
copy_link1 = Button


def clear():
    global e1
    e1.delete(0, 'end')
    output.destroy()
    copy_link1.destroy()
    messagebox.showinfo("clear", "Values cleared")


def loadingCopyLink(value):
    global copy_link1
    copy_link1 = Button(root, text="copy", fg="white", bg="green", width=8, font=("arial", 7, "bold"))
    copy_link1.config(command=clipboard.copy(value))
    copy_link1.place(x=700, y=260)


def outputText(value):
    global output
    var1 = StringVar()
    output = Entry(root, width=80, textvariable=var1)
    var1.set(value)
    output.place(x=100, y=220)
    loadingCopyLink(value)


def decode():
    try:
        output.destroy()
        copy_link1.destroy()
    except:
        pass
    str1 = e1.get()
    if str1 == "":
        messagebox.showinfo("No Input Alert", "Please enter the text !!")
    else:
        text = urllib.parse.unquote(str1)
        outputText(text)


def encode():
    try:
        output.destroy()
        copy_link1.destroy()
    except:
        pass
    str1 = e1.get()
    if str1 == "":
        messagebox.showinfo("No Input Alert", "Please enter the text !!")
    else:
        text = urllib.parse.quote(str1)
        outputText(text)


def exit1():
    MsgBox = messagebox.askquestion('Exit application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        exit()


inputLabel = Label(root, text='Enter your input', bg="light blue", fg="gray21", font=("arial", 16, "bold"))
inputLabel.place(x=10, y=50)

var = StringVar()
e1 = Entry(root, width=60, textvariable=var)
e1.place(x=200, y=50)

decodeButton = Button(root, text='Decode', width=20, command=decode)
decodeButton.place(x=200, y=120)

encodeButton = Button(root, text='Encode', width=20, command=encode)
encodeButton.place(x=450, y=120)

clearButton = Button(root, text="clear", image=clearImg, width=40, command=clear)
clearButton.place(x=650, y=320)

exitButton = Button(root, text="Exit", image=exitImg, width=40, command=exit1)
exitButton.place(x=720, y=320)


root.mainloop()
