''' 
EXERCÍCIO 2
Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 70 km/h, mostre uma mensagem dizendo que ele foi
multado e o valor que deverá pagar, caso ele esteja dentro do limite
permitido, mostre uma mensagem o parabenizando. A multa vai
custar R$ 10,00 por cada km acima dos 70.

'''

km = int(input("Digite a velocidade do carro em km/h: "))
x = float(100+10*(km-70))
if(km>70):
    print("Você foi multado! O valor a pagar é de R$","%.2f"%x)
else:
    print("Parabéns, você não foi multado!")
