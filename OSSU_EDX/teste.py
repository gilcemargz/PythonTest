raiz = 308024

x = raiz / 2

count = 0
ant = None
while True:
    print(x)
    count += 1
    ant = x
    if x * x == raiz:
        print(f'A raiz de {raiz} é {x}')
        break
    else:
        x = ((x + (raiz / x)) / 2)
        if ant == x:
            break


print(f'Voltas {count}')
