from time import sleep
from random import randint

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

opcao= int(input(print("\n\t\033[1;36mVamos jogar?!\n\t 1 - SIM\t\t 0 - NÃO\033[m\n\t>")))

while opcao != 0:
    print("\n  ", "\033[1;31m=-"*5, "VAMOS JOGAR JOKENPO!", "=-"*5)
    print('''\n\t\033[1;34m[ 0 ] PEDRA
    \n\t[ 1 ] PAPEL 
    \n\t[ 2 ] TESOURA''')
    jogador = int(input("\033\n\t[1;33mQUAL A SUA JOGADA ?\n\033[m\t>"))
    print("\n\t\033[1;35mJO")
    sleep(1)
    print("\n\tKEN")
    sleep(1)
    print("\n\tPO\033[m")
    sleep(1)
    print("\n    ", "\033[1;36m=-\033[m"*20)
    print("\n\tVocê escolheu: {}".format(lista[jogador]))
    print("\n\tO computador escolheu: {}".format(lista[computador]))
    print("\n    ","\033[1;36m=-\033[m"*20)


    if(computador== 0):#PEDRA
        if (jogador ==0):
            print("\n\tEMPATE")
        elif (jogador == 1):
            print("\n\tVocê GANHOU!")
        elif(jogador ==2 ):
            print("\n\tO computador GANHOU!")
    elif (computador== 1): #PAPEL
        if (jogador == 0):
            print("\n\tO computador GANHOU!")
        elif (jogador == 1):
            print("\n\tEMPATE!")
        elif (jogador == 2):
            print("\n\tVocê GANHOU!")
    elif (computador==2): #TESOURA
        if (jogador == 0):
                print("\n\tVocê GANHOU!")
        elif (jogador == 1):
            print("\n\tO computador GANHOU!")
        elif (jogador == 2):
            print("\n\tEMPATE!")

    opcao = int(input("\033[1;31m\n\tDeseja jogar novamente?\n\n\t 1 - SIM \t\t\t 0 - NÃO\n\t>\033[m"))
