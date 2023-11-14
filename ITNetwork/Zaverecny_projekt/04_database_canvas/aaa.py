# -*- coding: utf-8 -*-

import tkinter as Tk

def overeni():
    print
    "nyni overuji text"
    return 1


def cteni():
    print
    vstupObsah.get()  # pristup pres tkPromennou
    print
    vstup.get()  # pristup pres metodu get instance Entry


hlavni = Tk()
hlavni.option_add('*Font', 'Arial 9')  # aby byl lepsi font

vstupObsah = StringVar()
vstupObsah.set("Žluťoučký kůň pěl ďáleské ódy.")

# obsah je napojen na tkProměnnou vstupObsah
# a při každém písmení probíhá ověřování
vstup = Entry(hlavni, textvariable=vstupObsah, width=40, validate="key",
              validatecommand=overeni)
vstup.pack(side=LEFT)
vstup.focus_set()  # aby se dalo hned psát
vstup.icursor(END)  # aby byl kurzor na konci
vstup.selection_range(0, END)

tlacitko = Button(hlavni, text=u"přečti", width=10, command=cteni)
tlacitko.pack()

mainloop()