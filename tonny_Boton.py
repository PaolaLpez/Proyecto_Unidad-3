from machine import Pin, Timer
import time

# Pin para controlar el botón/relevo
boton = Pin(15, Pin.OUT)
boton.value(0)

# Variable de control
ultima_activacion = None
minutos = 60  # 1 minuto = 60 segundos

def activar_boton():
    global ultima_activacion
    ahora = time.localtime()
    if ultima_activacion is None or ahora[2] != ultima_activacion[2]:  # Cambió de día
        print("Botón activado")
        boton.value(1)
        ultima_activacion = ahora
        time.sleep(minutos)
        boton.value(0)
        print("Botón desactivado")

while True:
    activar_boton()
    time.sleep(3600)  # Esperar una hora para verificar otra vez