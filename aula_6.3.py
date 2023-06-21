# EXERCÍCIO 3

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