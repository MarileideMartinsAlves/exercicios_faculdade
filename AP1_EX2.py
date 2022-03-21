# Atividade Prática Lógica de Programação e Algoritmos ** Exercício 1 **
print('Bem vindo(a) a Lanchonete da Marileide Martins Alves\n')  # identificador pessoal

s1 = "Cachorro-Quente"  # s1 ao s8 são produtos do cardapio
s2 = "Cachorro-Quente Duplo"
s3 = "x-Egg"
s4 = "X-Salada"
s5 = "X-Bacon"
s6 = "X-Tudo"
s7 = "Refrigerante Lata"
s8 = "Chá Gelado"

preco_s1: float = float(9)  # valor de todos os produtos
preco_s2 = float(11)
preco_s3 = float(12)
preco_s4 = float(12)
preco_s5 = float(14)
preco_s6 = float(17)
preco_s7 = float(5)
preco_s8 = float(4)

print(' *************** CARDAPIO *****************')  # composicao do cardapio com códigos, produtos e valores
print('| Código |        Descrição        | Valor |')
print('|  100   |    ', s1, '    | ', preco_s1, ' |')
print('|  101   | ', s2, ' | ', preco_s2, '|')
print('|  102   |         ', s3, '         | ', preco_s3, '|')
print('|  103   |       ', s4, '        | ', preco_s4, '|')
print('|  104   |        ', s5, '        | ', preco_s5, '|')
print('|  105   |         ', s6, '        | ', preco_s6, '|')
print('|  200   |   ', s7, '   | ', preco_s7, ' |')
print('|  201   |       ', s8, '      | ', preco_s8, ' |')

total = 0  # valor do pedido iniciando em R$0,00

while True:  # laço de repetição para receber os pedidos
    pedido = 1  # pedido igual a 1 permanece dentro do laço de repetição
    cod_prod = int(input('\nEntre com o codigo do produto desejado:'))  # recebe código do produto e inicia if's
    if cod_prod == 100:  # busca produto e preço correspondente ao codigo digitado
        valor = preco_s1  # variável valor recebe valor do produto indicado
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s1, preco_s1))  # mostra na tela produto e valor
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))  # confirmação para continuar pedido
        if pedido == 0:  # verifica se permanece ou encerra o laço
            total = total + valor  # soma ao total o valor do pedido
            break  # encerra laço se if verdadeiro
    elif cod_prod == 101:  # repete rotina if conforme o código
        valor = preco_s2
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s2, preco_s2))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 102:
        valor = preco_s3
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s3, preco_s3))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 103:
        valor = preco_s4
        print('\nVocê pediu um {} no valor de R${:.2f}.'.format(s4, preco_s4))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 104:
        valor = preco_s5
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s5, preco_s5))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 105:
        valor = preco_s6
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s6, preco_s6))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 200:
        valor = preco_s7
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s7, preco_s7))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    elif cod_prod == 201:
        valor = preco_s8
        print('\nVocê pediu um {} no valor de R$ {:.2f}.'.format(s8, preco_s8))
        pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))
        if pedido == 0:
            total = total + valor
            break
    else:  # código digitado não está no cardápio
        valor = 0  # não adiciona nenhum valor ao total
        print('\nCódigo inválido')  # mensagem na tela
        continue  # segue laço de repetição
    total = total + valor  # somatorio de todos os pedidos

total3049987 = total  # RU na variável
print('\nO total a ser pago é: R${:.2f}.'.format(total3049987))  # mostra na tela valor final do pedido
