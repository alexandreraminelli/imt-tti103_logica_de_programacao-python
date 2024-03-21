lista = []

for n in range(1, 6):
    lista.append(int(input(f'Digite o {n}º número: ')))
print('-' * 35)

maior = menor = lista[0]
maior_posicao = menor_posicao = 0
for p, n in enumerate(lista):
    if n > maior:
        maior = n
        maior_posicao = p
    if n < menor:
        menor = n
        menor_posicao = p

print(f'O maior número é {maior} na posição {maior_posicao}.')
print(f'O maior número é {menor} na posição {menor_posicao}.')
