from controller import ControllerChatCPT
from model import ModelChatCPT
from view import ViewChatCPT

mChatCPT: object = ModelChatCPT()
vChatCPT: object = ViewChatCPT()
cChatCPT: object = ControllerChatCPT(mChatCPT, vChatCPT)
cChatCPT.poserQuestion()
vChatCPT.fenetre.mainloop()