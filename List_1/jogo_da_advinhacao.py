import random
from sre_constants import RANGE


print('\n**********************************')
print('Bem vindo ao jogo da advinhação!!!')
print('********************************** \n')
numero_secreto= random.randrange(1,101)
numero_tentativas=0
pontuacao=1000
print('Qual o nível do jogo?')
print('(1) Fácil | (2) Médio | (3) Difícil')
nivel =int(input('Defina o nível: '))
print(numero_secreto)
if(nivel==1): numero_tentativas=20
elif(nivel==2): numero_tentativas=15
else: numero_tentativas=10
for contador in range(1,numero_tentativas+1):
    print(f'Tentativa {contador} de {numero_tentativas}')
    numero_chute = int(input('Digite um número de 1 - 100: '))
    print(f'Você digitou: {numero_chute}')
    if(numero_chute<1 or numero_chute>100):
        print('Você digitiou um número fora do intervalo \n')
        continue
    acerto = numero_chute==numero_secreto
    maior=numero_chute>numero_secreto
    pontuacao=pontuacao-abs(numero_chute-numero_secreto)
    if(acerto):
        print('\n---------------------')
        print('Parabéns, você acertou!')
        print('---------------------\n')
        break
    elif(maior):
        print('Seu chute foi maior que o número secreto! \n')
    else:
        print('Seu chute foi menor que o número secreto! \n')
print(f'Sua pontuação é {pontuacao}')
print('\n############')
print('Fim de jogo!')
print('############')
