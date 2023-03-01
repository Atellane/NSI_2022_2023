class ControllerChatCPT():
	def __init__(self: object, model: object, view: object) -> object:
		self.model = model
		self.view = view

	def poserQuestion(self) -> None:
		self.view.poserQuestionUtilisateur(self.model.creationPhrase, self.model.choixAleatoireImage)
