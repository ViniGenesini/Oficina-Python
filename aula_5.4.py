# EXERCÍCIO 4

ano = int(input("Digite seu ano de nascimento: "))
idade = 2023-ano
if idade<=9:
    print("MIRIM")
elif(idade>9 and idade<=14):
    print("INFANTIL")
elif(idade>14 and idade<=19):
    print("JUNIOR")
elif(idade>19 and idade<=25):
    print("SÊNIOR")
else:
    print("MASTER")