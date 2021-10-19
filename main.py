# Import a library of functions called 'pygame'
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine

ancho = int(input("ancho de la ventana: "))
alto = int(input("alto de la ventana: "))
size = [1300, 600] # Define size of windows
size[0]=ancho
size[1]=alto

titulo = input("titulo: ")
rojo = int(input("cantidad de rojo: "))
verde = int(input("cantidad de verde: "))
azul = int(input("cantidad de azul: "))
color = (rojo,verde,azul)

main2(size,titulo,color)