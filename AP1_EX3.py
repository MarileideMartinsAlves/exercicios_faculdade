# Atividade Prática Lógica de Programação e Algoritmos ** Exercício 3 **
print('Bem vindo(a) a Companhia de Logistica Marileide Martins Alves S.A.')  # identificador pessoal


# funcao para calcular volume do objeto
def dimensoesobjeto():
    while True:
        try:
            comprimento = float(input('Digite o comprimento do objeto em cm: '))
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor entre com as dimensões desejadas novamente')
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
                    volume = altura * largura * comprimento
                    return volume


# funcao para calcular peso do objeto
def pesoobjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto em kg: '))
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico')
            print('Por favor entre com o peso desejado novamente')
        else:
            return peso


# funcao para calcular rota do objeto
def rotaobjeto():
    print('Selecione a rota:')
    print('|              ROTA               | SIGLA |')
    print('| De Rio de Janeiro até São Paulo |   RS  |')
    print('| De São Paulo até Rio de Janeiro |   SR  |')
    print('| De Curitiba até Santa Catarina  |   CS  |')
    print('| De Santa Catarina até Curitiba  |   SC  |')
    r = 0
    while r == 0:
        rota = input('Informe a sigla da rota (UTILIZE LETRA MAIÚSCULA): ')
        if rota == 'RS' or rota == 'SR' or rota == 'CS' or rota == 'SC':
            return rota
        else:
            print('Você digitou uma rota que não existe')
            print('Por favor entre com a rota desejada novamente:')


x = dimensoesobjeto()
if x < 1000:
    valor_volume = 10
elif 1000 <= x < 10000:
    valor_volume = 20
elif 10000 <= x < 30000:
    valor_volume = 30
elif 30000 <= x < 100000:
    valor_volume = 50
else:
    valor_volume = 0
    print('O volume do objeto é em cm³: {}'.format(x))
    print('Não aceitamos objetos com dimensões tão grandes')
    print('Entre com as dimensões desejadas novamente: ')
    x = dimensoesobjeto()
print('O volume do objeto {} em cm³'.format(x))

y = pesoobjeto()
if y < 0.1:
    multiplicador_peso = 1
elif 0.1 <= y < 1:
    multiplicador_peso = 1.5
elif 1 <= y < 10:
    multiplicador_peso = 2
elif 10 <= y < 30:
    multiplicador_peso = 3
else:
    multiplicador_peso = 0
    print('Não aceitamos objetos tão pesados')
    print('Entre com o peso desejado novamente')
    y = pesoobjeto()

z = rotaobjeto()
if z == 'RS':
    multiplicador_rota = 1
elif z == 'SR':
    multiplicador_rota = 1.5
elif z == 'CS':
    multiplicador_rota = 2
else:
    multiplicador_rota = 2.5

valor = valor_volume * multiplicador_peso * multiplicador_rota

print('Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota {})'.format(valor, valor_volume, multiplicador_peso, multiplicador_rota))
