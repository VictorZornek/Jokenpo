# Jogo do Pedra, Papel e Tesoura (Jokenpô)

import random

class Jokenpo():
    def __init__(self):
        # Possibilidades de escolha
        self.escolha = [
            'pedra',
            'papel',
            'tesoura'
        ]

    def Iniciar(self):
        self.usuario = input('Escolha pedra, papel ou tesoura: ').lower()       # Escolha do usuário
        self.programa = random.choice(self.escolha)                             # Escolha randomica do programa
        print('Escolha do programa: ', self.programa)                           # Mostra a escolha do programa

        if (self.usuario == self.programa):
            print('Deu empate!')

        elif (self.usuario == 'pedra' and self.programa == 'tesoura') or (self.usuario == 'tesoura' and self.programa == 'papel') or (self.usuario == 'papel' and self.programa == 'pedra'):
            print('Você ganhou!')

        else: 
            print('Você perdeu!')

jogo = Jokenpo()
jogo.Iniciar()