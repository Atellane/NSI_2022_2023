from model import ModelChatCPT
from view import ViewChatCPT
class ControllerChatCPT():
	@staticmethod
	def poserQuestion():
		view: object = ViewChatCPT()
		model: object = ModelChatCPT()
		view.poserQuestionUtilisateur(model.creationPhrase(), model.choixAleatoireImage())
