from tkinter import *

window = Tk()
window.geometry("600x500")
window.title("Calculadora")
window.resizable(False, False)

numbers_label = Entry(window, width=30).place(x=40, y=60)
window.mainloop()
