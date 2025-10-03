print(' LOJAS AMERICANAS ')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    calculo = preço - (preço * 10 / 100)
    print(f'O valor da sua compra é {preço:.2f}R$, com o desconto de 10% ficou {calculo}R$')
elif opção == 2:
    calculo = preço - (preço * 5 / 100)
    print(f'O valor da sua compra é {preço:.2f}R$, com o desconto de 5% ficou {calculo}R$')    
elif opção == 3:
    calculo = preço / 2
    print(f'O valor da sua compra é {preço:.2f}R$, parcelando em duas vezes, fica 2 parcelas de {calculo}R$')
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))    
    calculo = (preço + (preço * 20 / 100)) /  parcela
    Valor = preço + (preço * 20 / 100) 
    print(f'O valor da sua compra é {preço:.2f}R$,sua compra será parcelada em {parcela}x de {calculo:.2f} com juros. Sua compra de {preço:.2f}R$ vai custar {Valor:.2f}R$')
    