from tkinter import *


def click(event):
    text = event.widget.cget("text")
    if text == "C":
        scValue.set("")
        screen.update()

    elif text == "DEL":
        delete = scValue.get()
        scValue.set(delete[:-1])
        screen.update()

    elif text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Syntax Error"

        scValue.set(value)
        screen.update()

    else:
        scValue.set(scValue.get() + text)
        screen.update()


root = Tk()
# root.geometry("350x370")
root.minsize(350, 370)
root.maxsize(350, 370)
root.title("Aman's Calculator")
root.wm_iconbitmap("Calculator.ico")

scValue = StringVar()
scValue.set("")

screen = Entry(root, textvariable=scValue, font="Arial 40 italic", bg='lightgray')
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

f1 = Frame(root)
b = Button(f1, text="C", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="DEL", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="9", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="8", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="7", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root)
b = Button(f1, text="%", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="/", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="6", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="5", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="4", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root)
b = Button(f1, text="*", width=3, height=1, font="Arial 15", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="-", width=3, height=1, font="Arial 15", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="3", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="2", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="1", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root)
b = Button(f1, text="=", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="+", width=4, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text=".", width=3, height=1, font="Arial 14 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="0", width=12, height=2, font="Arial 10 bold", bg='gray')
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()

root.mainloop()
