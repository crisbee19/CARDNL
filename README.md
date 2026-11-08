# CARDNL: Coordinador y actualizador de recursos ante desastres naturales

Proyecto final del curso de Internet de las Cosas (IoT).

**Integrantes:** Sophia Peluyera, Cristian Padilla, Ángel López

\---

## Problema

En Puerto Rico, los huracanes, terremotos, inundaciones y cortes de luz son parte de la realidad de la población. Durante y después de estos eventos se pierde la señal celular y el acceso a internet, disminuye el acceso a la información y las comunidades no saben qué recursos están disponibles a su alrededor. Las primeras 24 a 72 horas después de un desastre son críticas, y por la situación de la isla ese periodo puede extenderse. En ese tiempo, muchas personas dependen de su propia comunidad como primera respuesta.

La solución beneficia a las comunidades y sus integrantes, a sus líderes y a las organizaciones de manejo de emergencias.

## Solución

CARDNL es una red local, que no depende de internet, para coordinar recursos esenciales después de un desastre. Cada vivienda tiene un dispositivo con el que puede pedir u ofrecer recursos como agua, comida o primeros auxilios. Los mensajes viajan por radio hasta un centro comunitario (Raspberry Pi), que lleva el inventario actualizado, une cada solicitud con quien tiene el recurso y permite que un voluntario acepte transportarlo y confirme la entrega. Toda la información se consulta en un tablero web que se abre desde el navegador del celular (Safari o Chrome) conectándose a la red Wi-Fi propia de la Raspberry Pi.

Como medida de mejora se propone el tiempo entre una solicitud y su entrega confirmada, que el sistema registra automáticamente.

## Componentes

* **Nodo de vivienda (Heltec WiFi LoRa 32 V3):** ESP32 con radio LoRa y pantalla OLED. Lee el teclado y envía las solicitudes por LoRa.
* **Teclado matricial 4×4:** permite escoger el tipo de solicitud o recurso.
* **Receptor central (Heltec WiFi LoRa 32 V3):** recibe los mensajes LoRa de las viviendas y se los pasa a la Raspberry Pi por cable USB. Es el dispositivo intermediario del sistema.
* **Raspberry Pi 4:** centro comunitario. Guarda las solicitudes y el inventario, une pedidos con ofertas, crea la red Wi-Fi local y sirve el tablero web.
* **Celulares de los usuarios:** acceden al tablero para ver recursos, aceptar entregas y confirmarlas.
* \[Sensor de nivel de agua para alertas de inundación, si el grupo lo incluye]

## Diagrama

!\[Diagrama de componentes y flujo de datos](docs/diagrama/diagrama\_CARDNL.png)

El archivo editable está en `docs/diagrama/diagrama\_CARDNL.drawio` (se abre con draw.io).

## Costo estimado

Para estimar el costo de nuestro proyecto, buscamos los precios de los componentes que necesitaríamos si fuéramos a construir el sistema físicamente. Consultamos tiendas como Rokland, Adafruit, PiShop y Walmart (ver Referencias).

**Es importante aclarar que esta cotización corresponde a una posible implementación física del proyecto y no necesariamente a los gastos de nuestra simulación.** Como inicialmente estaremos trabajando con una simulación, no sería necesario comprar todos los materiales mencionados. Sin embargo, incluimos sus precios para tener una idea de cuánto costaría desarrollar el prototipo físico y evaluar su viabilidad fuera del salón.

1. Heltec WiFi LoRa 32 V3 con antena: 4 × $29.97 = $119.88 (Rokland).
2. Raspberry Pi 4 de 4 GB: $100.00 (PiShop). **Material que el grupo ya tenía.**
3. Teclado matricial 4×4: 3 × $5.95 = $17.85 (Adafruit).
4. Protoboard y cables de conexión: 3 × $9.95 = $29.85 (Adafruit).
5. Cable USB-A a USB-C: 4 × $4.95 = $19.80 (Adafruit).
6. Tarjeta microSD de 32 GB: $19.95 (PiShop).
7. Fuente de alimentación para Raspberry Pi: $8.95 (PiShop).
8. Adaptador de alimentación USB: 3 × $7.95 = $23.85 (Adafruit).

**Costo total estimado:** $340.13. Como el grupo ya tenía la Raspberry Pi, el gasto adicional para construir el prototipo físico sería de $240.13 antes de impuestos, o $267.74 con el IVU de 11.5 %, sin incluir el envío.

Debemos tener en cuenta que estas cantidades no representan lo que estaríamos gastando actualmente en la simulación, sino una estimación de los materiales necesarios para construir el sistema físicamente. Al utilizar herramientas de simulación y componentes que ya tenemos disponibles, el costo real de esta etapa podría ser menor.

**Gastos adicionales para apagones:** Si el sistema se implementara físicamente, también tendríamos que considerar fuentes de energía alternativas para mantener los dispositivos funcionando durante una emergencia. Una opción sería utilizar tres baterías portátiles para las viviendas y una de mayor capacidad para la Raspberry Pi, por un total aproximado de $127.94. Esto elevaría el valor total de los componentes a unos $468.07, sin incluir impuestos ni envío. Antes de utilizarlas, sería necesario verificar su compatibilidad y duración.

