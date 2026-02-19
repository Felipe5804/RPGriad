from personagem import Personagem
import random
NUM_FLECHAS = 3

class Arqueiro(Personagem):

    def __init__(self, nome, vida, forca, mana):
         super().__init__(nome, vida, forca, mana)
        
    def usar_especial(self, oponente):
            dano = 0
            # 3 é número de flechas
            for i in range(NUM_FLECHAS):
                dano += random.randint(6,10)
            print(f"{self.nome} usou a Chuva de Flechas e causou {dano} de dano!")
            oponente.receber_dano(dano)
            return None