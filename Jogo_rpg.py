from random import choice
import os

def main():
    print('UMA BUSCA CRISTALIZADA\n\n')
    print("\n---------------\n| |1-Iniciar| |\n---------------\n| |2-Regras | |\n---------------\n| | 3-Sair  | |\n---------------\n")
    try:
        entrar = int(input('\nEscolha aqui a opção: '))
        print("")
        
        if entrar == 1:
            os.system("cls")#Limpar o terminal
            player()#Iniciar o programa
            continuar()#Vai para a função perguntando se quer continuar ou não
        
        elif entrar == 2:
            os.system("cls")
            regras()

        elif entrar == 3:
            os.system("cls")
            fim()

        else:
            os.system("cls")
            print('Escolha 1, 2 ou 3')
            main()

    except ValueError:
        os.system("cls")
        print('Escolha 1, 2 ou 3')
        main()

def regras():
    print('Ola jogador!\nBem vindo ao jogo, são simples as regras\nentão não se preocupe\n\n1- Você é um guerreiro que tem que livrar o mundo do mal do Rei Caveira\n e pegar de volta o Cristal Mágico\n2- Você andará pelas salas e sempre com a opção de continuar ou não\n3- Vão ter salas com itens escondidos ou com monstros para lutar\n4- Tente achar o Rei Caveira, mas cuidado! Você pode não achar ele\nTenha um ótimo jogo\n')

    try:
        voltar = int(input('|4-Voltar|\n'))
        print('\n')
        if voltar == 4:
            os.system("cls")
            main()
        else:
            os.system("cls")
            print('Aperte 4 para sair!')
            regras()
    except ValueError:
        os.system("cls")
        print('Aperte 4 para sair!')
        regras()       

def continuar():
    print("\n\n----------------------------------------------------------------------------------------------------")
    print('Quer reiniciar?\n------     ------\n|1-SIM |   |2-NÂO |\n ------     ------\n')

    try:
        quer = int(input())
        if quer == 1: 
            os.system("cls")
            player()
            
        elif quer == 2:
            os.system("cls")
            print('Até a próxima!')

        else:
            os.system("cls")
            print('Tem que ser 1 ou 2')
            continuar()

    except ValueError:
        os.system("cls")
        print('Tem que ser 1 ou 2')
        continuar()

def player():
    print('Vamos começar\nVocê é Garoto ou Garota?\n')

    print('      _______     |    _________    \n'
          '   _/_________\_  |  _/___/ \___\_  \n'
          '  |\| O     O |/| | |\| O     O |/| \n'
          '    \__ --- __/   |  |\__ --- __/|  \n'
          '     /|_____|\    |  |_/| \ / |\_|  \n'
          '     -|__T__|-    |    -|_____|-    \n'
          '     --------     |     --------    \n'
          '    |1-Garoto|    |    |2-Garota|   \n'
          '     --------     |     --------    \n')

    try:
        escolha = int(input('Insira aqui: '))
        if escolha == 1:
            nome = input('Então garoto, insira seu nome:\n')
            print(f'Bem vindo {nome}')
        elif escolha == 2:
            nome = input('Então garota, insira seu nome:\n')
            print(f'Bem vindo {nome}')
        else:
            os.system("cls")
            print('Aperte 1 ou 2')
            player()
    except ValueError:
        os.system("cls")
        print('Aperte 1 ou 2')
        player()

    jogo()

