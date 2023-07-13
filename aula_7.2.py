''' 
EXERCÍCIO 2
Oferta de carnes em um açougue:

Carne           Até 6Kg             Acima de 6Kg
File Duplo      R$ 3,90 por Kg      R$ 6,80 por Kg
Alcatra         R$ 4,90 por Kg      R$ 7,80 por Kg
Picanha         R$ 5,90 por Kg      R$ 8,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas
um dos tipos de carne da promoção, porém não há limites para a 
quantidade  de  carne  por  cliente.  Se  compra  for  feita  no  
cartão Tabajara o cliente receberá ainda um desconto de 6% sobre o 
total da compra. Escreva um programa que peça o tipo e a quantidade 
de carne comprada pelo usuário e gere um cupom fiscal, contendo as 
informações da compra: tipo e quantidade de carne, preço total, tipo 
de pagamento, valor do desconto e valor a pagar.

'''

try:
    print("*** CARNES *** \n\n 1- Filé Duplo \n 2- Alcatra \n 3- Picanha \n")
    tipo = int(input("Digite o número correspondente ao tipo de carne desejada: "))
    kg = float(input("Digite a quantidade desejada (kg): "))
    print("\n *** FORMA DE PAGAMENTO *** \n\n 1- Cartão Tabajara \n 2- Outro \n")
    pag = int(input("Digite a forma de pagamento: "))
    def cupom_fiscal():
        print("\n *** CUPOM FISCAL ***")
        if(tipo==1):
            print("\nTipo de Carne: Filé Duplo")
        elif(tipo==2):
            print("\n Tipo de Carne: Alcatra")
        elif(tipo==3):
            print("\n Tipo de Carne: Picanha")
            print("Quantidade:",kg,"kg")
            print("Valor Total: R$","%.2f"%valor_total)
        if(pag==1):
            print("Forma de Pagamento: Cartão Tabajara")
        elif(tipo==2):
            print("Forma de Pagamento: Outro")
            print("Valor do Desconto: R$","%.2f"%valor_desconto)
            print("Valor á Pagar: R$","%.2f"%valor_pagar)
    if(tipo==1):
        if(kg<=6):
            if(pag==1):
                valor_total = kg*3.9
                valor_desconto = (kg*3.9)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*3.9
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
        elif(kg>6):
            if(pag==1):
                valor_total = kg*6.8
                valor_desconto = (kg*6.8)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*6.8
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
    elif(tipo==2):
        if(kg<=6):
            if(pag==1):
                valor_total = kg*4.9
                valor_desconto = (kg*4.9)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*4.9
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
        elif(kg>6):
            if(pag==1):
                valor_total = kg*7.8
                valor_desconto = (kg*7.8)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*7.8
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
    elif(tipo==3):
        if(kg<=6):
            if(pag==1):
                valor_total = kg*5.9
                valor_desconto = (kg*5.9)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*5.9
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
        elif(kg>6):
            if(pag==1):
                valor_total = kg*8.8
                valor_desconto = (kg*8.8)*0.06
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            elif(pag==2):
                valor_total = kg*8.8
                valor_desconto = 0
                valor_pagar = valor_total-valor_desconto
                cupom_fiscal()
            else:
                print("*** VALOR(ES) INVÁLIDO(S)! ***")
    else:
        print("*** VALOR(ES) INVÁLIDO(S)! ***")
except:
    print("*** VALOR(ES) INVÁLIDO(S)! ***")
