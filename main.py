
import tirar_dado 
import ppt
import adivinar_numero_
import mov_parabolico

print("                                             BIENVENID@s !\n")
print("                             *** Elige cual juego deseas jugar *** \n")

actividad = int(input("1. Tirar dados -- 2. Piedra papel o tijeras -- 3. Grafica de moviento movimiento parabolico -- 4. Adivina el numero "))

if actividad == 1:
    play = tirar_dado.Dados()
    play.main()
elif actividad == 2:
    play = ppt.piedra_papel_tijeras()
    play.main()
elif actividad == 3:
    mp = mov_parabolico.movimiento_parabolico()
    mp.main()
elif actividad == 4:
    juego = adivinar_numero_.adivinar_numero()
    juego.main()    
else:
    print('Hasta la proxima !!')
  
        
        

 