def cenario():
    
    cont = 0
    lifeP1 = 15
    level = 1
    dinheiro = 0
    danos = [1, 2]
    loop = True

    while loop:
        os.system("cls")
        if cont == 14:
            boss(lifeP1, level, dinheiro, danos)
            loop = False

        else:
            inimigo = 5
            sala1 = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                       I                *      |  *        |\n'
                '|            |               __________________              |  **       |\n'
                '|            |  **          / ________________ \             |  *    II  |\n'
                '|            |   *         / /||||||||||||||||\ \            |  / \      |\n'
                '|   *        |            | |||||||||||||||||||| |           | ||\ \     |\n'
                '|  *         |            | || | | | | | | | | | |    **     | |||\ \    |\n'
                '|            |            | ||  |  |  |  |  |  | |      *    | ||||\ \   |\n'
                '|     **     |            | |                _____________   | |||||\ \  |\n'
                '|           *|    **      | |               /  - =   --_=  \ | ||| ||| | |\n'
                '|            |____________|_|     JOGADOR  |=======(o)======||*||    | |  |\n'
                '|     *    /                     ________  |________________| \||    | |  |\n'
                '|  *     /                    _/||||||||||\_                         | | |\n'
                '-------------------------------------------------------------------------'
            )

            sala2 = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                   DIFF:fÁCIL  /|\      *      |  *        |\n'
                '|            |                               |||             |  **       |\n'
                '|   II       |  **               ESQUELETO   |||             |  *    I   |\n'
                '|       / \  |   *                 ------  ==vOv==           |  / \      |\n'
                '|   *  / /|| |                   /  @  @  \  (|)             | ||\ \     |\n'
                '|  *  / /||| |                   \_  ^^  _/ //           **  | |||\ \    |\n'
                '|    / /|||| |               ( )  O \||/ O//             *   | ||||\ \   |\n'
                '|   / /||||| |                ||/ /= __ =\               *   | |||||\ \  |\n'
                '|  | || |||| |    **              \=/  \=/                   | ||| ||| | |\n'
                '|  | |    || |_____________________JOGADOR___________________| ||    | | |\n'
                '|  | |    ||/                    ________                     \||    | | |\n'
                '|  | |                        _/||||||||||\_                         | | |\n'
                '-------------------------------------------------------------------------'
            )

            sala3 = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                    DIFF:MÉDIA          *      |  *        |\n'
                '|            |                                               |  **       |\n'
                '|   I        |  **                  Zumbi                    |  *   II   |\n'
                '|       / \  |   *                 MMMMMM                    |  / \      |\n'
                '|   *  / /|| |                    / O  X \                   | ||\ \     |\n'
                '|  *  / /||| |                   \_  ^^  _/              **  | |||\ \    |\n'
                '|    / /|||| |               (w)   \_MM_/   (w)         *    | ||||\ \   |\n'
                '|   / /||||| |                ||/ /= \/ =\ \||           *   | |||||\ \  |\n'
                '|  | || |||| |    **              |=WW--=|                   | ||| ||| | |\n'
                '|  | |    || |____________________JOGADOR____________________| ||    | | |\n'
                '|  | |    ||/                    ________                     \||    | | |\n'
                '|  | |                        _/||||||||||\_                         | | |\n'
                '-------------------------------------------------------------------------'
            )
            
            mimico = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                   DIFF:???????         *      |  *        |\n'
                '|            |               __________________              |  **       |\n'
                '|   *        |  **          /________(O)________\            |  *   II   |\n'
                '|            |   *           WWWWWWWWWWWWWWWWWWW             |  / \      |\n'
                '|   *        |        (\ (\  MMMMMMMMMMMMMMMMMMM             | ||\ \     |\n'
                '|  *         |         (\_(\|___________________|        **  | |||\ \    |\n'
                '|        *   |          (__ (/    ___| |___                * | ||||\ \   |\n'
                '|            |            \_ /   ( \      _ )            *   | |||||\ \  |\n'
                '|       *    |    *        \ \  / / \/ \_/ \ \               | ||| ||| | |\n'
                '|            |______________\ \/ /  JOGADOR \ \--____________| ||    | | |\n'
                '|  *         /               \_ /________   / /               \||    | | |\n'
                '|          /                  _/||||||||||\_ /                       | | |\n'
                '-------------------------------------------------------------------------'
            )

            sala5 = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                 DIFF: MÁXIMA             *    |  *        |\n'
                '|            |                  LOBISOMEN                    |  **       |\n'
                '|   I        |  *                __                          |  *   *    |\n'
                '|       / \  |   *              3\_\                         |           |\n'
                '|   *  / /|| |                  3   \_                       |           |\n'
                '|  *  / /||| |               MMM    (-\ \__              **  |      *    |\n'
                '|    / /|||| |               \----       W/             *    |           |\n'
                '|   / /||||| |                _ \   VVV  \               *   |   **      |\n'
                '|  | || |||| |    *         VVV \/ /--     \                 |  *        |\n'
                '|  | |    || |_______________  \ JOGADOR VV  \_______________|           |\n'
                '|  | |    ||/                    ________                     \        * |\n'
                '|  | |                        _/||||||||||\_                     \       |\n'
                '-------------------------------------------------------------------------'
            )

            sala6 = (
                '-------------------------------------------------------------------------\n'
                '|           \ _______________________________________________ /          |\n'
                '|            |                   DIFF:NENHUMA         *      |  *        |\n'
                '|            |                                               |  **       |\n'
                '|   *        |  **             *                             |  *   II   |\n'
                '|            |   *                  SLIME                    |  / \      |\n'
                '|   *        |                     ___( \__                  | ||\ \     |\n'
                '|  *         |                    /  O   O  \            **  | |||\ \    |\n'
                '|        *   |                  (   °)--(°   )          *    | ||||\ \   |\n'
                '|            |                 (   \_____/    )          *   | |||||\ \  |\n'
                '|       *    |    *          (°  \_________/  °)             | ||| ||| | |\n'
                '|            |______________(     JOGADOR   °°  )____________| ||    | | |\n'
                '|  *         /                   ________                     \||    | | |\n'
                '|          /                  _/||||||||||\_                         | | |\n'
                '-------------------------------------------------------------------------'
            )

            sala = [sala1, sala2, sala3, sala5, sala6]
            escolha = choice(sala)
            cont += 1
            print("------------------------------------------------------------------------------------------------")
    ###############################################################################################################
            if escolha == sala1:
                print(f'Sala {cont}')
                print(escolha)
                print(f'Lv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDanos: {danos[0]} e crítico {danos[1]}\n')
                print('Um Bau no canto... Susupeito\nQuer dar uma olhada?\n ------     ------\n|1-SIM |   |2-NÂO |\n ------     ------\n')
                lp3 = True
                while lp3:
                    try:
                        escolher = int(input('Escolha aqui: '))
                        if escolher == 1:
                            olhadas = ['achou', 'nada']
                            olhada = choice(olhadas)
                            if olhada == 'achou': 
                                lista = ['objeto', 'moeda', 'mimico', 'nada']
                                objetos = choice(lista)

                                if objetos == 'objeto':
                                    obj = ['porção1', 'porção2']
                                    objeto = choice(obj)
                                    if objeto == 'porção1':
                                        print(f'Você achou uma porção de vida\nSeu Hp aumentou +5\n')
                                        print(f'Lv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDanos: {danos[0]} e crítico {danos[1]}\n')
                                        lifeP1 += 5
                                        lp3 = False
                                    elif objeto == 'porção2':
                                        print(f'Você tomou veneno\nSeu Hp diminuiu -3\n')
                                        print(f'Lv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDanos: {danos[0]} e crítico {danos[1]}\n')
                                        lifeP1 -= 3
                                        lp3 = False
                                    else:
                                        print('Deu B.O')
                                        lp3 = False

                                elif objetos == 'moeda':
                                    moedas = [1, 5, 25, 40, 65, 100]
                                    moeda = choice(moedas)
                                    dinheiro += moeda
                                    print(f'Você achou\nVocê tem: ${dinheiro}\n')
                                    print(f'Lv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDanos: {danos[0]} e crítico {danos[1]}\n')
                                    lp3 = False
                        
                                else:
                                    print('Você não encontra nada,\nmas a constante sensação de ser observado...\nnão deixa você!')
                                    print(f'\nLv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDano: {danos[0]} e crítico {danos[1]}\n')
                                    lp3 = False
                            else:
                                print('Não era nada!\n')
                                lp3 = False

                                lp4 = True
                                while lp4:
                                    try:
                                        print('Quer continuar?\n ------     ------\n|1-SIM |   |2-NÂO |\n ------     ------\n')
                                        continua = int(input('Escreva aqui: '))
                                        if continua == 1:
                                            os.system("cls")
                                            lp4 = False
                                            lp3 = False
                                        elif continua == 2:
                                            print('Devido as dificuldades você sai da caverna')
                                            lp4 = False
                                            lp3 = False
                                            loop = False
                                    except ValueError:
                                        print('Tem que ser 1 ou 2')

                    except ValueError:
                        print('Tem que ser 1 ou 2')
                        
    ###############################################################################################################
            else:
                print(f'Sala {cont}')
                print(escolha)
                if escolha == sala5:
                    inimigo += 15
                elif escolha == sala2:
                    inimigo += 5
                elif escolha == sala3:
                    inimigo += 10
                elif escolha == mimico:
                    inimigo += 25
                    print(f'Sala {cont}')
                    print(mimico)
                    inimigo += 30
                    print('O baú respira??')
                    print('Ele te mordeu!! -7 de HP\n')
                    lifeP1 -= 7
                else:
                    pass

                loop2 = True
                print(f'Lv: {level}\nHp: {lifeP1}\nMoedas: {dinheiro}\nDanos: {danos[0]} e crítico {danos[1]}\n\nInimigo: {inimigo}\n')
                print('Oh não! Você encontrou um monstro,\nprepare-se para a batalha!\n-----------------    ------------------\n| | 1-Atacar  | |    | |   2-Fugir  | |\n-----------------    ------------------\n')

                while loop2:
                    lp5 = True
                    while lp5:
                        try:
                            decisao = int(input('Escolha aqui: '))
                            golpes = ['Acertou!', 'Errou...']
                            acertos = ['Um golpe de um guerreiro', 'Acertou bem na cabeça',
                                    'Se ele tivesse vivo ele ia morrer na hora']
                            erros = ['Essa doeu...', 'Revide!'
                                    'Não deixe a morte vencer']

                            if decisao == 1:
                                golpe = choice(golpes)
                                print(golpe)

                                if golpe == 'Acertou!':
                                    acerto = choice(acertos)
                                    dano = choice(danos)
                                    inimigo -= dano

                                    if inimigo < 1:
                                        print('------------------------------------------------------------------------------------------------')
                                        inimigo = 0
                                        inimigo += 3
                                        level += 1
                                        lifeP1 += 10
                                        if level >= 2:
                                            add = danos[1] + 1
                                            danos.pop(0)
                                            danos.append(add)
                                            print(f'Seus ataques:\nSeu normal: {danos[0] - 1} -> {danos[0]}\nSeu crítico: {danos[1] - 1} -> {danos[1]}')
                                        
                                        print(f'\nSubiu de nível!!\n{level - 1} -> {level}\n\nSua vida aumentou!!\n{lifeP1 - 10} -> {lifeP1}\n\nVocê está mais forte!\nVocê ganhou!\n\nQuer continuar?\n ------     ------\n|1-SIM |   |2-NÂO |\n ------     ------\n')
                                        print('------------------------------------------------------------------------------------------------')
                                        lp6 = True
                                        while lp6:
                                            try:
                                                continua = int(input('Escreva aqui: '))

                                                if continua == 1:
                                                    os.system("cls")
                                                    print('Próxima sala então!\n')
                                                    lp6 = False
                                                    lp5 = False
                                                    loop2 = False
                                                elif continua == 2:
                                                    os.system("cls")
                                                    print('Você sai da caverna...\n')
                                                    fim()
                                                    lp6 = False
                                                    lp5 = False
                                                    loop2 = False
                                                    loop = False
                                                else: 
                                                    print('Tem quer ser 1 ou 2')
                                            except ValueError:
                                                print('Tem que ser 1 ou 2')
                                    else:
                                        os.system("cls")
                                        print(f'Sala {cont}')
                                        print(escolha)
                                        print(acerto)
                                        if dano == danos[0]:
                                            print(f'-{danos[0]} do inimigo\n')
                                            lp5 = False
                                        else:
                                            print(f'CRÍTICO!!!\n-{danos[1]} do inimigo\n')
                                            lp5 = False
                                        print('\n-----------------    ------------------\n| | 1-Atacar  | |    | |   2-Fugir  | |\n-----------------    ------------------\n')
                                        print(f'|HP: {lifeP1}|     |    |Inimigo: {inimigo}|\n')
                                        lp5 = False
                                    lp5 = False

                                else:
                                    erro = choice(erros)
                                    print(erro)
                                    danos2 = [1, 2, 3]
                                    dano2 = choice(danos2)
                                    lifeP1 -= dano2
                                    if lifeP1 < 1:
                                        print('---------------------------------------------------------------------------------------------------------------------------')
                                        print('\nCom o sangue na garganta...\nvocê se lembra da sua aventura até aqui...\nfoi um bom guerreiro...\n\nVocê perdeu...\n')
                                        print('---------------------------------------------------------------------------------------------------------------------------')
                                        lifeP1 = 0
                                        print(f'|HP: {lifeP1}|     |    |Inimigo: {inimigo}|\n')
                                        lp5 = False
                                        loop2 = False  
                                        loop = False

                                    else:
                                        os.system("cls")
                                        print(f'Sala {cont}')
                                        print(escolha)
                                        print(erro)
                                        if dano2 == 1:    
                                            print('O monstro devolveu... Ai!\n-1 de HP\n')
                                            lp5 = False
                                        elif dano2 == 2:
                                            print('Boa jogada do inimigo...\n-2 de HP\n')
                                            lp5 = False
                                        else: 
                                            print('Nossa, foi crítico...\n-3 de HP\n')    
                                            lp5 = False              
                                        print('\n-----------------    ------------------\n| | 1-Atacar  | |    | |   2-Fugir  | |\n-----------------    ------------------\n')
                                        print(f'|HP: {lifeP1}|     |    |Inimigo: {inimigo}|\n')
                                        lp5 = False

                            elif decisao == 2:
                                os.system("cls")
                                print('Sua coragem foi desimada,\ne você foge da batalha com vergonha\n')
                                lp5 = False
                                loop2 = False

                            else:
                                print('tem quer ser 1 ou 2!\n')   

                        except ValueError:
                            print('Tem que ser 1 ou 2')
                inimigo += 2
    fim()

