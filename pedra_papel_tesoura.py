import random

def jogo(): 
    usuario = input("Escolha um: pedra 'p', papel 'l' ou tesoura 't'?\n")
    maquina = random.choice(['p', 'l', 't'])
    
    # PEDRA > TESOURA, TESOURA > PAPEL, PAPEL > PEDRA
    def vitoria(jogador, oponente):
        if (jogador == 'p' and oponente == 't')  \
            or (jogador == 't' and oponente == 'l') \
            or (jogador == 'l' and oponente == 'p'):
            return True
    
    if usuario == maquina:
        return 'Empate :/'
    
    if vitoria(usuario, maquina):
        return 'Você ganhou!!!'
    
    return 'Você perdeu!'
    
print(jogo())