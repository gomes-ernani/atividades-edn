"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""

# Dados da viagem
distancia = 300  # em km
combustivel = 25  # em litros

# Cálculo do consumo médio
consumo_medio = distancia / combustivel

# Exibição dos resultados
print("Distância percorrida: {} km".format(distancia))
print("Combustível gasto: {} litros".format(combustivel))
print("Consumo médio: {:.2f} km/l".format(consumo_medio))