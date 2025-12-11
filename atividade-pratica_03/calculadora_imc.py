"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"

Para os demais cenários: classificacao = "Obeso"

"""

def calcular_imc():
    print("Calculadora de IMC (Índice de Massa Corporal)\n")

    while True:
        try:
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))

            if peso <= 0 or altura <= 0:
                print("Erro: Peso e altura devem ser maiores que zero.\n")
                continue

            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25:
                classificacao = "Peso normal"
            elif imc < 30:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obeso"

            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}\n")
            break

        except ValueError:
            print("Erro: Entrada inválida. Digite valores numéricos válidos.\n")

# Executar o programa
calcular_imc()