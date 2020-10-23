"""
Autores del código
José Gustavo Buenaventura Carreón
César Armando Lara Liceaga
"""
import random
import math
import os
#Crear matriz aletoria.
def matriz_aleatoria():
  nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
  random.shuffle(nums)
  matriz = [[],[],[],[]]
  temp = 0
  for i in range(4):
    for j in range(4):
      matriz[i].append(nums[temp])
      temp+= 1
  return matriz
#Poner una matriz predeterminada.
def matriz_escogida():
  nums=[]
  while len(nums)!=16:
    nums = input('Teclea los números separados por espacios (y el vació con un 0): ')
    nums = nums.split()
    dummy_nums = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']
    temp1 = []
    for i in nums:
      if (i not in temp1 and i in dummy_nums):
        temp1.append(i)
      else:
        print('Hay un número repetido o no disponible')
    nums = temp1
  for i in nums:
    if i == '0':
      nums[nums.index(i)] = ""
    else:
      nums[nums.index(i)] = int(i)
  assert len(nums) == 16
  matriz = [[],[],[],[]]
  temp = 0
  for i in range(4):
    for j in range(4):
      matriz[i].append(nums[temp])
      temp+= 1
  return matriz
#Enseñar el tablero.
def print_tablero(matriz):
  for i in matriz:
    for j in i:
      print('{:5s}'.format(str(j)),end=' ')
    print('\n')
#posibles respuests a elegir
respuestaNormal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,""]]
respuestaInversa = [["",15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]
respuestaEspiral = [[1,2,3,4],[12,13,14,5],[11,15,"",6],[10,9,8,7]]
respuestaEspiralInversa = [[4,3,2,1],[5,14,13,12],[6,15,"",11],[7,8,9,10]]
respuestaVerticalNormal = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,""]]
respuestaVerticalInversa = [["",12,8,4],[15,11,7,3],[14,10,6,2],[13,9,5,1]]
#Set de siglas de las respuestaEspiral
respuestas=['n','i','e','ei','vn','vi']
#Encontrar la casilla de un número dado.
def buscar_casillas(casilla,tablero):
  for i in tablero:
        i_index = tablero.index(i)
        for j in i:
            j_index= i.index(j)
            if tablero[i_index][j_index] == casilla:
                return (i_index,j_index)
#Distancia entre 2 casillas.
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
#Realizar el movimiento.
def movimiento(ficha,tablero):
  posicion1= buscar_casillas(ficha, tablero)
  posicion2= buscar_casillas('', tablero)
  dist= distance(posicion1,posicion2)
  if dist!=1:
    print('No es un movimiento posible')
  else:
    tablero[posicion1[0]][posicion1[1]],tablero[posicion2[0]][posicion2[1]]=tablero[posicion2[0]][posicion2[1]],tablero[posicion1[0]][posicion1[1]]
  return tablero
#main
def juego():
  count = 0
  modo = ''
  tipo = ''
  print('En caso de querer interrumpir el juego, ingrese 0.')
  while modo != "a" or modo != "p":
    modo= input('¿Quieres un tablero aleatorio(a) o uno predeterminado(p)? ')
    if modo == "a":
        matriz = matriz_aleatoria()
        break
    elif modo == "p":
        matriz = matriz_escogida()
        break

  while tipo not in respuestas:
      tipo = input('¿Cual tipo de juego quiere jugar? \nNormal (n) \nInverso (i) \nEspiral (e) \nEspiral Inverso (ei)\nVertical (v)\nVertical inverso(vi)\n')
  print_tablero(matriz)
  if tipo == 'n':
      solucion= respuestaNormal
  elif tipo == 'i':
      solucion=respuestaInversa
  elif tipo =='e':
      solucion=respuestaEspiral
  elif tipo == 'ei':
      solucion=respuestaEspiralInversa
  elif tipo == 'v':
      solucion=respuestaVerticalNormal
  elif tipo == 'vi':
      solucion = respuestaVerticalInversa
  while matriz != solucion:
    ficha = int(input('Seleccione la tecla que quiere mover: '))
    if ficha == 0:
        print('Gracias por jugar')
        break
    else:
        os.system('cls')
        movimiento(ficha, matriz)
        print_tablero(matriz)
        count += 1
  if matriz == solucion:
    print_tablero(matriz)
    print("Felicidades lo has resuelto en " + str(count) + " movimientos.")
juego()
"""
Caso de prueba
tablero=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,'',15]]
intercambiar 15 con ''
función movimiento(ficha, tablero)
se encuentra la ficha con la función buscar_casillas
se intercambia
tablero=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'']]
tablero==soluciónote
se termina el juego
Función movimientos
Dos casos
Fichas adyacentes
Fichas no adyacentes
Todas las fichas adyacentes están a una distancia 1
Si la ficha no está a distancia 1, no es posible moverla
Solo intercambiar fichas si distancia=1
para evitar que el usuario de inputs no deseados, se usaron while loops hasta que el usuario de el input correcto
"""
