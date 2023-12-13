# README - Automatización de Inicio de Sesión en plataformas de streaming

Este script de Python utiliza Selenium para automatizar el proceso de inicio de sesión en las plataformas Crunchyroll, Disney+, Hbomax, Netflix, Star+. Verifica la validez de las credenciales almacenadas en un archivo CSV y guarda los resultados en un archivo de texto.

## Requisitos

- Python 3.x instalado: [Descargar Python](https://www.python.org/downloads/)
- WebDriver para Chrome: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/frankmiller-crypto/login-automatically-python.git
   cd tu-repositorio
   ```

2. **Instalar las dependencias:**

   ```bash
   pip install selenium tqdm
   ```

3. **Descargar ChromeDriver:**

   Asegúrate de descargar la versión de ChromeDriver compatible con tu versión de Google Chrome. Puedes descargarlo [aquí](https://sites.google.com/chromium.org/driver/).

4. **Configurar el path de ChromeDriver:**

   Coloca el archivo 'chromedriver' descargado en una ubicación accesible y actualiza la variable 'PATH_CHROMEDRIVER' en el script con la ruta completa.

## Uso

1. **Preparar el archivo CSV:**

   Asegúrate de tener un archivo CSV con las credenciales en el formato adecuado (ver ejemplo en 'csv/data_starplus.csv').

2. **Ejecutar el script:**

   ```bash
   python nombre_del_script.py
   ```

3. **Verificar resultados válidos:**

   Las credenciales válidas se guardarán en un archivo de texto en la carpeta 'results'.

## Archivos y Estructura del Proyecto

- `scripts/nombre_del_script.py`: El script principal.
- `csv/data_starplus.csv`: Archivo CSV con las credenciales.
- `results/credenciales_validas_starplus.txt`: Archivo de texto con las credenciales válidas.

## Contribución

Si deseas contribuir al desarrollo de este script, sigue los pasos descritos en la sección de Contribución en el README.

## Problemas conocidos

- Pueden surgir problemas de ejecución si no se configura correctamente el path de ChromeDriver y la versión correcta.
- En la plataforma de Crunchyroll, después de 3 o 4 intentos aparece un captcha, y el script no será efectivo hasta que se resuelva el captcha.
- En sistemas operativos como Linux o MacOS, deberás cambiar las rutas de 'csv/data_starplus.csv' a '..csv/data_starplus.csv'.
- Es posible que debas ajustar los tiempos de 'time.sleep' dependiendo de la velocidad de tu máquina y la conexión a internet.

## Soporte

Si encuentras algún problema o tienes preguntas, puedes abrir un problema en el [repositorio de problemas](https://github.com/frankmiller-crypto/login-automatically-python/issues).

¡Gracias por utilizar este script! Si tienes sugerencias de mejora, ¡estaré encantado de escucharlas!
