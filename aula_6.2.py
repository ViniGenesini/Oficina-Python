# EXERCÍCIO 2

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