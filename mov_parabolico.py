import numpy as np
import matplotlib.pyplot as plt
from sys import exit

class movimiento_parabolico:
    def __init__(self):
        pass
    
    def x_pos(self):
        while True:
            try:
                self.angulo = int(input("Ingrese un angulo de disparo entre 0° y 90° : "))
                #posibilidades = [0,1,2,3,4,5,6,7,8,9,10]
                if  self.angulo > 90 :
                    print('Elegi un angulo entre 0 y 90°')  
                elif self.angulo < 0:
                    print('Elegi un numero entre 0 y 90°')
                else:
                    break        
            except ValueError:
                print('Entrada incorrecta')        
        
        self.x0 = 0  #Posicion x inicial
        self.y0 = 0  #Posicion y inicial
        self.v0 = 70 #Velocidad inicial
        self.g = 9.81 #Aceleracion de la gravedad 
        t= np.linspace(0,20,50) #Tiempo
        x = self.x0+self.v0*np.cos(self.angulo *((np.pi)/180))*t    #El angulo es pasado en radianes
        return x
    
    def y_pos(self):
        
        self.angulo = self.angulo #45*((np.pi)/180) #np.pi/4  #45°
        self.x0 = 0  #Posicion x inicial
        self.y0 = 0  #Posicion y inicial
        self.v0 = 70 #Velocidad inicial
        self.g = 9.81 #Aceleracion de la gravedad 
        
        t= np.linspace(0,20,50) #Tiempo
        y = self.y0+(self.v0*np.sin(self.angulo*((np.pi)/180))*t) - ((self.g*t**2)/2) #El angulo es pasado en radianes
        
        return y
    
    
    def graficar(self):
            
        x= self.x_pos()
        y=self.y_pos()

        fig, ax = plt.subplots(figsize=(12, 7))

        plt.plot(x,y, 'r--o')
        ax.set_facecolor("black")
        ax.set_xlim(0,500)
        ax.set_ylim(0,260)
        
        ax.set_title('Posición en función de t en el movimiento parabólico', loc = "center", fontdict = {'fontsize':13, 'fontweight':'bold', 'color':'tab:red'})
        ax.set_xlabel("Posicion(x)")
        ax.set_ylabel("Posicion(y)")
        
        plt.grid()
        plt.show()
        print(f'Velocidad inicial: {self.v0}\n')
        print(f'Aceleracion de la gravedad: {self.g}\n')
        print(f'Angulo de lanzamiento: {self.angulo}°\n')
        print(f'Posicion inicial (x,y): ({self.x0},{self.y0})\n')

      
    def main(self):
        while True:
            try:
                
                print('                                 *** BIENVENIDO A GRAFICA DE MOVIMIENTO PARABOLICO ***\n')
                print('1. GRAFICAR ')
                print('2. SALIR')
                opcion_elegida = int(input('Ingrese una opcion: '))
            except ValueError:
                print('Opcion invalida')

            if opcion_elegida == 1:
                
                self.graficar()
                break
            
            elif opcion_elegida == 2:
                exit()
            else:
                print("Opcion invalida")   
                
if __name__ == "__main__":
    mp = movimiento_parabolico()
    mp.main() 