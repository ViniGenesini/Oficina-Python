# EXERCÍCIO 2

km = int(input("Digite a velocidade do carro em km/h: "))
x = float(100+10*(km-70))
if(km>70):
    print("Você foi multado! O valor a pagar é de R$","%.2f"%x)
else:
    print("Parabéns, você não foi multado!")