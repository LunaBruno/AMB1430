# AMB1430 - Programação para Engenharia Elétrica

# PEP 8 — the Style Guide for Python Code
# https://pep8.org/

# PEP 20 – The Zen of Python
# https://peps.python.org/pep-0020/
# import this

# project_root/
# │
# ├── project/  
# ├── docs/
# ├── README
# ├── HOW_TO_CONTRIBUTE
# ├── CODE_OF_CONDUCT
# ├── examples.py


# Importar módulos/pacotes
from stanfordkarel import *


def main():
  # Linha de comentário sobre a lógica de varredura
  move()
  girar_direita()


if __name__ == "__main__":
  # Chamada do programa Karel 
  run_karel_program()


def girar_direita():
  # Girar para a direita
  turn_left()
  turn_left()
  turn_left()


def mover_fronteira():
  # Mover enquanto não atinge a fronteira
  while front_is_clear():
    move()  