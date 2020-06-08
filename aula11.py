
lista = [1, 10]

try:
    arquivo = open('notas.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print("Não é possível realizar um divisão por 0")
except ArithmeticError:
    print("Ouve um erro ao realizar uma opreração aritmética")
except IndexError:
    print("Erro ao acessar um indice inválido da lista!")
except BaseException as ex:
    print("Erro desconhecido. Erro: {}".format(ex))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")
    print("Fechando arquivo")
    arquivo.close()
