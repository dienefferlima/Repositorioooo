# exercicios com função
# 1
def soma(x, y, z):
    return x + y + z
print(soma(1, 2, 3))

# 2
#  funcao x + 1
def funcao(x, y):
    soma = x + y
    if soma > 0:
        return 'P'
    else:
        return 'N'
print(funcao(1, 2))

# 3
def numero_digitos(x):
    numero = list(map(int, str(x)))
    return len(numero)
print(numero_digitos(123))

# 4
def retangulo(linhas, colunas):
    if linhas < 1 or colunas < 1:
        linhas = 1
        colunas = 1
        return ['+' in range(linhas)
                '-' in range(linhas)
                '|' in range(colunas)
            ]
    else:
        return [linhas, colunas]

linhas = int(input('Digite o número de colunas:'))
colunas = int(input('Digite o número de colunas: '))
print(retangulo(linhas, colunas))