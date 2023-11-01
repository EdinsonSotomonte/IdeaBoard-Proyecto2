# IdeaBoard-Proyecto2

Propuesta de Dispositivo Wearable para Mascotas en "Pets Inn" 

 

Descripción: Nuestro dispositivo wearable, conocido como "PetGuard," está diseñado para monitorizar la temperatura y la humedad en tiempo real en las áreas donde se encuentran las mascotas en "Pets Inn." 

Problema: La necesidad de garantizar el confort y bienestar de las mascotas durante su estancia. 

Ventajas: Monitoreo continuo, notificaciones en tiempo real y tranquilidad para los dueños de las mascotas. 

Objetivo: Mejorar la experiencia de las mascotas y ganar la confianza de los dueños. 

Introducción: 

Presentamos "PetGuard," un dispositivo que aborda este problema al proporcionar monitoreo en tiempo real de la temperatura y la humedad en las áreas de las mascotas. 

Descripción del Dispositivo: 

Pequeño dispositivo que se sujeta al collar de la mascota. 

Sensores de temperatura y humedad de alta precisión. 

Transmisión de datos en tiempo real a través de una red segura. 


imagen

Dispositivo (Entrada):  Se representa el dispositivo, que actúa como punto de entrada de datos. 

Crear estructura: El dispositivo crea una estructura de datos que desea enviar a la API. Esto incluye información sobre la temperatura y la humedad recopiladas por el dispositivo. 

Enviar estructura a la API: El dispositivo envía la estructura de datos a la API para su procesamiento. Este paso implica la transmisión de datos desde el dispositivo hasta la API. 

API (Recibir estructura): La API recibe la estructura de datos del dispositivo y comienza a procesarla. 

Guardar estructura en la Base de Datos: Después de recibir la estructura de datos, la API la almacena en la base de datos. Esto permite que los datos estén disponibles para su consulta y posterior análisis. 

Mostrar datos (Salida): En el extremo derecho, se representa la salida de datos desde la base de datos. Los datos pueden ser recuperados para su visualización, análisis o notificación a los dueños de las mascotas.


imagen

Un sensor de humedad y temperatura (DHT11) y un módulo Wi-Fi. El DHT11 registra datos sobre la humedad y la temperatura, mientras que el ESP8266 se encarga de transmitir estos datos a través de Internet a un servidor remoto. 

En términos de funcionamiento, el ESP8266 actúa como una especie de repetidor de red inalámbrica. En este caso, recibe la información del sensor DHT11 y la envía a un servidor en línea. De esta manera, el sensor puede monitorear la humedad y la temperatura incluso cuando no está cerca de un computador o dispositivo similar. 
