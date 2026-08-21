import serial
from pynput.keyboard import Controller
import time

puerto = 'COM8'   # Cambiar según corresponda
baudrate = 9600

teclado = Controller()

# Mapeo de liberación: cada letra 'i'–'p' libera una 'a'–'h' correspondiente
liberar_mapeo = {
    'i': 'a',
    'j': 'b',
    'k': 'c',
    'l': 'd',
    'm': 'e',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'u': 'v'
}

try:
    with serial.Serial(puerto, baudrate, timeout=1) as ser:
        print(f"Escuchando en {puerto} a {baudrate} baudios...")

        while True:
            if ser.in_waiting > 0:
                dato = ser.read().decode('utf-8').strip()
                print(f"Recibido: {dato}")

                # Presionar teclas 'a' a 'h'
                if dato in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'v']:
                    teclado.press(dato)
                    print(f"Tecla '{dato}' presionada (sostenida)")

                # Liberar teclas correspondientes a 'i'–'p'
                elif dato in liberar_mapeo:
                    tecla = liberar_mapeo[dato]
                    teclado.release(tecla)
                    print(f"Tecla '{tecla}' liberada (por '{dato}')")

            time.sleep(0.01)

except serial.SerialException as e:
    print(f"Error al abrir el puerto: {e}")
