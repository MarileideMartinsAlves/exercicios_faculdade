# Atividade Prática Lógica de Programação e Algoritmos ** Exercício 3 **
print('Bem vindo(a) a Companhia de Logistica Marileide Martins Alves S.A.\n')  # identificador pessoal


# funcao para calcular volume do objeto
def dimensoesobjeto():
    while True:
        try:
            altura = int(input('Informe altura em cm: '))
            comprimento = int(input('Informe comprimento em cm: '))
            largura = int(input('Informe largura em cm: '))
            volume = altura * comprimento * largura
        except ValueError:
            print('Valor inválido, tente novamente')
        else:
            return volume


# funcao para calcular peso do objeto
def pesoobjeto():
    while True:
        try:
            peso = float(input('Informe peso em kg: '))
        except ValueError:
            print('Valor inválido, tente novamente')
        else:
            return peso


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
    print('Volume maior ou igual a 100.000, não é aceito')

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
    print('Peso maior ou igual a 30kg, não é aceito')

print('\nVolume de {}'.format(x))
print('R${}'.format(valor_volume))
print('\nPeso de {}kg'.format(y))
print('Multiplicador igual a {}'.format(multiplicador_peso))
