''' 
EXERCÍCIO 1
Elabore um programa que leia um número inteiro qualquer e
mostre na tela a sua tabuada.

'''

x = int(input("Digite um número: "))
print("TABUADA DO",x)
for i in range(11):
    print(x," x ",i," = ",x*i)
    i+=1
