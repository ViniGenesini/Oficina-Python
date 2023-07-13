''' 
EXERCÍCIO 7
Escreva um programa que leia um número n inteiro
qualquer e mostrena tela os n primeiros elementos
de uma Sequência de Fibonacci. (“Fibonacci é uma 
sequência de números, que aparece em certos mistérios
da natureza e da vida, onde a sequência inicia com 0
e 1, e os números seguintes serão a soma dos dois
números anterior”.)

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

'''

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
