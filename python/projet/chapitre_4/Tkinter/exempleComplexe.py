from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, Canvas, PhotoImage, BitmapImage, Entry
import tkinter.font as tkFont

fenetrePrincipale: object = Tk()
fenetrePrincipale.title("Ma première fenêtre avec Tkinter")

ouvrirImage: object = Image.open("crylia.png")
imageForTkinter: object = ImageTk.PhotoImage(image=ouvrirImage)
font: object = tkFont.Font(family="DroidSansMono Nerd Font", weight="normal")

for i in range(9):
	fenetrePrincipale.rowconfigure(i, weight=1)
	fenetrePrincipale.columnconfigure(i, weight=1)

texte: object = Label(fenetrePrincipale, text="", font=font)

boutonQuitter: object = Button(fenetrePrincipale, text="quitter",  font=font, borderwidth=5, relief="raised", command=fenetrePrincipale.quit)
boutonQuitter.grid(row=1, column=4)

def bienAfficherRetourMethodeInfo(methode: tuple or dict or list or str, nomMethode: str) -> str:
	result: str = ""
	match nomMethode:
		case "grid_bbox":
			result = f"boite englobante: x = {methode[0]}, y = {methode[1]}, colonne = {methode[2]}, ligne = {methode[3]}"
		case "grid_info":
			for i in methode.keys():
				result = f"{i}: {methode[i]}, "
		case "grid_size":
			result = f"Le système de grille de fenetrePrincipale contient {methode[0]} colonnes et {methode[1]} lignes."
		case "gride_slaves":
			nombreWidget: int = len(methode)
			result += f"fenetrePrincipale contient {nombreWidget} widgets :"
			for i in range(len(methode)):
				result += f" {methode[i]}"
		case None:
			result = methode
	return result

def changerTexte(methode: tuple or dict or list or str, nomMethode: str) -> str:
	texte.grid_forget()
	texte["text"] = bienAfficherRetourMethodeInfo(methode, nomMethode)
	texte.grid(row=0, column=4)

def changerTexte(methode: tuple or dict or list or str, nomMethode: str) -> str:
	texte.grid_forget()
	texte["text"] = bienAfficherRetourMethodeInfo(methode, nomMethode)
	texte.grid(row=0, column=4)

nePlusAfficherBoutonQuitterSansOublierLesCoordonnées: object = Button(fenetrePrincipale, text="ne plus afficher le bouton quitter sans perdre les coordonnées", font=font, borderwidth=5, relief="sunken", command=boutonQuitter.grid_remove)
nePlusAfficherBoutonQuitterSansOublierLesCoordonnées.grid(row=2, column=4)

nePlusAfficherBoutonQuitterEnOubliantLesCoordonnées: object = Button(fenetrePrincipale, text="ne plus afficher le bouton quitter en perdant les coordonnées",  font=font, borderwidth=5, relief="groove", command=boutonQuitter.grid_forget)
nePlusAfficherBoutonQuitterEnOubliantLesCoordonnées.grid(row=3, column=4)

afficherBoutonQuitter: object = Button(fenetrePrincipale, text="afficher le bouton quitter",  font=font, borderwidth=5, relief="ridge", command=boutonQuitter.grid)
afficherBoutonQuitter.grid(row=4, column=4)

obtenirListeOptionBoutonQuitter: object = Button(fenetrePrincipale, text="afficher la liste des options de la grille de boutonQuitter",  font=font, borderwidth=5, relief="raised", command=lambda: changerTexte(boutonQuitter.grid_info(), "grid_info"))
obtenirListeOptionBoutonQuitter.grid(row=5, column=4)

obtenirInfoGrilleFenetrePrincipale: object = Button(fenetrePrincipale, text="afficher le nombre de ligne et de colonne de la grille de fenetrePrincipale",  font=font, borderwidth=5, relief="sunken", command=lambda: changerTexte(fenetrePrincipale.grid_size(), "grid_size"))
obtenirInfoGrilleFenetrePrincipale.grid(row=6, column=4)

obtenirWidgetsGeresParFenetrePrincipale: object = Button(fenetrePrincipale, text="afficher la liste de wigets gérés par fenetrePrincipale",  font=font, borderwidth=5, relief="groove", command=lambda: changerTexte(fenetrePrincipale.grid_slaves(), "gride_slaves"))
obtenirWidgetsGeresParFenetrePrincipale.grid(row=7, column = 4)

bitmap: object = BitmapImage(file="defaultpfp.xbm", background="white")
affichageBitmap: object = Label(fenetrePrincipale, image=bitmap)
# testBitmap.create_bitmap(185, 135, bitmap="@defaultpfp.xbm")
affichageBitmap.grid(row=4, column=0)

imageAffichage: object = Label(fenetrePrincipale, image=imageForTkinter)
imageAffichage.grid(row=4, column=8)

testChampsDeSaisi: object = Entry(fenetrePrincipale)

def changerTexteEvt(evt) -> str:
	texte.grid_forget()
	texte["text"] = bienAfficherRetourMethodeInfo(testChampsDeSaisi.get(), None)
	testChampsDeSaisi.delete(0, len(testChampsDeSaisi.get()) + 1)
	texte.grid(row=0, column=4)

testChampsDeSaisi.bind("<KeyPress-Return>", changerTexteEvt)
testChampsDeSaisi.grid(row=0, column=0)

fenetrePrincipale.mainloop()