from personagem import Personagem

class Guerreiro(Personagem):

    def __init__(self, nome, vida, forca, mana):
        super().__init__(nome, vida, forca, mana)

    def usar_especial(self):
        print(f"🛡️ {self.nome} usou o escudo e recuperou 10 de vida!")
        self.vida += 10
        return None