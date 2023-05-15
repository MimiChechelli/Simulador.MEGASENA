import random

print('-------------------------------')
print("           MEGASENA")
print('-------------------------------')

x = int(input('Quantos jogos devem ser sorteados? '))

print('-------sorteando',x,'jogos-------')

for i in range(x):
    
    aleatorio = list()
    aleatorio = random.sample(range(1, 61), 6)
    aleatorio.sort()
    print('Jogo',i+1,':',aleatorio)
    aleatorio.clear()

print('-Boa Sorte a todos os jogadores!-')