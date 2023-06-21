# EXERCÍCIO 9

try:
    print("*** NÚMEROS INTEIROS 2 ***\n")
    num = []
    resposta = 'S'
    while resposta=='S':
        x = int(input("Digite números inteiros: "))
        num.append(x)
        resposta = input("Deseja continuar, sim ou não? (S / N): ")
        if resposta=='N':
        print("\n*** RESULTADO ***\n")
        print("Média dos números:",sum(num)/len(num))
        num.sort()
        print("Maior número:",num[-1])
        print("Menor número:",num[0])
        elif resposta!='S':
        print("\n*** RESPOSTA INVÁLIDA! ***")
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS INTEIROS! ***")