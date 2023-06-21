# EXERCÍCIO 3

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