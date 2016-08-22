pontov1 = int(input('Digite os pontos de vida do jogador 1: '))
pontov2 = int(input('Digite os pontos de vida do jogador 2: '))
print("""Pontos de vida do jogador 1: {0}
Pontos de vida do jogador 2: {1}""" .format(pontov1, pontov2))

while pontov1 != 0 and pontov2 != 0:
    dano = str(input("O dano será causado por Cartas de Feitiço/Efeito ou por Batalha? (E, B) "))
    if dano == "B" or dano == "b":
        jogat = str(input('Qual jogador está atacando? (1, 2) '))
        if jogat == "1":
            atck1 = int(input("Qual o poder de ataque da carta atacando? "))
            def1 = int(input("Qual o poder de ataque da carta defendendo? "))
            def2 = int(input("Qual o poder de defesa da carta defendendo? "))
            modo1 = str(input("A carta defendendo está em modo de ataque ou defesa? (Ataque, Defesa) "))
            if modo1 == "Ataque":
                if atck1 > def1:
                    pontov2 = pontov2 - (atck1 - def1)
                elif atck1 == def1:
                    pontov2 = pontov2
                else:
                    pontov1 = pontov1 - (def1 - atck1)
            elif modo1 == "Defesa":
                if atck1 > def1:
                    pontov2 = pontov2
                elif atck1 == def1:
                    pontov2 = pontov2
                else:
                    pontov1 = pontov1 - (def2 - atck1)
        elif jogat == "2":
            atck1 = int(input("Qual o poder de ataque da carta atacando? "))
            def1 = int(input("Qual o poder de ataque da carta defendendo? "))
            def2 = int(input("Qual o poder de defesa da carta defendendo? "))
            modo1 = str(input("A carta defendendo está em modo de ataque ou defesa? (Ataque, Defesa) "))
            if modo1 == "Ataque":
                if atck1 > def1:
                    pontov1 = pontov1 - (atck1 - def1)
                elif atck1 == def1:
                    pontov1 = pontov1
                else:
                    pontov2 = pontov2 - (def1 - atck1)
            elif modo1 == "Defesa":
                if atck1 > def1:
                    pontov1 = pontov1
                elif atck1 == def1:
                    pontov1 = pontov1
                else:
                    pontov2 = pontov2 - (def2 - atck1)
            else:
                print('Erro. Por favor responda com "Ataque" ou "Defesa".')
        else:
            print('Erro. Por favor responda com "1" ou "2".')
    elif dano == "E" or dano == "e":
        eff1 = str(input("O efeito afetará o jogador 1 ou 2? (1, 2) "))
        if eff1 == "1":
            eff2 = str(input("O efeito é de dano ou de cura? (D, C) "))
            if eff2 == "D" or eff2 == "d":
                eff3 = int(input("Qual o valor do dano causado? "))
                pontov1 = pontov1 - eff3
            elif eff2 == "C" or eff2 == "c":
                eff3 = int(input("Qual o valor da cura causada? "))
                pontov1 = pontov1 + eff3
            else:
                print ("Erro. Por favor responda com 'C' ou 'D'. ")
        elif eff12 == "2":
            eff2 = str(input("O efeito é de dano ou de cura? (D, C)"))
            if eff2 == "D" or eff2 == "c": #Malditos usuários
                eff3 = int(input("Qual o valor do dano causado? "))
                pontov2 = pontov2 - eff3
            elif eff2 == "C" or eff2 == "c":
                eff3 = int(input("Qual o valor da cura causada? "))
                pontov2 = pontov2 + eff3
            else:
                print ("Erro. Por favor responda com 'C' ou 'D'. ")
        else:
            print("Erro. Por favor responda com '1' ou '2'.")
    else:
        print("Erro. Por favor responda com 'B' ou 'E'. ")
    print("""Pontos de vida do Jogador 1: {0}
Pontos de vida do Jogador 2: {1}""" .format(pontov1, pontov2))

if pontov1 == 0 and pontov2 != 0:
    print("O jogo acabou. O vencedor é o Jogador 2. Parabéns!")
elif pontov2 == 0 and pontov1 != 0:
    print("O jogo acabou. O vencedor é o Jogador 1. Parabéns!")
else:
    print("O jogo acabou. O resultado é um empaate.")
