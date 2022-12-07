import time
from random import randint
from sys import exit


class piedra_papel_tijeras:
    def __init__(self):
        self.opciones = "piedra", "papel", "tijeras"
        self.victorias_jugador = 0
        self.victorias_compu = 0
       
      
    
    def nombre_jugador(self):
        name = (input("Como te llamas? "))
        self.name = name
        return name
    
    
        
    def eleccion_jugador(self):
        while True:
            try:
                eleccion = int(input('Elegi Piedra (1), Papel (2) o Tijeras (3): '))

                if eleccion == 1 or eleccion == 2 or eleccion == 3:
                    break
                else:
                    print('Elegi un numero entre 1 y 3')    
            except ValueError:
                print('Entrada incorrecta')

        return eleccion

    def eleccion_compu(self):
        return randint(1,3)

    def ganador(self):
        if self.victorias_jugador == self.victorias_compu:
            return 'Empate !'
        elif self.victorias_jugador > self.victorias_compu:
            return 'Ganaste!'
        else:
            return 'Perdiste!'           
               
    
        
    
    
    def jugar(self):
        self.nombre_jugador()
        
                
        for i in range(3):
            jugador = self.eleccion_jugador()
            compu = self.eleccion_compu()
            
            print(f"{self.name.upper()} eligio {self.opciones[jugador-1].upper()}\n")
            time.sleep(2)
            print(f"COMPU eligio {self.opciones[compu-1].upper()}\n")
            time.sleep(2)
            
            
            if jugador == compu:
                print('Empate! ')
                
                
            elif ((jugador == 1 and compu == 3) or
                  (jugador == 2 and compu == 1) or
                  (jugador == 3 and compu == 2)):
                print(f"Ganaste {self.name.upper()} !\n") 
                
                self.victorias_jugador += 1
            
            elif ((compu == 1 and jugador == 3) or
                  (compu == 2 and jugador == 1) or
                  (compu == 3 and jugador == 2)):
                print(f"Perdiste {self.name.upper()} !")     
                
                self.victorias_compu += 1
       
        self.imprimir_marcador()
       
        
        while True:
            continuar = input("Desea jugar de nuevo ? s/n ").lower()
            
            if continuar == 'n':
                    exit()
            elif continuar == 's':
                self.main()    
                
            else:
                print(" Respuesta invalida \n")
                continue
        
    def imprimir_marcador(self):
        print("\n=================================")      
        print(f"        RESULTADO: {self.ganador()}  ")
        print(f"        {self.name.upper()} : {self.victorias_jugador}")
        print(f"        COMPU : {self.victorias_compu}")
        print("=================================\n")
        
            
    def main(self):
        while True:
            try:
                
                print('*** BIENVENIDO A PIEDRA, PAPEL O TIJERAS! ***')
                print('1. JUGAR AL MEJOR DE 3')
                print('2. SALIR')
                opcion_elegida = int(input('Ingrese una opcion: '))
            except ValueError:
                print('Opcion invalida')

            if opcion_elegida == 1:
                
                self.jugar()
                break
            
            elif opcion_elegida == 2:
                exit()
            else:
                print("Opcion invalida")
                
            
if __name__ == "__main__":
    PPT = piedra_papel_tijeras()
    PPT.main()