from tkinter import Tk, Button

fenetrePrincipale: object = Tk()
fenetrePrincipale.title("Ma première fenêtre avec Tkinter")

boutonQuitter: object = Button(fenetrePrincipale, text="Quitter", command=fenetrePrincipale.quit)

boutonQuitter.pack()

fenetrePrincipale.mainloop()