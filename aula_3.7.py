''' 
EXERCÍCIO 7
Elabore um programa que solicite ao usuário a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$ 0.20 por
Km para viagens de até 100 km e R$ 0.15 para viagens mais longas.

'''

km = float(input('Digite a distância da viagem em km: '))
if(km<=100):
    print("Valor da passagem:",km*0.20)
else:
    print("Valor da passagem:",km*0.15)
