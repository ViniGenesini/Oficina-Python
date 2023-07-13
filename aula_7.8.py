''' 
EXERCÍCIO 8
Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a somaentre eles.

'''

try:
    print("*** NÚMEROS INTEIROS ***\n")
    num = [0]
    x = 0
    num[0] = int(input("Digite números inteiros, para finalizar o programa digite 999: "))
    while(x!=999):
        x = int(input(""))
        num.append(x)
    print("\n*** RESULTADO ***\n")
    print("Quantidade de números:",len(num)-1)
    print("Soma dos números:",sum(num)-num[-1])
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS INTEIROS! ***")
