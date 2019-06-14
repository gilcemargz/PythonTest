valorNovo = 110000

vetorTotal = [[37700.24, 0.285],
              [250, 0.572],
              [80592.24, 0.1425]]

vetorNovo = []

valorTotal = 0
for x in range(3):
    valorTotal += vetorTotal[x][0]

valorTotal = round(valorTotal, 2)

valorTotal += valorNovo

for x in range(3):
    vetorNovo.append(vetorTotal[x])
    vetorNovo[x][0] = round(valorTotal * vetorNovo[x][1], 2)

print(vetorNovo)