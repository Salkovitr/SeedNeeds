from Sensores import temperatura, suelo
from Logica import analizador
from Actuadores import riego, luces
from Comunicacion import red
import config

def loop():
    t, h = temperatura.leer_datos()
    humedad_suelo = suelo.leer_humedad()
    acciones = analizador.decidir(t, h, humedad_suelo)
    
    if acciones["regar"]:
        riego.activar()
    if acciones["luz"]:
        luces.encender()

while True:
    loop()