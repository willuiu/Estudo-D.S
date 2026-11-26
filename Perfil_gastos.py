GastoA = float(input('Digite o valor mensal gasto com Aluguel: '))
GastoM = float(input('Digite o valor mensal gasto com Mercado: '))
GastoT = float(input('Digite o valor mensal gasto com Transporte: '))
Total = GastoA + GastoM + GastoT
Media = Total / 3 
porcentagemA = GastoA / Total * 100
porcentagemM = GastoM / Total * 100 
porcentagemT = GastoT / Total * 100
print(f'Valores mensais gastos:Total: R${Total:.2f}, Media: R${Media:.2f}')

print(f'Porcentagem de gastos com Aluguel: {porcentagemA:.2f}%, Mercado: {porcentagemM:.2f}%, Transporte: {porcentagemT:.2f}%')