# Definindo função que irá ler e salvar os dados do usuario
def ler_numero():
  # ler do usuario o numero do cartão
  numero_cartao_possivel_erro = list(input("Digitar o número do cartão: "))

  numero_cartao = []
  # Tratamento de erro: remove qualquer caracter não numerico
  for item in numero_cartao_possivel_erro:
    if (item.isdigit()): # apenas caracteres numericos são adicionados
      numero_cartao.append(item)
  
  # Transforma a lista, até então de strings, em uma lista de inteiros
  lista_inteiros = list(map(int, numero_cartao))

  return lista_inteiros # Retorna a lista contendo cada numero do cartão como um inteiro

# Definindo função que validará o numero do cartão seguindo o algoritmo de Luhn
def validar(num):
  lista_dobrados = []
  # Le a lista de inteiros de tras para frente, começando do pnultimo e lendo um sim um não
  for item in list(reversed(num))[1::2]:
      x = item * 2
      lista_dobrados.append(x)
  
  # Para numero maiores que 9, subtrair nove (assim gerando o resultado da soma dos digitos. Exemplo: 10 - 9 = 1 e 1 + 0 = 1)
  # Para numeros menores que 9, apenas adicionar à nova lista
  lista_somatoria = []
  for item in lista_dobrados:
    if item > 9:
      lista_somatoria.append(item - 9)
    else:
      lista_somatoria.append(item)

  # Pega todos os numeros que sobraram da lista original e adiciona eles na lista_somatoria para participarem da somatoria
  for item in list(reversed(num))[::2]:
    lista_somatoria.append(item)

  # Primeiro é verificado se a somatoria é multipla de 10, caso não seja o processo encerra sem precisar verificar a bandeira
  # Caso a primeira verificação passe, é então verificado qual a bandeira do cartão (VISA, MASTERCARD ou AMEX) e retoramos o valor apropriado
  if sum(lista_somatoria) % 10 == 0:
    if num[0] == 4:
      print("VISA")
    elif num[0] == 5 and (num[1] == 1 or 2 or 3 or 4 or 5):
      print("MASTERCARD")
    elif num[0] == 3 and (num[1] == 4 or 7):
      print("AMEX")
    else:
      print("Invalido")
  else:
      print("Invalido")

# Chamando a função validar e inserindo a função input_cartao como valor de num
validar(ler_numero())
