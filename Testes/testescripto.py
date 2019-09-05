import math

for i in range(10, 14):
    print("a"+str(round(math.sqrt(i),3)))

    menor = 0
    maior = i
    meio = (menor + maior) / 2
    valor = i

    while True:
        if meio*meio > valor:
            maior = meio
        elif meio*meio < valor:
            menor = meio
        elif meio*meio == valor:
            break

        if round(maior, 3) == round(meio, 3) == round(menor, 3):
            break

        meio = (menor + maior) / 2

    print("b"+str(round(meio, 3)))