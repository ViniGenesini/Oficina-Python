''' 
EXERCÍCIO 4
Um clube de natação estrangeiro irá visitar o brasil para avaliar os
novos atletas e precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima: MASTER

Faça o programa de acordo com as diretrizes acima.

'''

ano = int(input("Digite seu ano de nascimento: "))
idade = 2023-ano
if idade<=9:
    print("MIRIM")
elif(idade>9 and idade<=14):
    print("INFANTIL")
elif(idade>14 and idade<=19):
    print("JUNIOR")
elif(idade>19 and idade<=25):
    print("SÊNIOR")
else:
    print("MASTER")
