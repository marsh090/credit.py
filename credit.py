{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "credit.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOdkWFRCv8AnfGM2Dt/jbaK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/marsh090/credit.py/blob/main/credit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ler do usuario o numero do cartão\n",
        "print(\"Não colocar espaços\") \n",
        "numero_cartao_possivel_erro = list(input())\n",
        "numero_cartao = []\n",
        "del numero_cartao[:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WHtpiTKOKRCD",
        "outputId": "f1d84d0c-6c00-414e-8e77-09531aeeb8fe"
      },
      "execution_count": 200,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Não colocar espaços\n",
            "3768 978971 27952\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for item in numero_cartao_possivel_erro:\n",
        "  if (item.isdigit()):\n",
        "    numero_cartao.append(item)"
      ],
      "metadata": {
        "id": "cdH1tHJuXN3-"
      },
      "execution_count": 201,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lista_inteiros = list(map(int, numero_cartao))\n",
        "lista_dobrados = []\n",
        "for item in list(reversed(lista_inteiros))[1::2]:\n",
        "    x = item * 2\n",
        "    lista_dobrados.append(x)"
      ],
      "metadata": {
        "id": "-qdoF7gmKrwU"
      },
      "execution_count": 202,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lista_somatoria = []\n",
        "for item in lista_dobrados:\n",
        "  if item > 9:\n",
        "    lista_somatoria.append(item - 9)\n",
        "\n",
        "  else:\n",
        "    lista_somatoria.append(item)"
      ],
      "metadata": {
        "id": "jq17YVxNpIxG"
      },
      "execution_count": 203,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for item in list(reversed(lista_inteiros))[::2]:\n",
        "  lista_somatoria.append(item)"
      ],
      "metadata": {
        "id": "HUHID3L4sDDW"
      },
      "execution_count": 204,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(Visa)\n",
        "print(\"Cartão Valido\" if sum(lista_somatoria) % 10 == 0 else \"Cartão Invalido\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YK1T5i8iqtzK",
        "outputId": "6560d476-1fdb-45b2-8b2d-2bc3b9077cc5"
      },
      "execution_count": 209,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cartão Valido\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def verificarCartao(numero_cartao_possivel_erro):\n",
        "  numero_cartao_possivel_erro = list()\n",
        "  numero_cartao = []\n",
        "  del numero_cartao[:]\n",
        "\n",
        "  for item in numero_cartao_possivel_erro:\n",
        "    if (item.isdigit()):\n",
        "      numero_cartao.append(item)\n",
        "\n",
        "  lista_inteiros = list(map(int, numero_cartao))\n",
        "  lista_dobrados = []\n",
        "  for item in list(reversed(lista_inteiros))[1::2]:\n",
        "      x = item * 2\n",
        "      lista_dobrados.append(x)\n",
        "\n",
        "  lista_somatoria = []\n",
        "  for item in lista_dobrados:\n",
        "    if item > 9:\n",
        "      lista_somatoria.append(item - 9)\n",
        "    else:\n",
        "      lista_somatoria.append(item)\n",
        "\n",
        "  for item in list(reversed(lista_inteiros))[::2]:\n",
        "    lista_somatoria.append(item)\n",
        "\n",
        "  print(sum(lista_somatoria))"
      ],
      "metadata": {
        "id": "n7GXp6x8vBO4"
      },
      "execution_count": 206,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "verificarCartao(\"3768 978971 27952\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6BH5RrVetyR8",
        "outputId": "3d05ae0c-44c2-4d9d-a5de-292a1f33c9a1"
      },
      "execution_count": 207,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    }
  ]
}