def jogo():
    print('---------------------------------------------------------------------------------------')
    print('')
    print('Então, você entrou na Caverna das Almas\nPara derrotar o Rei Caveira e pegar seu Cristal Mágico!\n')

    try:
        press = int(input('Aperte 1 para continuar: '))
        if press == 1:
            os.system("cls")
            cenario()

        else:
            os.system("cls")
            print('Tem que aperta 1!')
            jogo()
    except ValueError:
        os.system("cls")
        print('Tem que aperta 1!')
        jogo()       

def boss(hp, lv, mn, dano):
    os.system("cls")
    final1 = (
        '-------------------------------------------------------------------------\n'
        '|           \ ____________________REI CAVEIRA________________ /          |\n'
        '|            |                       MMM              *      |  *        |\n'
        '|            |             ___     /[] []\   ___             |  **       |\n'
        '|   Ganhe    |  **        /   \ ___M| W |MM_/   \            |  *        |\n'
        '|Se for capaz|   *        \___/<____|MMM|__>\___/            |           |\n'
        '|   *        |           /  / / / W  O  W \ \ \  \           |  CUIDADO  |\n'
        '|  *         |          /  / /  \ = /\/\ = / \ \  \       *  |           |\n'
        '|            |         O--O /    \_/ || \_/   \ O--O     *   |           |\n'
        '|            |          \  \         ||        /  /     *    |           |\n'
        '|       *    |    **    /\__\    / O    O \   /__/\          |           |\n'
        '|            |________/(   )__________________(   )\_________|           |\n'
        '|           /            WWW      ________     WWW            \          |\n'
        '|        /                     _/||||||||||\_                    \       |\n'
        '-------------------------------------------------------------------------'
    )

    final2 = (
        '-------------------------------------------------------------------------\n'
        '|           \ _______________________________________________ /          |\n'
        '|            |                     SAÍDA              *      |  *        |\n'
        '|            |               __________________              |  **       |\n'
        '|   II       |  **          / ________________ \             |  *        |\n'
        '|            |   *         / /||||||||||||||||\ \            |           |\n'
        '|   *        |            | |||||||||||||||||||| |           |           |\n'
        '|  *         |            | || | | | | | | | | | |    **     |           |\n'
        '|            |            | ||  |  |  |  |  |  | |      *    |           |\n'
        '|            |            | |                  | |       *   |     **    |\n'
        '|            |    **      | |                  | |           |      *    |\n'
        '|            |____________|_|     JOGADOR      |_|___________|* *        |\n'
        '|           /                    ________                     \          |\n'
        '|        /                    _/||||||||||\_                    \        |\n'
        '-------------------------------------------------------------------------'
    )

    finais = [final1, final2]
    final = choice(finais)
    print("------------------------------------------------------------------------------------------------")
    print('Sala Final!')
    print(final)

    if final == final1:
        bosslife = hp + 30

        loop2 = True
        print(f'Lv: {lv}\nHp: {hp}\nMoedas: {mn}\n')
        print('Você está frente a frente com o inimigo mais forte!\nprepare-se para...\nMORRER!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n -----------------\n| | 1-Atacar  | |\n -----------------\n')

        while loop2:
            lp7 = True
            while lp7:
                try:
                    decisao = int(input('Escolha aqui: '))
                    golpes = ['Acertou!', 'Errou...']
                    acertos = ['Um golpe de um guerreiro', 'Acertou bem na cabeça',
                            'Se ele tivesse vivo ele ia morrer na hora']
                    erros = ['Essa doeu...', 'Revide!'
                            'Não deixe a morte vencer']

                    if decisao == 1:
                        golpe = choice(golpes)
                        print(golpe)

                        if golpe == 'Acertou!':
                            acerto = choice(acertos)
                            print(acerto)
                            danos = choice(dano)
                            bosslife -= danos

                            if bosslife < 1:
                                os.system("cls")
                                print('Subiu de nível!!\nSua vida máxima aumentou!!\nVocê ganhou!\n\nVocê livrou o mundo desse mal!\nRecuperou o cristal mágico')
                                print('\n  ________  \n'
                                    ' /\/\/\/\/\ \n'
                                    ' \  \  /  / \n'
                                    '  \__\/__/  \n'
                                    'O CRISTAL MÁGICO\n'
                                    )
                                lp7 = False
                                loop2 = False

                            else:
                                os.system("cls")
                                print('Sala Final!')
                                print(final)
                                print(acerto)
                                if danos == dano[0]:
                                    print(f'-{dano[0]} do Boss\n')
                                    lp7 = False
                                else:
                                    print(f'CRÍTICO!!!\n-{dano[1]} do Boss\n')
                                    lp7 = False

                                print('\n-----------------    ------------------\n| | 1-Atacar  | |    | |   2-Fugir  | |\n-----------------    ------------------\n')
                                print(f'|HP: {hp}|     |    |Inimigo: {bosslife}|\n')
                                lp7 = False

                        else:
                            erro = choice(erros)
                            print(erro)
                            danos2 = [5, 6, 8]
                            dano2 = choice(danos2)
                            hp -= dano2

                            if hp < 1:
                                print('Com o sangue na garganta...\nvocê se lembra da sua aventura até aqui...\nfoi um bom guerreiro...\n\nVocê perdeu...\n\nO Rei caveira dominou o mundo...\n')
                                lp7 = False
                                loop2 = False  

                            else:
                                os.system("cls")
                                print('Sala Final!')
                                print(final)
                                print(erro)
                                if dano2 == 5:    
                                    print('O Rei devolveu... Ai!\n-5 de HP')
                                    lp7 = False
                                elif dano2 == 6:
                                    print('Boa jogada do Rei...\n-6 de HP')
                                    lp7 = False
                                else: 
                                    print('Nossa, foi crítico...\n-8 de HP') 
                                    lp7 = False                 
                                print('\n-----------------    ------------------\n| | 1-Atacar  | |    | |   2-Fugir  | |\n-----------------    ------------------\n')
                                print(f'|HP: {hp}|     |    |Inimigo: {bosslife}|\n')
                                lp7 = False

                    else:
                        print('Não da para fugir...\nAperte 1 E MORRA!!!!!!!')
                except ValueError:
                    print('Não da para fugir...\nAperte 1 E MORRA!!!!!!!')

    else:

        print('\nVocê não achou o Cristal mágico...\nSua aventura foi em vão...\nMas você ganhou bastante experiência\n\nO Rei caveira dominou o mundo...\n')
    print(f'Seu level final: {lv}\nSeu HP final: {hp}\nQuantas moedas você tem: {mn}')

    fim()

def fim():
    print('--------------------------------------------------------------------------------------')
    print("Obrigado por jogar!\nAté próximas aventuras") 
    continuar()

main()
