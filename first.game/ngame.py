import random
import os

def jogar(): #criando a funcao jogar
    nm = random.randint(0, 10)
    tentativa = 0
    cont = 0

    while tentativa != num: #fazendo o 'corpo do jogo'
        try:
            tentativa = int(input('digite um numero: '))
            if tentativa > num:
                print('o numero é menor ')
                cont += 1
            else:
                print('o numero é maior ')
                cont += 1
        except ValueError:
            print('digite algo valido ')
    print(f'Você ganhou o numero era {num}!! Você fez {cont} tentativas')

def jogarDeNovo(): #jogar denovo com condiçao de s ou n
    while True:
        jogar()
        repetir = input('\nVocê quer jogar de novo? (sim ou nao): ')
        if repetir == 'nao':
            print('vlw fera')
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif repetir == 'sim':
            continue
        else:
            print("Resposta inválida. Encerrando.")
            break

if __name__ == "__main__": #código que protege de invocar o script quando não deve/querem
    jogarDeNovo()