''' 
EXERCÍCIO 6
Crie um programa que receba 4 notas, mostre ao usuário a sua
média aritmética e de acordo com sua média, se ele foi aprovado ou
reprovado.

'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1+nota2+nota3+nota4)/4
print("Média geral:",media)
if media<5:
    print("Você foi reprovado!")
else:
    print("Você foi aprovado!")
