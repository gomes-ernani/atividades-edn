"""
Criar um código que registre as notas de alunos e calcular a média da turma.

"""

def calcular_media_turma():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota registrada.")

calcular_media_turma()