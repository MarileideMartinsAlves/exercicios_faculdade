#  Atividade Prática Lógica de Programação e Algoritmos ** Exercício 1 **

print('Bem Vindo(a) à Loja da Marileide Martins Alves') # identificador pessoal
valorproduto3049987 = float(input('Digite o valor do produto: '))  # valor unitário do produto do tipo flutuante
# RU na variável
quantidadeproduto = int(input('Digite a quantidade do produto: '))  # quantidade de produto do tipo inteiro
comprasemdesconto = float(valorproduto3049987*quantidadeproduto)  # cálculo da compra sem desconto

if 10 <= quantidadeproduto <= 99:  # if contemplando a primeira condição para receber desconto
    desconto = float(0.05)  # desconto que precisa ser aplicado ao atender a condição acima
elif 100 <= quantidadeproduto <= 999:  # elif contemplando a segunda condição para receber desconto
    desconto = float(0.10)  # desconto que precisa ser aplicado ao atender a condição acima
elif quantidadeproduto >= 1000:  # elif contemplando a terceira condição para receber desconto
    desconto = float(0.15)  # desconto que precisa ser aplicado ao atender essa condição
else:  # quando nenhuma das condições foi atendida
    desconto = 0  # desconto que precisa ser aplicado se nenhuma das condições for atendida

print('Desconto de ', desconto * 100, '% no valor final da compra.')  # impressão na tela do % de desconto conquistado
compracomdesconto = float(comprasemdesconto-(comprasemdesconto*desconto))  # cálculo da compra com o desconto
print('Valor da compra sem desconto é R${:.2f}.'.format(comprasemdesconto))  # impressão na tela do valor da compra sem desconto
print('Valor da compra com desconto é R${:.2f}.'.format(compracomdesconto))  # impressão na tela do valor da compra com desconto
