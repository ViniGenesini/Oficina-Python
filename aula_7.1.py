# EXERCÍCIO 1

total = 0
print("*** CALCULADORA DE NÚMEROS PARES ***\n")
for i in range(6):
    num = float(input("Digite o {}º número: ".format(i+1)))
    if(num%2==0):
        total = total + num
print("\n*** RESULTADO ***\n\n{}".format(total))