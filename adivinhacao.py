
# Jogo de adivinhação 

import random

def tela():
    print('*********************************')
    print('***Copyright By Araújo Family*** ')
    print('Bem Vindos ao Jogo de Adivinhação')
    print('*********************************')
    print()
    print(' (1) Fácil (2) Médio (3) Difícil')

def fim():
    print('***************')
    print(' GAME OVER!!!')
    print(' ------------')
    print('***************')

tela()
baixo = 1
alto = 50
arnanivel = int(input('Entre com o Nível..: '))

if (arnanivel == 1):
    tentativas = 10
elif (arnanivel == 2):
    tentativas = 5
else:
    tentativas = 3

arna_secreto = round(random.randint(baixo, alto))
pts = 1000

#while (contador <= tentativas):
for contador in range(1,tentativas+1):
    print('Tentativa..:[{}/{}]'.format(contador,tentativas)) # string interpolation
    arnapega = int(input('Digite o número entre [1] e [50].: '))

    if (arnapega < 1 or arnapega > 50):
        print('Fora da faixa')
        continue

    acertou = (arnapega == arna_secreto) 
    maior = (arnapega > arna_secreto)
    menor = (arnapega < arna_secreto)

    if (acertou):
        print('Parabens você acertou o número secreto, vc fez {} pontos '.format(pts))
        break
    else:
     if (maior):
          print('Haaa que pena, você errou!, seu chute foi Maior')
     elif (menor):
          print('Haaa que pena, você errou!, seu chute foi Menor')
    pts_decremento = abs(arnapega - arna_secreto)
    pts = pts - pts_decremento    
   # contador = contador + 1
fim()
print('SECRET NUMBER IS ..: {}'.format(arna_secreto))

