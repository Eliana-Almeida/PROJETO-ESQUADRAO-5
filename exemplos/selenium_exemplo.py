from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

navegador.get('https://www.google.com')

print('Google aberto com sucesso!')

time.sleep(5)

navegador.quit()
