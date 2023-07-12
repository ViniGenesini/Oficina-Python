''' 
EXERCÍCIO 5
Faça um programa que receba um número em horas e converta em
minutos, informando ao usuário o horário digitado e os minutos ao qual
foi convertido.

ATUALIZADO EM: 12/07/2023

'''

horas = float(input("Insira horas: "))
horas_inteiras = int(horas)
minutos = (horas_inteiras-horas)*-60
print(f"Horário: {horas_inteiras}:{int(minutos)}")
print(f"Minutos: {horas*60}")
