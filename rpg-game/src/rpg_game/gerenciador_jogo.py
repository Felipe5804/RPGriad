from guerreiro import Guerreiro
from mago import Mago
from arqueiro import Arqueiro
from comum import Comum
from personagem import Personagem

# Criando os lutadores
while True:
    nome_heroi = str(input("Escolha o nome do herói: "))
    classe = int(input(f"CLASSES:\n1-indigente\n2-Guerreiro\n3-Mago\n4-Arqueiro\nEscolha a classe do herói: "))
    if classe == 1:
        heroi = Comum(nome_heroi, 100, 15, 5)
        break
    elif classe == 2:
        heroi = Guerreiro(nome_heroi, 120, 10, 5)
        break
    elif classe == 3:
        heroi = Mago(nome_heroi, 80, 20, 5)
        break
    elif classe == 4:
        heroi = Arqueiro(nome_heroi, 80, 20, 5)
        break
    else:
        print("Opção de classe inválida. Tente novamente.")

vilao = Comum("Orc Lider", 80, 12, 5)

#rodadas para o ataque especial estar disponível
cooldown_especial = 0
#quantidade de poções
pocoes = 3
#rodadas para a defesa estar disponível
cooldown_defesa = 0
#define se ataque será defendido ou não
defesa = False

print("⚔️ A BATALHA COMEÇOU! ⚔️")

while heroi.esta_vivo() and vilao.esta_vivo():
    heroi.status()
    vilao.status()
    
    # Turno do Herói
    while True:
        print(f"1 - Ataque Básico\n2 - Ataque Especial\n3 - Defesa\n4 - Usar Poção")
        decisao = int(input("Selecione a próxima ação: "))

        if decisao == 1:
            if isinstance(heroi, Mago):
                heroi.regenerar_mana()
            heroi.atacar(vilao)
            break

        elif decisao == 2:
            if cooldown_especial <= 0:
                if hasattr(heroi, "usar_especial"):
                    cooldown_especial = 3
                    heroi.usar_especial(vilao)
                    break
                else:
                    print("Esse personagem não tem especial!")
            else:
                print(f"Especial em cooldown. Faltam {cooldown_especial} turnos. Escolha outra opção.")
        elif decisao == 3:
            if cooldown_defesa <=0:
                if isinstance(heroi, Mago):
                    heroi.regenerar_mana()
                cooldown_defesa = 5
                defesa = True
                print("Mitigou o dano causado pelo próximo ataque inimigo.")
                break
            else:
                print(f"Defesa em cooldown. Faltam {cooldown_defesa} turnos. Escolha outra opção.")
        elif decisao == 4:
            if pocoes >= 1:
                pocoes -= 1
                heroi.usar_pocao(pocoes)
            else:
                print(f"Sem poções disponíveis!")
        else:
            print("Opção inválida. Tente novamente.")
    
    if vilao.esta_vivo():
        # Turno do Vilão
        if heroi.esquivar():
            print("Esquivou!")
        else:
            if defesa == True:
                print("O herói desviou.")
            else:
                vilao.atacar(heroi)

    #diminui a quantidade de turnos para as ações
    cooldown_defesa -= 1
    cooldown_especial -= 1

    print("-" * 30)

print("FIM DE JOGO!")
