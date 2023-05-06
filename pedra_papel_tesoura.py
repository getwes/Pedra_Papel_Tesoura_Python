import random

opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}

ganhou = 'vc ganhou'

perdeu = 'vc perdeu'

while True:
    sua_escolha = input('pedra, papel ou tesoura')
    num = random.randint(1,3)
    escolha_pc = opcoes[num]

    