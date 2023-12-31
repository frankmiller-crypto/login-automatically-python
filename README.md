# README - Automatización de Inicio de Sesión en plataformas de streaming

Este script de Python utiliza Selenium para automatizar el proceso de inicio de sesión en las plataformas Crunchyroll, Disney+, Hbomax, Netflix, Star+. Verifica la validez de las credenciales almacenadas en un archivo CSV y guarda los resultados en un archivo de texto.

## Requisitos

- Python 3.x instalado: [Descargar Python](https://www.python.org/downloads/)
- WebDriver para Chrome: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/frankmiller-crypto/login-automatically-python.git
   cd login-automatically-python
   ```

2. **Instalar las dependencias:**

   ```bash
   pip install selenium tqdm
   ```

3. **Descargar ChromeDriver:**

   Asegúrate de descargar la versión de ChromeDriver compatible con tu versión de Google Chrome. Puedes descargarlo [aquí](https://sites.google.com/chromium.org/driver/).

4. **Configurar el path de ChromeDriver:**

   Coloca el archivo 'chromedriver' descargado en la carpeta chromedriver dentro de la carpeta de repositorio login-automatically-python

## Uso

1. **Preparar el archivo CSV:**

   Asegúrate de tener un archivo CSV con las credenciales en el formato adecuado (ver ejemplo en 'csv/data_starplus.csv').

2. **Ejecutar el script:**

   ```bash
   Asegúrate de abrir la terminal desde la raiz de la carpeta login-automatically-python
   python scripts/nombre_del_script.py
   python3 scripts/nombre_del_script.py
   ```

3. **Verificar resultados válidos:**

   Las credenciales válidas se guardarán en un archivo delimitado por comas (.csv) en la carpeta 'results'.

## Archivos y Estructura del Proyecto

- `scripts/nombre_del_script.py`: El script principal.
- `csv/data_starplus.csv`: Archivo CSV con las credenciales.
- `results/credenciales_validas_starplus.csv`: Archivo delimitado por comas con las credenciales válidas.

## Contribución

Si deseas contribuir al desarrollo de este script, sigue los pasos descritos en la sección de Contribución en el README.

## Problemas conocidos

- Pueden surgir problemas de ejecución si no se configura correctamente el path de ChromeDriver y la versión correcta.
- En la plataforma de Crunchyroll, después de 3 o 4 intentos aparece un captcha, y el script no será efectivo hasta que se resuelva el captcha. Por lo que ya no se le esta dando actualización al script de crunchyroll
- Es posible que debas ajustar los tiempos de 'time.sleep' o ' WebDriverWait(driver,)' dependiendo de la velocidad de tu máquina y la conexión a internet.
- Puede surgir problemas al momento del guardado de las credenciales de las credenciales debido al formato de fecha y hora 'locale.setlocale(locale.LC_TIME, 'en_ES.UTF-8')' esto va a variar dependiende del SO que tengas instalado y si soporta el formato establecido sí tienes problemas puedes cambiarlo al de tu region o borrar el formato y dejarlo sin formato de fecha y solo dejarlo en 'credenciales_validas_plataforma.csv'

## Soporte

Si encuentras algún problema o tienes preguntas, puedes abrir un problema en el [repositorio de problemas](https://github.com/frankmiller-crypto/login-automatically-python/issues).

¡Gracias por utilizar este script! Si tienes sugerencias de mejora, ¡estaré encantado de escucharlas!
