def escolha_servico():
    '''
    Imprime o menu e solicita uma entrada
    :return: Valor da opção.
    '''
    while True:
        print('\nEntre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        op = str(input('>>>')).upper()

        # Se op for valido, o valor do serviço
        if (op in ['DIG', 'ICO', 'IPB', 'FOT']):
            if (op == 'DIG'):
                return 1.10
            elif (op == 'ICO'):
                return 1
            elif (op == 'IPB'):
                return 0.40
            elif (op == 'FOT'):
                return 0.20

        else:
            print('Escolha inválida, entre com o tipo do serviço novamento')
            continue

def num_pagina():
    '''
    Solicita a quantidade de páginas de no maáximo 20000
    e da desconto com base no número de páginas.
    :return: número inteiro, por centagem do desconto.
    '''
    while True:
        # Solicita um número inteiro, e o valida
        try:
            quant = int(input('\nEntre com o número de páginas: '))
        except ValueError:
            print('Escolha inválida, digite um número inteiro válido.')
            continue
        except:
            print('Ocorreu um erro inesperado!')
            continue
        else:
            # Desconto com base no número de páginas
            if (quant < 20):
                desc = 0
            elif (quant < 200):
                desc = 15
            elif (quant < 2000):
                desc = 20
            elif (quant < 20000):
                desc = 25
            # Solicita o número de paginas novamente caso seja maior que 20000
            else:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                continue
        return quant, desc

def servico_extra():
    '''
    Imprime o menu de serviços extras, e depois retorna o valor adicional
    caso seja selecionado algum
    :return: Numero inteiro
    '''
    while True:
        print('\nDeseja adicionar algum serviço?')
        print('1 - Encadernação Simples   - R$ 15,00')
        print('2 - Encadernação Capa Dura - R$ 40,00')
        print('0 - Não desejo mais nada')
        op = str(input('>>>'))
        match op:
            case '1':
                return 15
            case '2':
                return 40
            case '0':
                return 0
            case _:
                print('Escolha uma opção válida.')
                continue

#Programa principal
print('Bem vindo a Copiadora do César Gehres')

# Menu solicitando o serviço a ser utilizado, retorna o valor
servico = escolha_servico()

# Solicita o número de páginas
# Páginas[0], porcentagem[1]
pags = num_pagina()
n_pags = pags[0]
porcentagem = pags[1]

# Solicita se quer algum serviço extra
extra = servico_extra()

# Calcula o valor a ser descontado.
desconto = (servico * porcentagem / 100)
# Calcula o valor final
total = ((servico - desconto) * n_pags) + extra

# Imprime o valor final no console
print(f'Total: R$ {total:.2f} (serviço: R$ {servico:.2f} * páginas: {n_pags} + extra: R$ {extra:.2f})')
