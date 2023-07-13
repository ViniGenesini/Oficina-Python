''' 
EXERCÍCIO 3
Desenvolva um programa que leia peso e a altura de uma
pessoa, calcule seu IMCe mostre seu status, de acordo 
com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
(Obs: Utilize try except)

'''

try:
    print("*** CALCULADORA DE IMC *** \n")
    altura = float(input("Digite sua altura (em m): "))
    peso = float(input("Digite seu peso: "))
    IMC = peso/(altura*altura)
    if(IMC<18.5):
        print("\n*** RESULTADO *** \n\nIMC =","%.2f"%IMC,"\nStatus: Abaixo do Peso")
    elif(IMC>=18.5 and IMC<=25):
        print("\n*** RESULTADO *** \n\nIMC =","%.2f"%IMC,"\nStatus: Peso Ideal")
    elif(IMC>25 and IMC<=30):
        print("\n*** RESULTADO *** \n\nIMC =","%.2f"%IMC,"\nStatus: Sobrepeso")
    elif(IMC>30 and IMC<=40):
        print("\n*** RESULTADO *** \n\nIMC =","%.2f"%IMC,"\nStatus: Obesidade")
    else:
        print("\n*** RESULTADO *** \n\nIMC =","%.2f"%IMC,"\nStatus: Obesidade Mórbida")
except:
    print("*** VALOR(ES) INVÁLIDO(S)! ***")
