"""
Original file is located at
    https://colab.research.google.com/drive/1xgXKs-aYvunum_Xr4Yg4AncXISf4X2j0
"""

# ler do usuario o numero do cartão
print("Não colocar espaços") 
numero_cartao_possivel_erro = list(input())
numero_cartao = []
del numero_cartao[:]

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

print(Visa)
print("Cartão Valido" if sum(lista_somatoria) % 10 == 0 else "Cartão Invalido")

def verificarCartao(numero_cartao_possivel_erro):
  numero_cartao_possivel_erro = list()
  numero_cartao = []
  del numero_cartao[:]

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

  print(sum(lista_somatoria))

verificarCartao("3768 978971 27952")
