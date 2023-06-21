# EXERCÍCIO 5

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