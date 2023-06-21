# EXERCÍCIO 8

try:
    print("*** NÚMEROS INTEIROS ***\n")
    num = [0]
    x = 0
    num[0] = int(input("Digite números inteiros, para finalizar o programa digite 999: "))
    while(x!=999):
        x = int(input(""))
        num.append(x)
    print("\n*** RESULTADO ***\n")
    print("Quantidade de números:",len(num)-1)
    print("Soma dos números:",sum(num)-num[-1])
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS INTEIROS! ***")