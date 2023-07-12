''' 
EXERCÍCIO 1
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenasdaqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o. (Obs: Utilize try except)

'''
try:
    total = 0
    print("*** CALCULADORA DE NÚMEROS PARES ***\n")
    for i in range(6):
        num = float(input("Digite o {}º número: ".format(i+1)))
        if(num%2==0):
            total = total + num
    print("\n*** RESULTADO ***\n\n{}".format(total))
except:
    print("*** VALOR INVÁLIDO! ***")
