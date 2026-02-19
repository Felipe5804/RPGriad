from personagem import Personagem

class Comum(Personagem):

    def __init__(self, nome, vida, forca, mana):
        super().__init__(nome, vida, forca, mana)

    def usar_especial(self, oponente):
        print("Não possui especial! Realizando ataque básico!")
        self.atacar(oponente)
        return False