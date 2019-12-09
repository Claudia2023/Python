import random
import os

class Cucaracha:

    Cantidad = 5

    def Reproducir (self):
        self.Cantidad += random.randint(1, 10)

    def Aplastar (self):
        self.Cantidad -= 1

    def Rociar (self):
        self.Cantidad -= random.randint(1, 5)

if __name__ == "__main__":
    Insepto =  Cucaracha()
    while True:
        print('1..... Reproducir')
        print('2..... Aplastar')
        print('3..... Rociar')
        print('4..... Salir')
        Op=int(input('Ingrsar la Opcion: '))
        os.system ("clear")
        os.system ("cls")        
        
        if Op == 1:
            Insepto.Reproducir()
            print('Se Reproducieron ', Insepto.Cantidad, '\n')
        elif Op == 2:
            Insepto.Aplastar()
            print('Se Aplastaron 1 y Quedaron  ', Insepto.Cantidad, '\n')
        elif Op == 3:
            Insepto.Rociar()
            print('Se Rociaron y Quedaron  ', Insepto.Cantidad, '\n')
        else:
            break