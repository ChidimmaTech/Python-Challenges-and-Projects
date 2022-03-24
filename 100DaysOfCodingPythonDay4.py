{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "100DaysOfCodingPythonDay4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMpNr6VXoUA4V4CeTkUw1Kr",
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
        "<a href=\"https://colab.research.google.com/github/ChidimmaTech/Python-Challenges-and-Projects/blob/main/100DaysOfCodingPythonDay4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "**Randomnisation:**\n",
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "kcjMLE4PU4ra"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "random_integer = random.randint(1, 10)\n",
        "print(random_integer)\n",
        "\n",
        "random_float = random.random()\n",
        "print(random_float)\n",
        "\n",
        "love_score = random.randint(1, 10)\n",
        "print(\"your score is\", love_score)"
      ],
      "metadata": {
        "id": "4JFt5FfoVIMe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Virtual Coin Toss:**\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "\n",
        "You are going to write a virtual coin toss program. It will randomly tell the user \"Heads\" or \"Tails\".\n"
      ],
      "metadata": {
        "id": "m0KRxIHxXcRN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "choice = random.randint(1, 6)\n",
        "\n",
        "#user inputs a number\n",
        "choose = int(input('choose a number:\\n'))\n",
        "if choose == 6:\n",
        "  print(\"Heads\")\n",
        "else:\n",
        "  print(\"Tails\")"
      ],
      "metadata": {
        "id": "FvjxflU_XfbF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Lists - Banker Roulette**\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "\n",
        "You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill."
      ],
      "metadata": {
        "id": "Z__a_na-mYLh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#user inputs given names\n",
        "names_string = input('Type given names, separated by a comma:\\n')\n",
        "names = names_string.split(',')\n",
        "chosen = random.choice(names)\n",
        "print('Below are the lists of given names.\\n', names)\n",
        "print('The person to pay the bill is:\\n', chosen)"
      ],
      "metadata": {
        "id": "dv5e5vnjmiH_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Nested List:**\n",
        "\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "You are going to write a program that will mark a spot with an X.\n",
        "\n"
      ],
      "metadata": {
        "id": "HEXlskvK26AO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('Welcome to emoji treasure hunt!')\n",
        "row1 = ['🙂', '😀', '😃']\n",
        "row2 = ['😄', '😁', '😅']\n",
        "row3 = ['😆', '🤣', '😂']\n",
        "\n",
        "emoji = [row1, row2, row3]\n",
        "print(f'{row1}\\n{row2}\\n{row3}')\n",
        "\n",
        "#user makes a choice\n",
        "hunt = input('Where do you want to put your treasure? Hint: Use two numbers between 1and 3:')\n",
        "horizontal = int(hunt[0])\n",
        "vertical = int(hunt[1])\n",
        "\n",
        "emoji[vertical - 1][horizontal - 1] = \"X\"\n",
        "\n",
        "print(f\"{row1}\\n{row2}\\n{row3}\")"
      ],
      "metadata": {
        "id": "CNFJWZOu3Bia"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Rock, Paper Scissors Game**"
      ],
      "metadata": {
        "id": "dCM_AMUgk9dM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "user_action = input(\"Enter a choice (rock, paper or scissors): \\n\")\n",
        "possible_actions = [\"rock\", \"paper\", \"scissors\"]\n",
        "computer_action = random.choice(possible_actions)\n",
        "print(f\"\\nYou chose {user_action}, computer chose {computer_action}.\\n\")\n",
        "\n",
        "if user_action == computer_action:\n",
        "    print(f\"Both players selected {user_action}. It's a tie!\")\n",
        "elif user_action == \"rock\":\n",
        "    if computer_action == \"scissors\":\n",
        "        print(\"Rock smashes scissors! You win!\")\n",
        "    else:\n",
        "        print(\"Paper covers rock! You lose.\")\n",
        "elif user_action == \"paper\":\n",
        "    if computer_action == \"rock\":\n",
        "        print(\"Paper covers rock! You win!\")\n",
        "    else:\n",
        "        print(\"Scissors cuts paper! You lose.\")\n",
        "elif user_action == \"scissors\":\n",
        "    if computer_action == \"paper\":\n",
        "        print(\"Scissors cuts paper! You win!\")\n",
        "    else:\n",
        "        print(\"Rock smashes scissors! You lose.\")\n"
      ],
      "metadata": {
        "id": "zFh9gwsClJhd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}