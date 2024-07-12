# Curso 02 Python - Avançando na linguagem
# Estrutura de dados em lista ex: lista = [] 
# Estrutura tupla imutavel ex: tupla = () 

import random

arquivo = open("/home/runner/forca/base.txt", "r")
   
lista_palavras = []

for linha in arquivo:
    lista_palavras.append(linha.strip())
aleatorio = random.randrange(0,len(lista_palavras))

fecha_arquivo()
tela()

palavra_secreta = lista_palavras[aleatorio]
enforcou = False
acertou = False
tentativas = 1
estrutura_armazena = ['_' for letra in palavra_secreta]

while (not enforcou and not acertou):

    chute = input('Qual a Letra.: ').lower()
    chute = chute.strip()
    index = 0 
    for letra in palavra_secreta:
        if (chute == letra):
            estrutura_armazena[index] = chute
        index += 1 
    if (tentativas == 10):
        enforcou = True
        print('GAME OVER ENFORCADO ; PALAVRA SECRETA É {}'.format(palavra_secreta))
    tentativas += 1
    acertou = '_' not in estrutura_armazena
    if (acertou):
       print('ESCAPOU DA FORCA!!!')
    print(estrutura_armazena)

def tela():
    print('***********************')
    print('* BEM VINDOS FOCA 1.0 *')
    print('***********************')

def fecha_arquivo():
    arquivo.close()

#if (__name__ == '__main__'):
#    foca()