**Gastos recurrentes:** El sistema no necesitaría pagos mensuales de internet ni de servicios en la nube para su funcionamiento básico. Sin embargo, en una implementación física tendríamos que considerar el consumo eléctrico y el mantenimiento de los equipos, incluyendo el reemplazo de baterías, cables o dispositivos que puedan dañarse.

En nuestro caso, trabajar inicialmente mediante una simulación nos permitiría demostrar las funciones principales del sistema sin tener que invertir en todos estos componentes. Más adelante, si se quisiera implementar en una comunidad, sería necesario adquirir los materiales, realizar pruebas de comunicación y evaluar los costos adicionales de instalación y mantenimiento.

## Cómo poner en funcionamiento el prototipo





### Nodos de vivienda y receptor (Heltec WiFi LoRa 32 V3)

1. Instalar Arduino IDE y añadir el soporte para placas Heltec ESP32.
2. Instalar las bibliotecas: \[nombres de las bibliotecas usadas].
3. Copiar `codigo/config.example.h` como `config.h` y escribir los datos de la red (este archivo no se sube al repositorio).
4. Cargar `codigo/nodo\_vivienda/` en cada nodo de vivienda y `codigo/receptor/` en el receptor.
5. Conectar el teclado 4×4 a los pines \[pines] del nodo.

### Raspberry Pi

1. Instalar Raspberry Pi OS y Python 3.
2. Instalar las dependencias: `pip install -r codigo/raspberry\_pi/requirements.txt`.
3. Configurar la Raspberry Pi como punto de acceso Wi-Fi: \[pasos o guía usada].
4. Conectar el receptor por USB y ejecutar `python3 codigo/raspberry\_pi/app.py`.
5. Desde un celular conectado a la red de la Raspberry Pi, abrir `http://\[dirección de la Pi]` en el navegador.

## Pruebas

Los resultados, fotos y videos de las pruebas están en la carpeta `pruebas/`. Ver `pruebas/resultados.md`.

## Seguridad, privacidad y limitaciones

* Cada nodo tiene un código único para que la Raspberry Pi sepa de qué vivienda viene cada solicitud.
* Los mensajes LoRa se cifran para que otras personas no puedan leerlos ni modificarlos.
* Las viviendas se identifican con un número o código, no con nombres personales.
* Las entregas se confirman por ambas partes (quien transporta y quien recibe).
* Las contraseñas y claves se guardan en un archivo de configuración que no se sube a GitHub.
* **Limitaciones:** el alcance de LoRa puede verse afectado por la distancia, las montañas y los edificios; LoRa solo transmite mensajes cortos; el sistema depende de baterías durante los apagones, y el prototipo se probó con pocos dispositivos.

## Presentación

La presentación del proyecto está en `presentacion/`.

## Referencias y créditos

**Ideas y proyectos de referencia**

* Meshtastic (https://meshtastic.org): sirvió como referencia de comunicación sin internet mediante LoRa. CARDNL no reproduce Meshtastic: el grupo desarrolló el registro de solicitudes, el inventario actualizado, el emparejamiento de recursos, el rol del voluntario y la confirmación de entregas.
* \[Otros repositorios o tutoriales usados, con su enlace y qué se tomó o adaptó de cada uno]

**Herramientas de inteligencia artificial**

* Se utilizaron herramientas de IA para generar ideas, un primer borrador del diagrama y la estructura de este README. El grupo revisó, modificó y adaptó el contenido final.

**Tiendas consultadas para el costo**

1. Rokland. (s. f.). Heltec WiFi LoRa 32 (V3) US915 MHz with optional plastic shell. https://store.rokland.com/collections/all-active-products/products/heltec-wifi-lora-32v3
2. PiShop US. (s. f.). Raspberry Pi 4 Model B/4GB. https://www.pishop.us/product/raspberry-pi-4-model-b-4gb/
3. Adafruit Industries. (s. f.). 4x4 Matrix Keypad. https://www.adafruit.com/product/3844
4. Adafruit Industries. (s. f.). Half Size Breadboard + 78 Piece Jumper Wire Bundle. https://www.adafruit.com/product/3314
5. Adafruit Industries. (s. f.). USB Type A to Type C Cable. https://www.adafruit.com/product/4474
6. PiShop US. (s. f.). Raspberry Pi microSD Card, 32GB. https://www.pishop.us/product/raspberry-pi-sd-card-32gb/
7. PiShop US. (s. f.). USB-C Power Supply, 5.1V 3.0A. https://www.pishop.us/product/usb-c-power-supply-5-1v-3-0a-black-ul-listed/
8. Adafruit Industries. (s. f.). 5V 2A Switching Power Supply. https://www.adafruit.com/product/1994
9. Walmart. (s. f.). Anker Power Banks. https://www.walmart.com/c/brand/anker-mobile-power-packs

## Contribución de cada integrante

* **Sophia Peluyera:** 
* **Cristian Padilla:** 
* **Ángel López:** 

