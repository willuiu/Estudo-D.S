#Adivinhe o número
import random

numero_aleatorio = random.randint(1, 100)
numero = int(input("Qual é o numero secreto? "))
tentativas = 1
while numero != numero_aleatorio:    
    if numero > numero_aleatorio:
        print("Tente um numero menor")
    elif numero < numero_aleatorio:
        print("Tente um numero maior")
    numero = int(input("Qual é o numero secreto? ")) 
    tentativas = tentativas + 1 
print('Você acertou!')
if tentativas == 1:
    print("Você acertou de primeira!")
else:
    print(f'Você precisou de: {tentativas} tentativas.')