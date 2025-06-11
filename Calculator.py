{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z7-NET4LaIUs",
        "outputId": "d288720d-da95-4bcb-ef17-37e35c81e7fa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- Simple  Calculator ---\n",
            "Enter first number: 5\n",
            "Enter operator (+, -, *, /): +6\n",
            "Enter second number: 5\n",
            "Result: Invalid operator\n",
            "Do you want to calculate again? (yes/no): no\n",
            "Complite exitution\n"
          ]
        }
      ],
      "source": [
        "# Define functions for operations\n",
        "def add(a, b):\n",
        "    return a + b\n",
        "\n",
        "def subtract(a, b):\n",
        "    return a - b\n",
        "\n",
        "def multiply(a, b):\n",
        "    return a * b\n",
        "\n",
        "def divide(a, b):\n",
        "    if b == 0:\n",
        "        return \"Error: Division by zero\"\n",
        "    return a / b\n",
        "\n",
        "# Main calculator function\n",
        "def calculator():\n",
        "    print(\"\\n--- Simple  Calculator ---\")\n",
        "    num1 = float(input(\"Enter first number: \"))\n",
        "    op = input(\"Enter operator (+, -, *, /): \")\n",
        "    num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "    if op == '+':\n",
        "        result = add(num1, num2)\n",
        "    elif op == '-':\n",
        "        result = subtract(num1, num2)\n",
        "    elif op == '*':\n",
        "        result = multiply(num1, num2)\n",
        "    elif op == '/':\n",
        "        result = divide(num1, num2)\n",
        "    else:\n",
        "        result = \"Invalid operator\"\n",
        "\n",
        "    print(\"Result:\", result)\n",
        "\n",
        "# Simulating a do-while loop\n",
        "while True:\n",
        "    calculator()\n",
        "    again = input(\"Do you want to calculate again? (yes/no): \").lower()\n",
        "    if again != 'yes':\n",
        "        print(\"Complite exitution\")\n",
        "        break\n"
      ]
    }
  ]
}
