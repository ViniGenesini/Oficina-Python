''' 
EXERCÍCIO 1
Faça um programa que receba a data de aniversário do usuário
e mostre na tela como mensagem, sendo o dia/mês e ano. faça
um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:

• “Telefonou para a vítima?”
• “Esteve no local do crime?”
• “Mora perto da vítima?”
• “Devia para a vítima?”
• “Já trabalhou com a vítima?”

Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5
como “Assassino”. Caso contrário, ele será classificado como
“Inocente”

'''

print("Responda essas 5 perguntas sobre o crime!")
i=0
resposta = input("Telefonou para a vítima? \n")
if(resposta=="Sim"):
    i+=1
resposta = input("Esteve no local do crime? \n")
if(resposta=="Sim"):
    i+=1
resposta = input("Mora perto da vítima? \n")
if(resposta=="Sim"):
    i+=1
resposta = input("Devia para a vítima? \n")
if(resposta=="Sim"):
    i+=1
resposta = input("Já trabalhou com a vítima? \n")
if(resposta=="Sim"):
    i+=1
if(i<=1):
    print("Inocente")
elif(i==2):
    print("Suspeita")
elif(i<=4):
    print("Cúmplice")
elif(i==5):
    print("Assassino")
elif(i==5):
    print("Assassino")
