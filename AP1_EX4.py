# Atividade Prática Lógica de Programação e Algoritmos ** Exercício 4 **

print('Bem vindo(a) ao Controle de estoque da Bicicletaria da Marileide Martins Alves\n')  # identificador pessoal

listapecas = []  # lista vazia para receber os cadastros


def cadastrarpecas(codpeca):  # função para cadastrar peças
    print('Você selecionou a opção de Cadastrar Peças')
    print('Codigo da peça {}'.format(codpeca))
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor entre com  o VALOR(R$) da peça: '))
    dicionariocadastro = {'codpeca': codpeca,
                          'nome': nome,
                          'fabricante': fabricante,
                          'valor': valor}
    listapecas.append(dicionariocadastro.copy())  # entrada de dados do dicionário na lista


def consultarpecas():  # função para consultar peças
    while True:  # laço de repetição para escolha do tipo de consulta
        try:  # validação dos opções escolhidas
            print('Escolha a opção desejada:')
            opcao_consultar = int(input('1 - Consultar todas as Peças\n2 - Consultar peças por Código\n3 - Consultar peças por Fabricante\n4 - Retornar\nOpção desejada: '))
            if opcao_consultar == 1:  # critérios conforme a opção escolhida
                for pecas in listapecas:  # laço de repetição para mostrar dados da lista de cadastro
                    print('-' * 20)
                    for key, value in pecas.items():
                        print('{} : {}'.format(key, value))
                print('-' * 20)
            elif opcao_consultar == 2:
                entrada_cod = int(input('Digite o CODIGO da peça: '))
                for pecas in listapecas:
                    if pecas['codpeca'] == entrada_cod:
                        print('-' * 20)
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
                print('-' * 20)
            elif opcao_consultar == 3:
                entrada_fab = input('Digite o FABRICANTE da peça: ')
                for pecas in listapecas:
                    if pecas['fabricante'] == entrada_fab:  # critério para identificar item a ser apresentado
                        print('-' * 20)
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
                print('-' * 20)
            elif opcao_consultar == 4:
                print('Retornar ao menu principal')
                return
            else:
                print('Opção inválida')
                continue
        except ValueError:  # tratativa opção não numérica
            print('Você digitou um valor não numérico')
            print('Por favor escolha a opção desejada novamente')  # reinicia loop


def removerpecas():  # função para remover peças
    print('Você escolheu a opção de Remover Peça')
    entrada_rem = int(input('Digite o CODIGO da peça: '))
    for pecas in listapecas:
        if pecas['codpeca'] == entrada_rem:  # critério para identificar item que vai ser removido
            listapecas.remove(pecas)  # remover peças


# Início

codigopeca3049987 = 0  # contador para gerar códigos únicos e identificar RU compondo o nome da variável

while True:  # laço de repetição para iniciar programa
    try:  # validação dos valores de escolha
        print('Escolha a opção desejada:')
        opcao = int(input('1 - Cadastrar peças\n2 - Consultar peças\n3 - Remover peças\n4 - Sair\nOpção desejada: '))
        if opcao == 1:  # critérios conforme a opção escolhida
            codigopeca3049987 = codigopeca3049987 + 1
            cadastrarpecas(codigopeca3049987)
        elif opcao == 2:
            print('Você selecionou a opção de Consultar peças')
            consultarpecas()
        elif opcao == 3:
            removerpecas()
        elif opcao == 4:
            print('Saindo do controle de estoque')
            break
        else:
            print('Opção inválida')
            continue
    except ValueError:  # tratativa escolha não numérica
        print('Você digitou um valor não numérico')
        print('Por favor escolha a opção desejada novamente')  # opção inválida, reinicia loop
