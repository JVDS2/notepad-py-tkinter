from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tkinter.scrolledtext as tkscrolled

root = Tk()
root.geometry("600x600")
root.title("Notepad")

def newFile():
    global file
    root.title("Untitled - Notepad")
    entry.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
    if file == " ":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        f = open(file, "r")
        entry.delete(1.0, END)
        entry.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == " ":
        file = None
    else:
        f = open(file, "w")
        f.write(entry.get(1.0, END))
        f.close()

def exitFile():
    root.destroy()

entry = tkscrolled.ScrolledText(root, wrap=WORD, bg="#f5f9fa", font=("Heveltica", 14))
entry.pack(padx=10,pady=5,expand=TRUE, fill=BOTH)

menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar, tearoff=0)
file.add_command(label="New", command=newFile)
file.add_command(label="Save", command=saveFile)
file.add_command(label="Open", command=openFile)
file.add_separator()
file.add_command(label="Exit", command=exitFile)

menubar.add_cascade(label="File", menu=file)

root.mainloop()