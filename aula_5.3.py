# EXERCÍCIO 3

a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um número inteiro: "))
if(a==b==c):
    print("Números iguais!")
else:
    if(a>=b and a>=c):
        print("Número maior: ",a)
    elif(b>=a and b>=c):
        print("Número maior: ",b)
    elif(c>=a and c>=b):
        print("Número maior: ",c)
    if(a<=b and a<=c):
        print("Número menor: ",a)
    elif(b<=a and b<=c):
        print("Número menor: ",b)
    elif(c<=a and c<=b):
        print("Número menor: ",c)