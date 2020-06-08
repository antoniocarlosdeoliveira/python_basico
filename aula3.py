a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    print('Você digitou errado. Segundo bimestre')
c = int(input('terceiro bimestre: '))
if c > 10:
    print('Você digitou errado. Terceiro bimestre')
d = int(input('quarto bimestre: '))
if d > 10:
    print('Você digitou errado. Quarto bimestre')
media = (a + b + c + d) / 4
print('media: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('média: {}'.format(media))
# else:
#     print('foi informado alguma nota errada')




# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor'))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado par')
# else:
#     print('nenhum nùmero par foi digitado')


#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))

#if a > b and a > c:
#    print('o maior número é {}'.format(a))
#elif b > a and b > c:
#    print('o maior número é: {}'.format(b))
#else:
 #   print('o mairo número é: {}'.format(c))
#print('final do programa')