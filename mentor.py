'''
Juego de destreza MENTOR
de manera aleatoria selecciona un numero 1 - 5 y lo presenta
como nombre, el usuario debera escribir el digito antes de
que finalice el timer. Si no escribe nada y se consume el
tiempo, se da por perdida la partida.

Timer inicia en 5segundos
Despues de 10 acierto, el timer debe reducir 0.5 segundos
'''

import random
from threading import Thread
import time

cont =0
#diccionario de valores aleatorios para presentar en texto
reto = {"1":"uno","2":"dos","3":"tres","4":"cuatro","5":"cinco"}

#Instrucciones
print("")
print("-----------------------------------------------------")
print("")
print("              M E N T O R")
print("")
print("Teclea el numero que se te pide lo mas rapido posible")
print("by: Beto Garcia")
print("-----------------------------------------------------")
print("")

def timer(name, delay, repeat):
    print("Timer: " + name + " Started")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": "+str(time.ctime(time.time())))
        repeat -=1
    print("Timer: "+ name + " Completed")

def game:

    while True:
        #seleccionar numero aleatorio de 1 a 5 y convertir a String
        secretNum = str(random.randrange(1,6,1))
        #print (secretNum)
        #mostrar numero en texto
        print("Challenge:")
        print (reto[secretNum])
        print ("")
        #valor de input se considera como String por default
        ask = input("--> ")
        print("")
        #se compara string contra string
        if ask == secretNum:
            cont += 1
        else:
            print("Fallaste, lo siento")
            break

    print("Tu marca fue: ", cont)

def main():
    t1 = Thread(target=timer, args=("timer1", 1, 5))
    t1.start()
