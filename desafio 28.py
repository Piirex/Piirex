from random import randint

nome = str(input('Qual é o seu nome? '))
print(f'Okay! {nome}, eu estou escolhendo um número de 1 até 10. Você consegue adivinhar? ')
num_adivinhado = randint(1, 10)
num_tentativas = 3

for tentativa in range(1, num_tentativas + 1):
    num_escolhido = int(input('Escolha um número: '))
    if num_escolhido == num_adivinhado:
        print(f'Você acertou em {tentativa} tentatiivas! O número era {num_adivinhado}!')
        break
    elif num_escolhido > num_adivinhado:
        print('Escolha um número menor!')
    else:
        print('Escolha um número maior!')
else:
    print(f'Você perdeu. O número era {num_adivinhado}')
print(f'Obrigada por jogar, {nome}! Foi um prazer.')
