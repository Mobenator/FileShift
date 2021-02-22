import tkinter 
from tkinter import *
  
  
def isInt(input): 
      
    if input.isdigit(): 
        print(input) 
        return True              
    elif input == "": 
        print(input) 
        return True
    else: 
        print(input) 
        return False
                          
root = Tk() 
  
e = Entry(root) 
e.place(x = 50, y = 50) 
reg = root.register(isInt) 
  
e.config(validate ="key",  
         validatecommand =(reg, '%P')) 
  
root.mainloop() 