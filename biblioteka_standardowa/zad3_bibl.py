import tkinter


def koszt_przejazdu():
    dystans = int(entry_dystans.get())
    spalanie = float(entry_spal.get())
    cena = float(entry_cena.get())
    koszt = (dystans / 100) * spalanie * cena
    wynik.configure(text=f'{koszt} PLN')


root = tkinter.Tk()
root.columnconfigure(0, weight=1)

label_dystans = tkinter.Label(master=root, text='Dystans:')
label_dystans.grid(row=0, column=0)
entry_dystans = tkinter.Entry(master=root)
entry_dystans.grid(row=0, column=1, sticky=tkinter.EW)

label_spal = tkinter.Label(master=root, text='Spalanie:')
label_spal.grid(row=1, column=0)
entry_spal = tkinter.Entry(master=root)
entry_spal.grid(row=1, column=1, sticky=tkinter.EW)

entry_cena = tkinter.Ent

button = tkinter.Button(master=root, text='Oblicz', command=koszt_przejazdu)
button.grid(row=2, column=0)
root.mainloop()
