""" AMB1430 - Programação para Engenharia Elétrica """

# Importar módulos/pacotes/funções
from stanfordkarel import *


if __name__ == "__main__":
  """ Chamada do programa Karel """
  run_karel_program()


def main():
  """ Linha de comentário sobre a lógica de varredura """
  varrer_diagonal()


def varrer_diagonal_primaria():
  """ Varrer a diagonal primária """
  while front_is_clear():
    if front_is_clear():
      put_beeper()
      move()
      turn_left()
    if front_is_clear():
      put_beeper()
      move()
      turn_right()


def varrer_diagonal_secundaria():
  """ Varrer a diagonal secundária """
  while front_is_clear():
    if front_is_clear():
      put_beeper()
      move()
      turn_left()
    if front_is_clear():
      put_beeper()
      move()
      turn_right()


def varrer_diagonal():
  """ Varrer o mundo diagonalmente """
  while front_is_clear():
    varrer_diagonal_primaria()
    # Girar no sentido contrario
    turn_left()
    turn_left()  
    varrer_diagonal_secundaria()
    # Girar no sentido contrario
    turn_left()
    turn_left()


def turn_right():
  """ Girar para a direita """
  turn_left()
  turn_left()
  turn_left()


def mover_para_fronteira():
  """ Mover enquanto não atingir a fronteira """
  while front_is_clear():
    move()  


def varrer_fronteira():
  """ Varrer as fronteiras do mundo com 4 lados """
  for contador in range(4):
    mover_fronteira()
    turn_left()


def varrer_horizontal():
  """ Varrer o mundo no padrão zig-zag horizontal """
  while front_is_clear():
    # Zig
    mover_fronteira()
    turn_left()
    if front_is_clear():
      move()
      turn_left()
    # Zag
    mover_fronteira()
    turn_right()
    if front_is_clear():
      move()
      turn_right()


def varrer_vertical():
  """ Varrer o mundo no padrão zig-zag vertical """
  turn_right()
  turn_right()
  while front_is_clear():
    # Zig
    mover_fronteira()
    turn_left()
    if front_is_clear():
      move()
      turn_left()
    # Zag      
    mover_fronteira()
    turn_right()
    if front_is_clear():
      move()
      turn_right()      


 


# def atualizar_posicao(x_pos, y_pos):
#   """ Atualizar posição """
#   if facing_east():
#     x_pos = x_pos + 1
#   elif facing_west():
#     x_pos = x_pos - 1
#   elif facing_north():
#     y_pos = y_pos + 1
#   else:
#     y_pos = y_pos - 1

#   return (x_pos, y_pos)

# # Variavel Global
# # Posição do robô
# x_pos = 0
# y_pos = 0

# # Atualizar mapa de ocupação
# mapa = [[0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0]]