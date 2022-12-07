import random
import time
from sys import exit

class adivinar_numero:
    def __init__(self):
        
        self.jugador_adivinadas = 0
        self.compu_adivinadas = 0
        
    
    def main(self):
        while True:
            try:
                
                print('*** BIENVENIDO A ADIVINA EL NUMERO! ***')
                print('1. JUGAR')
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
    def eleccion_jugador(self):
        while True:
            try:
                guess_facil = int(input('Elegi un numero entre 0 y 10: \n'))
                posibilidades = [0,1,2,3,4,5,6,7,8,9,10]
                if  guess_facil in posibilidades :
                    break
                else:
                    print('Elegi un numero entre 0 y 10')    
            except ValueError:
                print('Entrada incorrecta')

        return guess_facil

    def objetivo(self):
        return random.randint(0, 10)

    def eleccion_compu(self):
        return random.randint(0, 10) 
                
    def jugar(self):
        self.nombre_jugador()
        
        rondas = int(input("Cuantas veces queres jugar? \n"))
        
        for i in range(rondas):
            objetivo = self.objetivo()
            compu =  self.eleccion_compu()
            jugador = self.eleccion_jugador()
            time.sleep(2)
            print(f"\n El numero objetivo es: {objetivo}\n")
            print(f" Compu eligio: {compu}\n")
            print (f" {self.name.upper()} eligio: {jugador}\n")
            
            
            if compu == objetivo and jugador == objetivo:
                print(" Ambos adivinan")
                self.jugador_adivinadas += 1
                self.compu_adivinadas += 1
            elif objetivo != compu and jugador != objetivo:
                print(" Ninguno adivina")
            elif objetivo == compu and jugador != objetivo:
                print(" Gana compu")
                self.compu_adivinadas += 1
            else:
                print(f"Gana {self.name.upper()}")
                self.jugador_adivinadas += 1
        time.sleep(2)
        print(f"                    Resultado: {self.ganador()}")  
        
        while True:
            continuar = input("Desea jugar de nuevo ? s/n ").lower()
                   
            if continuar == 'n':
                exit()
            elif continuar == 's':
                self.main()    
                        
            else:
                print(" Respuesta invalida \n")
                continue          
    def nombre_jugador(self):
        name = (input("Como te llamas? "))
        self.name = name
        return name        
    
    def ganador(self):
        if self.jugador_adivinadas > self.compu_adivinadas:
            return 'GANASTE !'
        elif self.jugador_adivinadas < self.compu_adivinadas:
            return 'GANO COMPU!'
        else:
            return 'EMPATE !' 

if __name__ == "__main__":
    juego = adivinar_numero()
    juego.main()        