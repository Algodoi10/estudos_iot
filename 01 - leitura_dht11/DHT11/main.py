from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(15))

print("Iniciando leitura do sensor DHT11...")
print("")

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
        print("Temperatura: {}°C  |  Umidade: {}%".format(temp, umid))
    except OSError as e:
        print("Erro ao ler o sensor:", e)

    time.sleep(2)
