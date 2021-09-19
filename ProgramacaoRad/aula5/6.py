import random

lista = ['Olá', 'mundo', 123]

print('mundo' in lista)

lista_num = [10, 50, 40, 30, 50, 90, 70]

print(min(lista_num))
print(max(lista_num))
print(sum(lista_num))

estados = ['SP', 'RJ', 'AC']

# Adiciona item para a lista
estados.append('MG')
print(estados)

# pop apaga um valor de uma determinada posição
estados.pop(3)
print(estados)

estados.pop()
print(estados)

# remove produca um determinado VALOR para remover
estados.remove('RJ')
print(estados)

estados.insert(1, 'AC')
estados.insert(0, 'ES')

estados.sort()
print('---SORT---')
print(estados)

print('---shuffle---')
random.shuffle(estados)
estados.reverse()
print(estados)

print('---Adiciona elementos na lista---')
estados.append('MG')
estados.append('MG')
estados.append('AC')
estados.append('AL')
print('A lista contem ', estados.count('MG'), 'valores "MG" adicionados')

print('---Retorna o index do valor---')
print(estados.index('MG'))

numeros = [5, 10, 15, 20]
mais_numeros = [25, 30, 35]

print('---Adiciona uma lista em outra com extend---')

numeros.extend(mais_numeros)
print(numeros)