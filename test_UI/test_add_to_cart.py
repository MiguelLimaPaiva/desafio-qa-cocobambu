from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://app-hom.cocobambu.com/delivery")
time.sleep(20)


# Simula digitar CEP (pode mudar conforme layout atual/entrada por localização automática.)
# driver.find_element(By.XPATH, "//*[@class='search-address-input']")
# driver.find_element(By.XPATH, "//*[@class='search-address-input']").send_keys("72405212")
# assert driver.find_element(By.ID, 'section-c8824012-5c03-40e6-9274-549033916c0d').is_displayed()
# time.sleep(3)

# Adiciona o item ao carrinho.
driver.find_element(By.XPATH, "//*[@class='item-name' and text()='Pizza Tradicional Grande']").click()

# Espera o elemento de descrição aparecer
desc_xpath = "//*[contains(@class, 'item-description') and contains(text(), 'Massa tradicional')]"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, desc_xpath)))

print("Elemento visível com sucesso!!")

driver.quit()
