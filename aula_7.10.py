# EXERCÍCIO 10

print("*** DADOS PESSOAIS ***\n")
maioridade = []
homens = []
mulheres_menor20 = []
resposta = 'S'
while resposta=='S':
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M / F): ")
    if sexo!='M' and sexo!='F':
        print("\n*** RESPOSTA INVÁLIDA! ***")
        resposta = 0
    else:
        if idade>18:
            maioridade.append(idade)
        if sexo=='M':
            homens.append(sexo)
        if sexo=='F' and idade<20:
            mulheres_menor20.append(0)
            resposta = input("Deseja continuar, sim ou não? (S / N): ")
        if resposta=='N':
            print("\n*** RESULTADO ***\n")
            print("Pessoas com mais de 18 anos:",len(maioridade))
            print("Homens cadastrados:",len(homens))
            print("Mulheres com menos de 20 anos:",len(mulheres_menor20))
        elif resposta!='S':
            print("\n*** RESPOSTA INVÁLIDA! ***")