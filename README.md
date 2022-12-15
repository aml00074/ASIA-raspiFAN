# Control de encendido y apagado del ventilador de Raspberry Pi

Este script trata de controlar el encendido y apagado del ventilador oficial de Raspberry Pi según la temperatura a la que se encuentra la CPU.

![Raspberry Pi 4 ya tiene caja oficial con refrigeración por ventilador:  cuesta apenas 5 dólares](https://i.blogs.es/e2ea49/case-fan007-2048x1365/1366_2000.jpg)

En concreto, el ventilador se enciende cuando la CPU supera un valor de temperatura de 50ºC y el ventilador se apaga cuando la CPU se encuentra por debajo de 42ºC.

## Pines

El ventilador oficial de Raspberry consta de tres cables. Un cable negro que irá conectado a GND de la placa, un cable rojo que irá conectado a la alimentación de 5V de la placa y un cable azul que va a ser el encargado de controlar el encendido y el apagado del ventilador en este caso se ha conectado al pin 18 o GPIO 24.

![Activar Pins en Raspberry Pi - infootec.net](https://www.infootec.net/wp-content/uploads/2021/05/GPIO-Pinout.png)

## Instalación

Para el correcto funcionamiento del script es necesaria la instalación de la librería RPi.GPIO que se puede hacer mediante pip con el siguiente comando.
```
pip install RPi.GPIO
```
El siguiente paso será ejecutar el archivo execute_raspiFan.sh.
