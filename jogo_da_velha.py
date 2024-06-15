# Atividade 4, Jogo da Velha
contador = 0
vencedor = False

print('Jogo da Velha')
print('Antes de iniciarmos o jogo, saiba que ao realizar suas jogadas:')
print('• O número 0(zero) respresenta a primeira linha/coluna; \n• 1(um) representa a segunda linha/coluna; e \n• 2(dois) representa a terceira linha/coluna.')

import random
jogador1 = random.choice(['X', 'O'])
print(f'Para realizar a primeira jogada, aleatoriamente o jogador que optou pelo {jogador1} foi escolhido.')

grade = [[' ' for _ in range(3)] for _ in range(3)]
def imprimir_grade():
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(grade[i][j], end=" | ")
            else:
                print(grade[i][j])
        if i < 2:
            print("---------")

while contador < 9 and not vencedor:
    imprimir_grade()
    print(f"Jogador {jogador1}, é sua vez.")
    linha = int(input("Insira a linha: "))
    coluna = int(input("Insira a coluna: "))
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Você inseriu um número que não corresponde a nenhuma linha ou coluna, tente novamente.")
        continue
    
    if grade[linha][coluna] == ' ':
        grade[linha][coluna] = jogador1
        contador += 1
        
        for i in range(3):
            if grade[i][0] == grade[i][1] == grade[i][2] == jogador1:
                vencedor = True
                break

        for i in range(3):
            if grade[0][i] == grade[1][i] == grade[2][i] == jogador1:
                vencedor = True
                break
        
        if grade[0][0] == grade[1][1] == grade[2][2] == jogador1:
            vencedor = True
        if grade[0][2] == grade[1][1] == grade[2][0] == jogador1:
            vencedor = True
        
        if vencedor:
            imprimir_grade()
            print(f"Jogador {jogador1} venceu!")
        else:
            if jogador1 == 'X':
                jogador1 = 'O'
            else:
                jogador1 = 'X'
    else:
        print("Já foi realizada uma jogada neste espaço, tente novamente.")

if not vencedor:
    imprimir_grade()
    print("Empate.")
