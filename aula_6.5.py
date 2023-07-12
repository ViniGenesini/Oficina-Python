''' 
EXERCÍCIO 5
Tente criar uma calculadora com funções básicas de soma,
multiplicação, subtração e divisão. Nessa calculadora você
deverá utilizar try-except. Caso queira, poderá adicionar mais
funcionalidades, fique livre para pesquisar funções e adicioná-las
a sua calculadora.

'''

try:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
except:
    print("Valor(es) inválido(s)!")
print("Soma:",x+y)
print("Subtração:",x-y)
print("Multiplicação:",x*y)
if(y!=0):
    print("Divisão:",x/y)
else:
    print("Divisão: Impossível dividir por zero!")
