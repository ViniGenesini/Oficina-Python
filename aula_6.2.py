''' 
EXERCÍCIO 2
Crie um programa que receba 1 número e mostre ao usuário qual
seu dobro, triplo e raiz quadrada. Faça um programa que calcule as
raízes de uma equação do segundo grau, na forma ax2 + bx + c. O
programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações: Se o
usuário informar o valor de A igual a zero, equação não é do
segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado; Se o delta calculado for negativo, a equação não
possui raízes reais. Informe ao usuário e encerre o programa; se o
delta calculado for igual a zero a equação possui apenas uma raiz
real; informe-a ao usuário; se o delta for positivo, a equação possui
duas raízes reais; informe-as ao usuário;

'''

a = float(input("Digite o valor de A: "))
if(a==0):
    print("Valor inválido! A equação não será de 2º grau, então não pode ser realizada!")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = b**2-4*a*c
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
    if delta<0:
        print("A equação não possui raízes reais, então não pode ser realizada!")
    elif delta==0:
        print("A equação possui apenas uma raiz real!")
        print("x1 = ",x1)
    else:
        print("A equação possui duas raízes reais!")
        print("x1 = ",x1)
        print("x2 = ",x2)
