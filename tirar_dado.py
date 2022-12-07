import time 
import random
from sys import exit

class Dados:
    def __init__(self):
        pass
    
    def nombre_jugador1(self):
        name1 = (input("Como te llamas jugador 1 ? "))
        self.name = name1
        return name1    
    
    def nombre_jugador2(self):
        name2 = (input("Como te llamas jugador 2 ? "))
        self.name2 = name2
        return name2    
    
    def jugar(self):
        jugador1 = self.nombre_jugador1()
        jugador2 = self.nombre_jugador2()
        self.lista1=[]
        self.lista2=[]
        
        for i in range(3):
            self.lista1.append(random.randint(1,6))
            self.lista2.append(random.randint(1,6))
        time.sleep(2)    
        print(f"{jugador1.upper()} saco {self.lista1}" )
        time.sleep(2)
        print(f"{jugador2.upper()} saco {self.lista2}\n" )
        time.sleep(2)
        print(self.ganador())
        
        while True:
            continuar = input("Desea jugar de nuevo ? s/n ").lower()
                   
            if continuar == 'n':
                exit()
            elif continuar == 's':
                self.main()    
                        
            else:
                print(" Respuesta invalida \n")
                continue          

    def ganador(self):
        if sum(self.lista1) > sum(self.lista2):
            return(f"           ** Gana {self.name.upper()} con {sum(self.lista1)} **")
        elif  sum(self.lista1) < sum(self.lista2):
            return(f"           ** Gana {self.name2.upper()} con {sum(self.lista2)}**")
        else:
            return("            ** Empate con {sum(self.lista2)}**")
        
        
    
    def main(self):
        while True:
            try:
                
                print('*** BIENVENIDO TIRAR DADOS ***')
                print('1. JUGAR ')
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
    dados = Dados()
    dados.main()                