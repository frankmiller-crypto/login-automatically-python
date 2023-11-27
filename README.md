# README - Automatización de Inicio de Sesión en plataformas de streaming

Este script de Python automatiza el proceso de inicio de sesión en las plataformas Crunchyroll, Disney+, Hbomax, Netflix, Star+ utilizando Selenium. A continuación, encontrarás información detallada sobre cómo utilizar y ejecutar este script.

## Descripción

Este script permite validar un conjunto de credenciales almacenadas en un archivo CSV (carpeta csv) para iniciar sesión en las plataformas Crunchyroll, Disney+, Hbomax, Netflix, Star+ y determinar cuáles son válidas. Las credenciales válidas se guardan en un archivo de texto.

## Requisitos

- Python 3.x instalado: [Descargar Python](https://www.python.org/downloads/)
- WebDriver para Chrome: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Instalación

1. **Clonar el repositorio:**

   '''bash
   git clone https://github.com/frankmiller-crypto/login-automatically-python.git
   cd tu-repositorio
   '''

2. **Instalar las dependencias:**

   pip install selenium

3. **Descargar ChromeDriver:**

   Asegúrate de descargar la versión de ChromeDriver compatible con tu versión de Google Chrome. Puedes descargarlo [aquí](https://sites.google.com/chromium.org/driver/).

4. **Configurar el path de ChromeDriver:**

   Coloca el archivo 'chromedriver' descargado en una ubicación accesible y actualiza la variable 'PATH_CHROMEDRIVER' en el script con la ruta completa.

## Uso

1. **Preparar el archivo CSV:**

   Asegúrate de tener un archivo CSV con las credenciales en el formato adecuado (ver ejemplo en 'csv/starplus.csv').

2. **Ejecutar el script:**

   python nombre_del_script.py

3. **Verificar resultados válidos:**

   Las credenciales válidas se guardarán en un archivo de texto en la carpeta 'results'.

## Archivos y Estructura del Proyecto

- 'scripts/nombre_del_script.py': El script principal.
- 'csv/data_starplus.csv': Archivo CSV con las credenciales.
- 'results/credenciales_validas_starplus.txt': Archivo de texto con las credenciales válidas.

## Contribución

Si deseas contribuir al desarrollo de este script, sigue los pasos descritos en la sección de Contribución en el README.

## Problemas conocidos

- Se pueden encontrar problemas de ejecución si no se configura correctamente el path de ChromeDriver y la version correcta.
- En la plataforma de crunchyroll debido a que despues de 3 o 4 intentos aparece una captcha y por ende el script no serviria si no se resuelve la captcha
- En SO como Linux o MacOS deberás cambiar las rutas de 'csv/data_starplus.csv' a '..csv/data_starplus.csv'
- Es posible que debas cambiar los 'time.sleep' dependiendo de la velocidad de tu maquina y conexión a internet

## Soporte

Si encuentras algún problema o tienes preguntas, puedes abrir un problema en el [repositorio de problemas](https://github.com/frankmiller-crypto/login-automatically-python/issues).

¡Gracias por utilizar este script! Si tienes sugerencias de mejora, ¡estaré encantado de escucharlas!