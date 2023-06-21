# EXERCÍCIO 4

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