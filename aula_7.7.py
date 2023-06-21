# EXERCÍCIO 7

try:
    print("*** SEQUÊNCIA DE FIBONACCI ***\n")
    n = int(input("Digite a quantidade de termos desejados na Sequência de Fibonacci: "))
    fib = [0,1]
    i=2
    while(i<n):
        fib.append(fib[i-1]+fib[i-2])
        i+=1
    print("\n*** RESULTADO ***\n")
    print("Sequência de Fibonacci:",fib)
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS INTEIROS! ***")