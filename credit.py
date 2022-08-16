"""
Original file is located at
    https://colab.research.google.com/drive/1xgXKs-aYvunum_Xr4Yg4AncXISf4X2j0
"""

# ler do usuario o numero do cartão
print("Não colocar espaços") 
numero_cartao_possivel_erro = list(input())
# Iniciar uma lista vazia para ser usada depois
numero_cartao = []
# deletar qualquer coisa que já tiver salvo na lista numero_cartao
del numero_cartao[:]

# Tratamento de erro: remove qualquer caracter não numerico
for item in numero_cartao_possivel_erro:
  if (item.isdigit()):
    numero_cartao.append(item)

lista_inteiros = list(map(int, numero_cartao))
lista_dobrados = []
for item in list(reversed(lista_inteiros))[1::2]:
    x = item * 2
    lista_dobrados.append(x)

lista_somatoria = []
for item in lista_dobrados:
  if item > 9:
    lista_somatoria.append(item - 9)

  else:
    lista_somatoria.append(item)

for item in list(reversed(lista_inteiros))[::2]:
  lista_somatoria.append(item)

if sum(lista_somatoria) % 10 == 0:
  if lista_inteiros[0] == 4:
    print("VISA")
  elif lista_inteiros[0] == 5 and (lista_inteiros[1] == 1 or 2 or 3 or 4 or 5):
    print("MASTERCARD")
  elif lista_inteiros[0] == 3 and (lista_inteiros[1] == 4 or 7):
    print("AMEX")
  else:
    print("Invalido")
else:
    print("Invalido")
