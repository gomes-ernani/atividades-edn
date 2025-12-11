"""
Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

"""

def calculadora():
    while True:
        print("\nOperações: +  -  *  /  | Digite 'sair' para encerrar.")
        operacao = input("Escolha a operação: ")
        if operacao == 'sair':
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                print("Resultado:", num1 + num2)
            elif operacao == '-':
                print("Resultado:", num1 - num2)
            elif operacao == '*':
                print("Resultado:", num1 * num2)
            elif operacao == '/':
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Erro: Divisão por zero.")
            else:
                print("Operação inválida.")
        except ValueError:
            print("Entrada inválida. Digite números válidos.")

calculadora()