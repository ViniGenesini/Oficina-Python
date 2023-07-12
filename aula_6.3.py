''' 
EXERCÍCIO 3
Faça um programa que verifique o ano de nascimento de um
jovem, se ele é homem ou mulher e de acordo com sua idade o
programa informe se ele ainda vai se alistar ao serviço militar, se é
a hora de se alistar, ou se já passou do tempo de alistamento. Seu
programa também deverá mostrar o tempo que falta ou que passou
do prazo.

'''

sexo = input("Você é homem ou mulher? ")
if(sexo!="Homem"):
    print("Seu alistamento não é obrigatório!")
else:
    ano_nasc = int(input("Digite seu ano de nascimento: "))
    idade = 2023-ano_nasc
    if(idade<18):
        print("Você ainda irá se alistar ao serviço militar, falta(m) ",18-idade," ano(s)!")
    elif(idade==18):
        print("Está na hora de se alistar ao serviço militar!")
    else:
        print("O tempo de se alistar já passou!")
