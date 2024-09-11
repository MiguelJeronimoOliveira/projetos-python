#Cronometro
import time

inicio = time.perf_counter()
print(int(inicio - inicio))

try:
    while True:
        time.sleep(1)
        fim = time.perf_counter()
        print(int(fim - inicio))
except KeyboardInterrupt:
    print("Cronometro parado.")
