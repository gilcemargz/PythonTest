import os

print(5|8)


t = open("d:/teste.txt", "wt")
t.write("Isso é um teste \nOutra linha")
t.close()
x = open("d:/teste.txt", "r")

for i in x:
    print(i)

x.close()
os.remove("d:/teste.txt")

exit()

#Isso é um comentário em python
if 5 > 2:
    print("Cinco é maior que 2")

#x1 = input("Qual o seu nome?")
#print("Olá "+x1)
x = 5
y = "  Gilcemar, o grande   "
y1 = y.split(",")
print(str(x) + " é o número do "+y)
print(y[2])
print(y[1:3])
print(y.strip())
print("Quantidade de caractreces de "+y+" é "+str(len(y)))
print("Quantidade de caractreces de "+y.strip()+" é "+str(len(y.strip())))
print(y.lower())
print(y.upper())
print(y.replace("e", "i"))
print(y1)


x1 = 1
x2 = 2.8
x3 = 1j
print(x1)
print(x2)
print(x3)

lista = ["Laranja", "Melancia", "Limão", "Pera"]
print(lista)
print(lista[0])
lista[2] = "Limão galego"
print(lista)

for n in lista:
    print(n)

if "Pera" in lista:
    print("Tem pera na lista")

print("Itens nesta lista " + str(len(lista)))

lista.append("Morango")
print(lista)
lista.insert(0, "Uva")
print(lista)
lista.remove("Pera")
print(lista)
lista.pop(3)
print(lista)
#del lista
lista.clear()
print(lista)
del lista
lista = list(("Goiaba", "Melão", "Jabuticaba"))
print(lista)

umaTupla = ("Vermelho", "Rosa", "Preto", "Azul", "Verde")
print(umaTupla)
print(umaTupla[1])
for n in umaTupla:
    print(n)

if "Rosa" in umaTupla:
    print("Existe rosa")
print(len(umaTupla))

outraTupla = tuple(("1", "2", "3","1"))
print(outraTupla)
print(outraTupla.count("1"))
print(outraTupla.index("3"))

umSet = {"Maça", "Banana", "Pera"}

for i in umSet:
    print(i)

print("Banana" in umSet)
umSet.add("Pêssego")
print(umSet)
umSet.update(["Limão", "Goiaba"])
print(umSet)
print(len(umSet))
umSet.remove("Limão")
print(umSet)
umSet.discard("Goiaba")
print(umSet)
umSet.pop()
print(umSet)

novoDicionario = {
    "marca": "Ford",
    "modelo": "ka",
    "ano": 2018
}

print(novoDicionario["marca"])
print(novoDicionario.get("marca"))
novoDicionario["marca"] = "vw"
print(novoDicionario)

for x in novoDicionario:
    print(x)

for x in novoDicionario:
    print(novoDicionario[x])

for x in novoDicionario.values():
    print(x)

if "marca" in novoDicionario:
    print("Tem marca")

print(len(novoDicionario))
novoDicionario["cor"] = "vermelho"
print(novoDicionario)
novoDicionario.popitem()
print(novoDicionario)
novoDicionario.clear()
print(novoDicionario)
outroDic = dict(marca="ford", modelo="ka", ano=2019)
print(outroDic)

x = 1
y = 9

if x > y:
    print("X é > que y")
elif x == y:
    print("x é igual que y")
else:
    print("x é menor que y")

i = 10
while i >= 0:
    i -= 1
    if i == 3:
        continue
    print(i)

for i in range(0,50,4):
    print(i)
    if i == 5:
        break
else:
    print("Acabou o loop")

def minha_funcao(nome = "Teste"):
    print("Eu sou uma função e meu nome é " + nome)
    return 49

minha_funcao("Gilcemar")
print(minha_funcao())

x = lambda a : a + 10
print(x(5))

cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
print(len(cars))
cars.append("Toyota")
cars.pop(0)
cars.remove("BMW")
print(cars)

class minhaClasse:
    x = 5

p1 = minhaClasse()
print(p1.x)

class pessoa:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def abFuncao(self):
        print("Olá, meu nome é "+ self.name)

class aluno(pessoa):
    pass

a1 = aluno("Pedro",12)
print(a1.name)
print(a1.age)
p1 = pessoa("Gil", 32)
print(p1.age)
print(p1.name)
p1.abFuncao()
p1.age = 33
print(p1.age)
del p1.age
p1.age = 11
print(p1.age)

teste = iter(umaTupla)

print(next(teste))
print(next(teste))
print(next(teste))

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%B"))

x = datetime.datetime(2020, 5, 17)
print(x)


import json
try:
    x = '{ name":"Joao", "age":30, "city":"Criciuma" }'
    y = json.loads(x)

    print(y)
    print(y["name"])

    x1 = json.dumps(y)
    print(x1)
except:
    print("Deu erro nesse bagaça"  )