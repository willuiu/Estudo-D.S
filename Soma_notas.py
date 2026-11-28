#Soma de notas aleatorias
import random

notas = [random.uniform(-0.1, 10.1) for i in range(10)]
soma = 0
maior = notas[0]
menor = notas[0]
for nota in notas:
    soma = soma + nota
    if nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
media = soma / len(notas)
print(f'media: {media:.2f}, maior nota: {maior:.2f}, menor nota: {menor:.2f} ')