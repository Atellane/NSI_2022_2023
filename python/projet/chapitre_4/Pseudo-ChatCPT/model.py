from PIL import Image
from random import randrange

class ModelChatCPT():
	def __init__(self: object) -> object:
		self.sujet: list = ["Le chat", "Le chien", "L'oiseau", "Le professeur", "L'étudiant", "Le cuisinier",\
							"L'artiste", "Le musicien", "Le jardinier", "L'architecte", "L'enfant", "Le médecin",\
							"L'infirmière", "Le facteur", "Le policier", "L'homme d'affaires", "La femme au foyer",\
							"Le footballeur", "Le joueur de tennis", "L'athlète", "L'acteur", "Le réalisateur",\
							"Le danseur", "Le voyageur", "Le touriste", "L'homme politique", "Le militant", "L'humanitaire",\
						 	"Le bénévole", "Le retraité"]
		self.verbe: list = ["mange", "boit", "dort", "court", "marche", "chante", "danse", "joue", "compose",\
							"construit", "crée", "enseigne", "soigne", "aime", "déteste", "discute", "voyage",\
							"écrit", "lit", "regarde", "écoute", "téléphone", "envoie", "reçoit", "achète",\
							"vends", "travaille", "rêve", "pense", "espère"]
		self.complement: list = ["de la pizza", "de la musique", "dans le livre", "dans la ville", "sur la mer", "dans le ciel",\
								 "avec les fleurs", "du gâteau", "sur le film", "sur le spectacle", "sur la pièce de théâtre",\
								 "sur le tableau", "sur le monument", "sur la montagne", "sur le parc", "sur le musée", "dans la maison",\
								 "sur le téléphone", "sur le mail", "sur la lettre", "sur l'invitation", "sur le cadeau",\
								 "sur le projet", "sur le plan", "sur le document", "sur l'ordinateur", "sur le portable", "dans la voiture",\
								 "dans l'avion", "dans le train"]
		self.image: list = []
		for i in range(20):
			self.image.append(Image.open(f"images/image_{i+1}.jpg"))

	def creationPhrase(self: object) -> str:
		"""crée une phrase"""
		phrase: str = f"{self.sujet[randrange(len(self.sujet))]} {self.verbe[randrange(len(self.verbe))]} {self.complement[randrange(len(self.complement))]}"
		return phrase

	def choixAleatoireImage(self: object) -> object:
		"""choisi une image au hasard dans la liste des images disponibles (images téléchargées à partir du script "banque_image_libre_droit.py")"""
		imageChoisie: object = self.image[randrange(len(self.image))]
		return imageChoisie
