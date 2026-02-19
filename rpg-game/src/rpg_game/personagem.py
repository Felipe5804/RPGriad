import random
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome:str, vida:int, forca:int, mana:int)->None:
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.mana = mana

    def status(self)->None:
        print(f"--- {self.nome} | Vida: {self.vida} | Força: {self.forca} | Mana: {self.mana} ---")

    def esta_vivo(self)->bool:
        return self.vida > 0
        
    def receber_dano(self, dano:int)->None:
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"☠️ {self.nome} foi derrotado!☠️")

    def atacar(self, oponente):
        dano = self.forca + random.randint(1, 5)
        print(f"⚔️ {self.nome} atacou {oponente.nome} e causou {dano} de dano!")
        oponente.receber_dano(dano)

    def esquivar(self)->None:
        esquiva = random.randint(1, 10)
        if esquiva == 1:
            return True
        else:
            return False
        
    @abstractmethod
    def usar_especial(self):
        pass
        
    def usar_pocao(self, usos:int)->None:
            self.vida += 8
            print(f"Utilizou uma poção e curou 8 de vida, restando {usos} poção(ões). Não custou nenhum turno.")
