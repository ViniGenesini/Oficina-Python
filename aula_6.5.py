# EXERCÍCIO 5

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