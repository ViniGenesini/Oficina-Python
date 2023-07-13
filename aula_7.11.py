''' 
EXERCÍCIO 11
Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:

1) Qual é o total gasto na compra.
2) Quantos produtos custam mais de R$ 1000.
3) Qual é o nome do produto mais barato.

'''

print("*** PREÇO DE PRODUTOS ***\n")
produtos = {}
resposta = 'S'
qtde_produto_mais_de_1000 = 0
preco_total = 0
while resposta == 'S':
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    produtos[preco_produto] = nome_produto
    preco_total += preco_produto
    if preco_produto > 1000:
        qtde_produto_mais_de_1000 += 1
    resposta = input("\n*** CONTINUAR? (S ou N?)***\n")
if resposta != 'N':
    print("*** VALOR INVÁLIDO! ***")
else:
    ordem_preco = sorted(produtos)
    print(f"Total da compra: R$ {preco_total:.2f}")
    print(f"Quantidade de produtos que custem mais de R$ 1000.00: {qtde_produto_mais_de_1000}")
    print(f"Nome do produto mais barato: {produtos[ordem_preco[0]]}")
