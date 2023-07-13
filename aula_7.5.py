''' 
EXERCÍCIO 5
Faça um Programa para um caixa eletrônico. O programa deverá
perguntar ao usuário a valor do saque e depois informar 
quantas notas de cada valor serão fornecidas. As notas 
disponíveis serão as de 1, 5, 10, 50 e 200 reais. O valor 
mínimo é de 20 reais e o máximo de 700 reais. O programa não 
deve se preocupar com a quantidade de notas existentes na
máquina. 

Exemplo 1: Para sacar a quantia de 256 reais, o programa 
fornece uma nota de 200, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar aquantia de 371 reais, o programa fornece
duas notas de 200, duas notas de 50, setenotas de 10 e uma de 1.

'''

print("*** CAIXA ELETRÔNICO ***\n\n")
try:
    saque = int(input("Digite o valor do saque (Mínimo: R$ 20.00 / Máximo: R$ 700.00): "))
    if(saque<20 or saque>700):
        print("\n*** VALOR INVÁLIDO: ACIMA DE R$ 700.00 OU ABAIXO DE R$ 20.00! ***")
    else:
        nota_200 = int(saque/200)
        nota_50 = int((saque-(nota_200*200))/50)
        nota_10 = int((saque-(nota_200*200)-(nota_50*50))/10)
        nota_5 = int((saque-(nota_200*200)-(nota_50*50)-(nota_10*10))/5)
        nota_1 = int(saque-(nota_200*200)-(nota_50*50)-(nota_10*10)-(nota_5*5))
        print("\n*** QUANTIDADE TOTAL DE NOTAS ***\n")
        print("NOTAS DE 200 REAIS:",nota_200,"nota(s).")
        print("NOTAS DE 50 REAIS:",nota_50,"nota(s).")
        print("NOTAS DE 10 REAIS:",nota_10,"nota(s).")
        print("NOTAS DE 5 REAIS:",nota_5,"nota(s).")
        print("NOTAS DE 1 REAL:",nota_1,"nota(s).")
except:
    print("\n*** VALOR INVÁLIDO: APENAS VALORES INTEIROS! ***")
