#Verificar se X ano é bissexto
ano = int(input('Esse ano é bissexto? '))
if ano % 400 == 0:
    print(f'{ano} É ano bissexto!')
elif ano % 100 == 0:
    print(f'{ano} Não é ano bissexto')    
elif ano % 4 == 0:
    print(f'{ano} É ano bissexto!')
else:
    print(f'{ano} Não é ano bissexto')