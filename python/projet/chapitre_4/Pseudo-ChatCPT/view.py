from tkinter import Tk, Label, Entry, PhotoImage
from PIL import Image, ImageTk
from typing import Callable

class ViewChatCPT():
	def __init__(self: object) -> object:
		self.fenetre: object = Tk()
		self.fenetre.title("Chat CPT")
		self.affichage: bool = False
		self.error = None

	def __effacerChampsDeSaisi(self: object) -> None:
		self.champDeSaisi.delete(0, len(self.champDeSaisi.get()) + 1)

	def __afficherReponse(self: object) -> None:
		if not self.affichage:
			self.affichage = True
		else:
			self.reponseTexte.destroy()
			self.reponseImage.destroy()
		imageChoisie: object = self.callbackImageChatCPT()
		self.photo: object = ImageTk.PhotoImage(image=imageChoisie)
		self.reponseTexte: object = Label(self.fenetre, text=f"ChatCPT: {self.callbackReponseDeChatCPT()}")
		self.reponseTexte.pack()
		self.reponseImage: object = Label(self.fenetre, image=self.photo)
		self.reponseImage.pack()
	
	def __reactionQuestionUtilisateur(self: object, evt: object):
		self.__effacerChampsDeSaisi()
		self.__afficherReponse()
	def poserQuestionUtilisateur(self: object, callbackReponseDeChatCPT: Callable[[None], str], callbackImageChatCPT: Callable[[None], object]) -> None:
		self.callbackReponseDeChatCPT: object = callbackReponseDeChatCPT
		self.callbackImageChatCPT: object = callbackImageChatCPT
		self.texte: object = Label(self.fenetre, text="Poser une question à ChatCPT:")
		self.texte.pack()
		self.champDeSaisi: object = Entry(self.fenetre)
		self.champDeSaisi.pack()
		self.champDeSaisi.bind("<KeyPress-Return>", self.__reactionQuestionUtilisateur)
