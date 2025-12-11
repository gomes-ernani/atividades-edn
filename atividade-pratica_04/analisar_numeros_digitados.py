"""
Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares
ou ímpares e contabilizando quantos de cada tipo foram inseridos.

"""

def analisar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.")
            else:
                impares += 1
                print(f"{numero} é ímpar.")
        except ValueError:
            print("Digite um número válido.")

    print(f"\nTotal de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

analisar_numeros()