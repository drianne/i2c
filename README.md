# i2c
Repositório com código de acesso aos dados do sensor de temperatura

## Programa em c 
Dentro da pasta temperatura_c 

### Para compilar 
gcc src/codigo.c inc/bme280.c -I ./inc -lwiringPi -o bin/bme280

### Para executar 
./bin/bme280 /dev/i2c-1

## Programa em Python

Dentro da pasta temperatura_p 

### Para executar
python3 main.py
