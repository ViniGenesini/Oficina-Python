# EXERCÍCIO 1

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