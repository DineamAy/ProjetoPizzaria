from tkinter import *
import time
import random
from tkinter import messagebox


class Pizza:

    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr = Tk()
        except:
            try:
                sf.scr = Tk()
            except:
                pass

        sf.scr.geometry("1366x768")
        sf.scr.title("Pizzaria Projeto")
        sf.scr.iconbitmap('p.ico')
        
        sf.mainf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.mainf2, height=618, width=1366)
        sf.c.pack()
        sf.back = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 284, image=sf.back)
        sf.mainf2.pack(fill=BOTH,expand=1)


        sf.scr.mainloop()

x=Pizza()
x.main()
