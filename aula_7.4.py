''' 
EXERCÍCIO 4
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades dele.
Observando os termos no plural a colocação do "e", da vírgula
entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 
25, 20, 10, 21, 11, 1, 7 e 16.

'''

print("*** CALCULADORA DE CASAS DECIMAIS ***\n")
try:
    num = int(input("Digite um número inteiro menor que 1000: "))
    if(num>1000 or num<-1000):
        print("\n*** VALOR INVÁLIDO: ACIMA DE 1000 OU ABAIXO DE -1000! ***")
    else:
        C = int(num/100)
        D = int((num-(C*100))/10)
        U = int(num-(C*100)-(D*10))
        print("\n*** RESULTADO ***\n")
        if(C==1 and D==1 and U==1):
            print(num,"=",C,"centena,",D,"dezena e",U,"unidade.")
        elif(C!=1 and D!=1 and U!=1):
            print(num,"=",C,"centenas,",D,"dezenas e",U,"unidades.")
        elif(C==1 and D==1 and U!=1):
            print(num,"=",C,"centena,",D,"dezena e",U,"unidades.")
        elif(C==1 and D!=1 and U==1):
            print(num,"=",C,"centena,",D,"dezenas e",U,"unidade.")
        elif(C!=1 and D==1 and U==1):
            print(num,"=",C,"centenas,",D,"dezena e",U,"unidade.")
        elif(C==1 and D!=1 and U!=1):
            print(num,"=",C,"centena,",D,"dezenas e",U,"unidades.")
        elif(C!=1 and D!=1 and U==1):
            print(num,"=",C,"centenas,",D,"dezenas e",U,"unidade.")
        elif(C!=1 and D==1 and U!=1):
            print(num,"=",C,"centenas,",D,"dezena e",U,"unidades.")
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS INTEIROS! ***")
