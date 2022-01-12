import webbrowser
from tkinter import *

root = Tk( )

root.title ('Abre Navegador')
root.geometry('300x200')

def google():
    webbrowser.open('https://www.google.com')

mygoogle = Button(root, text='Abre Google', command=google).pack(pady=20)
root.mainloop()
