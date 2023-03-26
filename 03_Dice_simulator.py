import random
from tkinter import *

window=Tk() # creating plane windows
window.minsize(600,600)
window.maxsize(600,600)
window.title('Roll The Dice')

label=Label(window,font=('bold',200)) 

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}{random.choice(number)}')
    label.pack()
    
heading=Label(window,text='Roll The Dice',font=('bold',50),bg='light cyan')
heading.pack(fill=X)

button=Button(window,text='lets roll....',font=('normal',25),command=lambda:roll())
button.pack()
window.mainloop() 
          
# closing of the program

