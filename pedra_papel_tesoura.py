import PySimpleGUI as sg
import random

# Lógica do jogo
def jogo(jogada_usuario): 
    jogada_usuario = jogada_usuario.lower()
    jogada_maquina = random.choice(['p', 'l', 't'])
    print(jogada_usuario, jogada_maquina)
    
    # PEDRA > TESOURA, TESOURA > PAPEL, PAPEL > PEDRA
    def vitoria(jogador, oponente):
        if (jogador == 'p' and oponente == 't')  \
            or (jogador == 't' and oponente == 'l') \
            or (jogador == 'l' and oponente == 'p'):
            return True
    
    if jogada_usuario == jogada_maquina:
        return 'Empate...'
    
    if vitoria(jogada_usuario, jogada_maquina):
        return 'Você ganhou!!!'
    
    return 'Você perdeu :C'

# Configuração de layout da janela
sg.theme('Reddit')
layout = [
    [sg.Text("Escolha um: Pedra 'P', Papel 'L' ou Tesoura 'T'.")],
    [sg.Text("Digite a sua escolha:"), sg.Input(key = 'usuario', size=(5,1))],
    [sg.Button('Jogar'), sg.Button('Sair')],
]

# Configuração da janela do jogo
janela = sg.Window('Pedra, papel ou tesoura', layout)

while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Jogar':
        sg.popup('Resultado da partida', jogo(valores['usuario']))
    
    if eventos == 'Sair':
        break 

    
janela.close()