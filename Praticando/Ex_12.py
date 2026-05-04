"""12 - Crie um programa que solicite notas de alunos até que seja digitado -1.
Ao final, exiba  Média das notas, Maior nota e Menor nota."""

notas_alunos = []
continuar = True

while continuar:
    nota = int(input("Nota: "))

    nova_nota = int(input("Deseja inserir novas notas (1/-1): "))

    if nova_nota == 1:
        continuar = True
    else:
        continuar = False
        print("\nConcluído!")

    notas_alunos.append(nota)

print(notas_alunos)

soma = 0
for total in notas_alunos:
    soma += total

media = soma / len(notas_alunos)
print(f"\nMédia das notas: {media:.2f}")

maior_nota = notas_alunos[0]

for nota in notas_alunos:
    if nota > maior_nota:
        maior_nota = nota

menor_nota = notas_alunos[0]

for nota in notas_alunos:
    if nota < menor_nota:
        menor_nota = nota

print(f"\nMaior nota: {maior_nota}")
print(f"Maior nota: {menor_nota}")