"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def celsius_para_kelvin(c):
    return c + 273.15


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9


def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def kelvin_para_celsius(k):
    return k - 273.15


def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def conversor_temperatura():
    print("Conversor de Temperatura")
    print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)\n")

    while True:
        try:
            valor = float(input("Digite a temperatura: "))
            origem = input(
                "Digite a unidade de origem (C/F/K): ").strip().upper()
            destino = input(
                "Digite a unidade de destino (C/F/K): ").strip().upper()

            if origem == destino:
                print(
                    f"A temperatura permanece a mesma: {valor:.2f}°{destino}\n")
                continue

            if origem == 'C':
                if destino == 'F':
                    convertido = celsius_para_fahrenheit(valor)
                elif destino == 'K':
                    convertido = celsius_para_kelvin(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            elif origem == 'F':
                if destino == 'C':
                    convertido = fahrenheit_para_celsius(valor)
                elif destino == 'K':
                    convertido = fahrenheit_para_kelvin(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            elif origem == 'K':
                if destino == 'C':
                    convertido = kelvin_para_celsius(valor)
                elif destino == 'F':
                    convertido = kelvin_para_fahrenheit(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            else:
                raise ValueError("Unidade de origem inválida.")

            print(f"Temperatura convertida: {convertido:.2f}°{destino}\n")
            break

        except ValueError as e:
            print(f"Erro: {e}\nDigite novamente.\n")

# Executar o programa
conversor_temperatura()