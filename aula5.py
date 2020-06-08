lista = [1, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#tupla
# imutavel
tupla = (1, 10, 12, 14)
print(tupla)

#tamanho da tupla
print(len(tupla))
tupla_animal = tuple(lista_animal)

#converter lista em tupla
print(type(tupla_animal))
print(tupla_animal)
#converter tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)



#print(lista_animal[0])

# lista.sort()
# lista_animal.sort()
#
# print(lista)
# print(lista_animal)
#
# lista_animal.reverse()
# print(lista_animal)

# soma com for
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
#
# print(soma)

#soma direto
#print(sum(lista))

#maior valor  e menor da lista
# print(max(lista))
# print(min(lista))
# print(min(lista_animal))
# print(max(lista_animal))

# nova_lista = lista_animal * 3
# print(nova_lista)

#condicional
# animal = input('Digite o nome de um animal: ')
# if animal in lista_animal:
#
#     print('animal encontrado na lista')
# else:
#     print('Esse animal não existe na lista, estou adicionando ele a sua lista agora mesmo! ')
#     lista_animal.append(animal)
#     print('Sua nova lista de animal {}'.format(lista_animal))

# lista_animal.pop(2)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)
