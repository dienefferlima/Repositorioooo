nome = input('Digite seu nome: ')
primeira_letra = nome[0].lower()
if primeira_letra in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'):
    print('A sala será 101')
elif primeira_letra in ('l', 'm', 'n'):
    print('A sala será 102')
elif primeira_letra in ('0', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
    print('A sala será 103')