import tkinter as tk

fileSizeList = [
"Bytes",
"Kilobytes",
"Megabytes",
"Gigabytes"
] 

app = tk.Tk()

fileSize = ''

app.geometry('100x200')

sizeMenuVal = tk.StringVar(app)
sizeMenuVal.set(fileSizeList[0])

sizeMenu = tk.OptionMenu(app, sizeMenuVal, *fileSizeList)
sizeMenu.config(width=90, font=('Helvetica', 12))
sizeMenu.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    global fileSize
    fileSize = sizeMenuVal.get()

sizeMenuVal.trace("w", callback)

app.mainloop()