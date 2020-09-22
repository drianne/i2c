# requires RPi_I2C_driver.py
from inc import RPi_I2C_driver
from time import *
import smbus2
import bme280

lcd = RPi_I2C_driver.lcd()

porta_i2c = 1
endereco = 0x76

bus = smbus2.SMBus(porta_i2c)

calibracao_params =  bme280.load_calibration_params(bus, endereco)

dado = bme280.sample(bus, endereco, calibracao_params)

while(1):
	# Escreve no LCD 
	lcd.lcd_display_string("T:{:.2f}".format(dado.temperature) + " U:{:.2f}".format(dado.humidity) , 1)
	lcd.lcd_display_string("P:{:.2f}".format(dado.pressure), 2)
	sleep(1) 
	print("Id:" + str(dado.id))
	print("Data/hora:" + str(dado.timestamp))
	print("Temperatura:" + "{:.2f}".format(dado.temperature))
	print("Humidade:" + "{:.2f}".format(dado.humidity))
	print("Pressão:" + "{:.2f}".format(dado.pressure))
