#  Repositório Validador de cartão
Trabalho realizado pelo aluno Lucas Zanon Guarnier, aluno de Ciência da Computação pela Universidade Vila Velha. Aluno do terceiro período durante realização deste trabalho.
Trabalho realizado para a materia de Linguagem de programação, orientado pelo professor [Abrantes Araujo Silva Filho](https://github.com/abrantesasf).

## O código:
Realizado em linguagem python, o codigo credit.py lê e valida um numero de cartão de credito usando o [algoritmo de Luhn (também conhecido como mod 10)](https://en.wikipedia.org/wiki/Luhn_algorithm).

Primeiro o programa pede pelo input de um numero de cartão que é salvo como lista para salvar cada caractere como um item de uma lista, após isso, mesmo sendo dito que não era necessário, o código irá retirar qualquer caractere não numérico digitado.

Após isso é realizado a transformação dos valores da lista de string para inteiros, para assim realizar as contas matemáticas.

Em seguida começa a primeira etapa do algoritmo de Luhn, onde o programa ira salvar  em uma nova lista, contando a partir do penúltimo, numero sim numero até chegar no final da lista. Cada um desses números salvos é então multiplicado por 2.

Para os numero que multiplicados por 2 tem seu valor acima de 9, subtraímos 9, esse calculo é uma abstração de uma das etapas do algoritmo de Luhn, onde ele soma os dígitos gerados após a multiplicação (Exemplo: 14, 1 + 4 = 5/ 14 - 9 = 5).

Por ultimo recuperamos os numero deixados para trás na terceira etapa (quando pegamos apenas numero sim numero não a partir do penúltimo) e os adicionamos junto a lista gerada na etapa anterior, para que possamos somar os valores da lista e verificar se o resultado é múltiplo de 10 (dai o nome mod 10).

Caso o numero não seja múltiplo de 10 (x % 10 != 0), o numero do cartão é invalido (assim concluindo o algoritmo de Luhn). Caso o numero seja multiplo de 10, verificamos a bandeira do cartão utilizando as instruções dadas no arquivo do pset-1.
