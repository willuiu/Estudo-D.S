peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}, você esta abaixo do peso')
elif imc < 25.0:
    print(f'Seu IMC é: {imc:.2f}, você esta com o peso normal')
elif imc < 30.0:
    print(f'Seu IMC é: {imc:.2f}, você esta com sobrepeso')
elif imc < 35.0:
    print(f'Seu IMC é: {imc:.2f}, você esta com obesidade I')
elif imc < 40.0:
    print(f'Seu IMC é: {imc:.2f}, você esta com obesidade II')
else:
    print(f'Seu IMC é: {imc:.2f}, você esta com obesidade III')