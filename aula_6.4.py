''' 
EXERCÍCIO 4
Uma fruteira está vendendo frutas com a seguinte tabela de
preços:

Fruta       Até 3 Kg            Acima de 6 Kg
Morango     R$ 3,50 por Kg      R$ 4,20 por Kg
Maçã        R$ 2,80 por Kg      R$ 2,50 por Kg

Se o cliente comprar mais de 12 Kg em frutas ou o valor total da
compra ultrapassar R$ 35,00, receberá ainda um desconto de
15% sobre este total. Escreva um algoritmo para ler a
quantidade (em Kg) de morangos e a quantidade (em Kg) de
maças adquiridas e escreva o valor a ser pago pelo cliente.

'''

kg_mor = float(input("Digite a quantidade de morangos adquiridos em kg: "))
kg_mac = float(input("Digite a quantidade de maçãs adquiridas em kg: "))
if(kg_mor<=3):
    valor_mor = 3.5*kg_mor
else:
    valor_mor = 4.2*kg_mor
if(kg_mac>6):
    valor_mac = 2.5*kg_mac
else:
    valor_mac = 2.8*kg_mac
valor_total = valor_mor+valor_mac
kg_total = kg_mor+kg_mac
if(kg_total>12 or valor_total>35):
    valor_total = valor_total-(valor_total*(0,15))
print("Valor total á ser pago: R$ ","%.2f"%valor_total)
