lista = [19, 5, 2, 4, 6, 7]

lista[2] = 3

lista.append(9)
print(lista)

lista.sort()
print('Ordenado:', lista)

lista.reverse()
print('Reverso', lista)

print(f'Essa lista possui {len(lista)} elementos.')
