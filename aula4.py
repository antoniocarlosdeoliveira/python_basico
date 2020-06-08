a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('segundo bimestre: '))
while b > 10:
    print('Você digitou errado. Segundo bimestre')
c = int(input('terceiro bimestre: '))
while c > 10:
    print('Você digitou errado. Terceiro bimestre')
d = int(input('quarto bimestre: '))
while d > 10:
    print('Você digitou errado. Quarto bimestre')
media = (a + b + c + d) / 4
print('media: {}'.format(media))

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a correta: '))
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))