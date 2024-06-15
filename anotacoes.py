# ordenação numeros
numeros = [4, 2, 6, 1, 3]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)

# compreenssoes de listas
numeros = [numeros for numeros in range(5) if numeros % 2 == 0]
print(numeros)

numeros1 = [x * x for x in range(5)]
print(numeros1)

numeros2 = [x * x for x in range(5) if x % 3 == 0]
print(numeros2)

# fazer uma lista com pares ordenaods
list = [(x, y)
        for x in range(10)
        for y in range(5)
]
print(list)

# escolhe aleatoriamente um elemento da lista
import random
jogador1 = random.choice(['X', 'O'])
print(jogador1)

# caso foi mais de 1, o 3 representa quantos algarismos serão sorteados
import random
numeros_aleatorios = random.sample([1, 2, 3, 4, 5, 6], 3)
print(numeros_aleatorios)

# caso não exista lista pode usar o range
import random 
numeros_aleatorio2 = range(10)
numeros_escolhidos = random.sample(numeros_aleatorio2, 3)
print(numeros_escolhidos)

# caso precise de números duplicados na escolha
import random
numeros_aleatorio3 = [random.choice(range(10))
                                    for _ in range(4)]
print(numeros_aleatorio3)

# printa 2 listas com 3 numeros em cada, de numeros até o 10 
import random
numeros_aleatorio4 = [random.sample((range(10)), 3)
                                    for _ in range(2)]
print(numeros_aleatorio4)

# map, reduce and filter
def double(x):
    return x * 2
xs = [1, 2, 3, 4]
outro_modo = [double(x) for x in xs]
outro_modo2 = map(double, xs)
print(outro_modo)
print(outro_modo2)
print(xs)

# compactar listas usando zip
L1 = [1, 3, 5, 7]
L2 = [0, 2, 4, 6]
combinado = zip(L1, L2)
print(combinado)

# cria uma lista com o 1 elemento de cada 1 e o 2 de cada uma
lista = [(1, 2), (3, 4), (5, 6)]
letras, numeros = zip(*lista)
print(letras, numeros)

