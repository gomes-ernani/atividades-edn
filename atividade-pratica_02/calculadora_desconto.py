"""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20%

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20  # em %

# Cálculo do desconto
valor_desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("Produto:", nome_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Desconto: {}%".format(porcentagem_desconto))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final com desconto: R$ {:.2f}".format(preco_final))