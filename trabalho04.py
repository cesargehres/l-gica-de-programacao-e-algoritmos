def cadastrar_livro(id):
    '''
    Pergunta nome, autor e editora de um livro, depois forma as informações
    em um dicionario junto com o 'id'
    :param id: id do livro
    :return: Adiciona um dicionario a lista "lista_livro"
    '''
    # Menu
    print(52 * '-')
    print(f'{15 * "-"} MENU CADASTRAR LIVRO {15 * "-"}')

    # Recebe os valores do livro
    print('Escolha a opção desejada:')
    nome = str(input('Nome: ')).title()
    autor = str(input('Autor: ')).title()
    editora = str(input('Editora: ')).title()

    # Junta os valores em um dicionário e adiciona a "lista_lisvro"
    livro = {'id': str(id), 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

def consultar_livro():
    '''
    Imprime o Menu de Consulta e solicita um tipo de consulta
    :return: Imprime os livros consultados no console
    '''
    while True:
        # Imprime as alternativas e recebe a opção desejada
        print(52 * '-')
        print(f'{15 * "-"} MENU CONSULTAR LIVRO {15 * "-"}')
        print('1. Consultar Todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        op = str(input('>>>'))

        #Imprime as informações dos livros conforme a escolha desejada
        match op:
            # Consultar todos os livros
            case '1':
                print(30 * '-')
                for livro in lista_livro:
                    for chave, valor in livro.items():
                        print(f'{chave}: {valor}')
                    print()
                continue

            # Consulta pelo ID
            case '2':
                id_procurado = str(input('Digite o ID do livro: '))
                id_existe = False
                print(30 * '-')
                # Se o livro tiver o id solicitado ira imprimir o livro
                for livro in lista_livro:
                    if (livro['id'] == id_procurado):
                        id_existe = True # Se existir o ID
                        for chave, valor in livro.items():
                            print(f'{chave}: {valor}')
                        print()
                # Se ID não existe
                if not id_existe:
                    print('ID não encontrado')
                continue

            # Consulta por Autor
            case '3':
                autor_procurado = str(input('Digite o autor do(s) livro(s): ')).title()
                autor_existe = False
                print(30 * '-')
                # Se o livro for do autor consultado ira imprimir o livro
                for livro in lista_livro:
                    if (livro['autor'] == autor_procurado):
                        autor_existe = True # Se o Autor existir
                        for chave, valor in livro.items():
                            print(f'{chave}: {valor}')
                        print()
                    # Se não tiver nenhum livro com o autor
                if not autor_existe:
                    print('Autor não encontrado.')
                continue

            # Retorna ao Menu Principal
            case '4':
                break

            # Se não escolher uma opção válida
            case _:
                print('Escolha inválida.')
                continue

def remover_livro():
    '''
    Remove um livro de "lista_livro" com base no ID
    :return: lista_livro com um item removido
    '''
    print(52 * '-')
    print(f'{13 * "-"} MENU REMOVER LIVRO {19 * "-"}')
    id = str(input('ID do livro a ser removido: '))
    id_existe = False

    for livro in lista_livro:
        # Se o ID existir remove o dicionario da lista
        if (livro['id'] == id):
            livro_a = livro
            id_existe = True
            lista_livro.remove(livro_a)
            print('Livro removido com sucesso.')
    # Caso o ID não exista
    if not id_existe:
        print('Livro inexistente.')


# Programa principal
print('Bem vindo a Livraria do César Gehres')

# Lista dos livros e variavel de id que aumenta a cada livro novo registrado
lista_livro = []
id_global = 0

while True:
    # Menu Principal
    print(52 * '-')
    print(f'{17 * "-"} MENU PRINCIPAL {19 * "-"}')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    op = str(input('>>>'))

    match op:
        # Cadastrar um novo livro
        case '1':
            cadastrar_livro(id_global)
            id_global += 1

        # Abre o menu de consultas
        case '2':
            consultar_livro()

        case '3':
            remover_livro()

        # Fecha o Programa
        case '4':
            break

        # Se a escolha for inválida
        case _:
            print('Escolha inválida.')
