print('Bem-vindo a Loja do César Gehres')

#Recebe os valores a serem calculaldos.
valor = float(input('Valor do produto: '))
quant = int(input('Quantidade do produto: '))

#Calcula o valor total
total = valor * quant

#Recebe o valor para calcular a porcentagem do desconto.
if total < 2500:
    desconto = 0
elif total < 6000:
    desconto = 0.04
elif total < 10000:
    desconto = 0.07
else:
    desconto = 0.11

#Calcula o desconto.
total_com_desconto = total - (total * desconto)

#Mostra o resultado com e sem desconto no console
print(f'Valor SEM desconto: R${total:.2f}')
print(f'Valor COM desconto: R${total_com_desconto:.2f}')
