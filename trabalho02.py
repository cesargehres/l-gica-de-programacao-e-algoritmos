print('Bem vindo a Loja de Gelados do César Gehres')

# Cardápio
print(f'{19 * "-"} Cardápio {20 * "-"}')
print(49 * '-')
print('---|  Tamanho  |  Cupuaçu (CP) |  Açaí (AC)  |---')
print('---|     P     |    R$  9,00   |  R$ 11,00   |---')
print('---|     M     |    R$ 14,00   |  R$ 16,00   |---')
print('---|     G     |    R$ 18,00   |  R$ 20,00   |---')
print(49 * '-')

total = 0

# Looping que só finaliza ao ter feito todos os pedidos desejados
while True:
    sabor = ''
    tamanho = ''
    # Entradas de sabor e tamanho e validação das mesmas
    sabor = str(input('Sabor desejado (CP/AC): ')).upper()
    if (sabor not in ('AC', 'CP')):
        print('Sabor inválido. Tente novamente\n')
        continue

    tamanho = str(input('Tamanho desejado (P/M/G): ')).upper()
    if  (tamanho not in ('P, M, G')):
        print('Tamanho inválido. Tente novamente\n')
        continue

    # Recebe o valor do produto com base no sabor e no tamanho
    # Substitue o sabor pelo nome inteiro para futura utilização no console
    # Cupuaçu
    if (sabor == 'CP') and (tamanho == 'P'):
        valor = 9
        sabor = 'Cupuaçu'
    elif (sabor == 'CP') and (tamanho == 'M'):
        valor = 14
        sabor = 'Cupuaçu'
    elif (sabor == 'CP') and (tamanho == 'G'):
        valor = 18
        sabor = 'Cupuaçu'

    # Açaí
    elif (sabor == 'AC') and (tamanho == 'P'):
        valor = 11
        sabor = 'Açaí'
    elif (sabor == 'AC') and (tamanho == 'M'):
        valor = 16
        sabor = 'Açaí'
    elif (sabor == 'AC') and (tamanho == 'G'):
        valor = 20
        sabor = 'Açaí'

    # Adiciona valor do pedido ao total
    print(f'Você pediu um {sabor} no Tamnho {tamanho}: R$ {valor:.2f}')
    total += valor

    # Pergunta se quer continuar. E valida a resposta
    continuar = str(input('\nDeseja mais alguma coisa? (S/N): ')).upper()
    while continuar not in ('S', 'N'):
        print('Opção inválida. Selecione (S) para continuar ou (N) para parar.')
        continuar = str(input('Deseja mais alguma coisa? (S/N): ')).upper()

    if (continuar == 'N'):
        break
    elif (continuar == 'S'):
        continue


# Mostra o valor total dos pedidos
print(f'\nO valor total a ser pago: R$ {total:.2f}')
