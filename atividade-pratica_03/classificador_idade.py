"""
Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos) ou
Idoso (60 anos ou mais).

"""

def classificar_idade():
    print("Classificador de Idade\n")

    while True:
        entrada = input("Digite sua idade (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            idade = int(entrada)

            if idade < 0:
                print("Idade inválida. Digite um número positivo.\n")
            elif idade <= 12:
                print("Categoria: Criança 🧒\n")
            elif idade <= 17:
                print("Categoria: Adolescente 👦\n")
            elif idade <= 59:
                print("Categoria: Adulto 👨\n")
            else:
                print("Categoria: Idoso 👴\n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")

# Executar o programa
classificar_idade()