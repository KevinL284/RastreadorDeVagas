from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Localização do Brave

driver = webdriver.Chrome(options=options)
driver.get("https://www.indeed.com.br/") #da pra usar o linkedin mas a tela de login vai atrapalhar.

# Aplicando filtros
wait = WebDriverWait(driver, 10)
location_input = wait.until(EC.presence_of_element_located((By.NAME, "l")))
location_input.send_keys("João Pessoa, PB")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Desenvolvedor Python") #se divirta procurando aqui

search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
search_button.click()

# Aplicando filtro de data
date_filter = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Publicados a menos de 1 mês")]')))
date_filter.click()

# Obtendo os resultados
job_titles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h2[contains(@class, "title")]')))
for title in job_titles:
    print(title.text)

driver.quit()

#ainda estou trabalhando nesse sisteminha