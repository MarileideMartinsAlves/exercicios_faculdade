# Atividade Prática Lógica de Programação e Algoritmos ** Exercício 3 **

print('Bem vindo(a) a Companhia de Logistica Marileide Martins Alves S.A.')  # identificador pessoal


def dimensoesobjeto():  # funcao para calcular volume do objeto
    while True:  # laço de repetição para validações das dimensões
        try:  # validação das dimensões
            comprimento = float(input('Digite o comprimento do objeto em cm: '))
        except ValueError:  # tratativa dimensão não numérica
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor entre com as dimensões desejadas novamente')  # dimensão inválida, reinicia input dimensão
        else:
            try:
                largura = float(input('Digite a largura do objeto em cm: '))
            except ValueError:
                print('Você digitou alguma dimensão do objeto com valor não numérico')
                print('Por favor entre com as dimensões desejadas novamente')
            else:
                try:
                    altura = float(input('Digite a altura do objeto em cm: '))
                except ValueError:
                    print('Você digitou alguma dimensão do objeto com valor não numérico')
                    print('Por favor entre com as dimensões desejadas novamente')
                else:
                    return altura * largura * comprimento  # após todas dimensões com valores válidos retorna volume


def pesoobjeto():  # funcao para calcular peso do objeto
    while True:  # laço de repetição para validações dos pesos
        try:  # validação dos pesos
            peso = float(input('Digite o peso do objeto em kg: '))
        except ValueError:  # tratativa peso não numérico
            print('Você digitou peso do objeto com valor não numérico')
            print('Por favor entre com o peso desejado novamente')
        else:
            return peso  # após peso validado como numérico retorna peso


def rotaobjeto():  # funcao para mostrar rota do objeto
    print('Selecione a rota:')  # tabela para referencia das siglas por rotas
    print('|              ROTA               | SIGLA |')
    print('| De Rio de Janeiro até São Paulo |   RS  |')
    print('| De São Paulo até Rio de Janeiro |   SR  |')
    print('| De Curitiba até Santa Catarina  |   CS  |')
    print('| De Santa Catarina até Curitiba  |   SC  |')
    r = 0  # parâmetro para iniciar e terminar laço while
    while r == 0:  # laço de repetição para validar rotas
        rota = input('Informe a sigla da rota (UTILIZE LETRA MAIÚSCULA): ')
        if rota == 'RS' or rota == 'SR' or rota == 'CS' or rota == 'SC':  # tratativa para valores válidos ou inválidos
            return rota  # rota válida, retorna rota
        else:  # rota inválida, reinicia input sigla da rota
            print('Você digitou uma rota que não existe')
            print('Por favor entre com a rota desejada novamente:')


# Programa principal
valor_volume = 0  # parâmetro para iniciar e terminar laço while
x = dimensoesobjeto()  # chama função das dimensões do objeto
while valor_volume == 0:  # laço de repetição para identificar valor R$ por volume
    if x < 1000:  # critérios de definição de valor R$ por volume
        valor_volume = 10  # valor R$ atribuído conforme volume
        print('O volume do objeto {} em cm³'.format(x))  # mostra na tela volume do objeto
    elif 1000 <= x < 10000:  # elif demais critérios
        valor_volume = 20
        print('O volume do objeto {} em cm³'.format(x))
    elif 10000 <= x < 30000:
        valor_volume = 30
        print('O volume do objeto {} em cm³'.format(x))
    elif 30000 <= x < 100000:
        valor_volume = 50
        print('O volume do objeto {} em cm³'.format(x))
    else:
        valor_volume = 0
        print('O volume do objeto {} em cm³'.format(x))
        print('Não aceitamos objetos com dimensões tão grandes')
        print('Entre com as dimensões desejadas novamente: ')
        x = dimensoesobjeto()  # chama função novamente caso volume inválido

multiplicador_peso = 0  # parâmetro para iniciar e terminar laço while
y = pesoobjeto()  # chama função das dimensões do objeto
while multiplicador_peso == 0:  # laço de repetição para identificar fator multiplicador por peso
    if y < 0.1:  # critérios de definição do multiplicador por peso
        multiplicador_peso = 1  # multiplicador atribuído conforme peso
    elif 0.1 <= y < 1:  # elif demais critérios
        multiplicador_peso = 1.5
    elif 1 <= y < 10:
        multiplicador_peso = 2
    elif 10 <= y < 30:
        multiplicador_peso = 3
    else:
        multiplicador_peso = 0
        print('Não aceitamos objetos tão pesados')
        print('Entre com o peso desejado novamente')
        y = pesoobjeto()  # chama função novamente caso volume inválido

z = rotaobjeto()  # chama função das dimensões do objeto
if z == 'RS':  # critérios de definição do multiplicador por rota
    multiplicador_rota = 1  # multiplicador atribuído conforme rota
elif z == 'SR':  # elif demais critérios
    multiplicador_rota = 1.5
elif z == 'CS':
    multiplicador_rota = 2
else:
    multiplicador_rota = 2.5

valor = valor_volume * multiplicador_peso * multiplicador_rota  # total a ser pago  # RU identificador do aluno

print('Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota {})'.format(valor, valor_volume, multiplicador_peso, multiplicador_rota))
# mostra na tela total a pagar
