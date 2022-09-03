from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import Constants as const 

class Booking(webdriver.Chrome):
  def __init__(self):
    options = webdriver.ChromeOptions().add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(ChromeDriverManager().install())
    super(Booking, self).__init__(service=service, options=options)
    self.maximize_window()
    self.implicitly_wait(3)
    
  def __exit__(self, exc_type, exc_value, trace):
    print("Saindo...")
    time.sleep(3)
  
  def pagina_inicial(self):
    self.get(const.BASE_URL)
    
    
    
  def mudar_moeda(self, moeda):
    if not moeda: 
      return
    self.implicitly_wait(10)
    self.find_element(By.CSS_SELECTOR, 'button[data-modal-id=language-selection]').click()
    self.find_element(By.CSS_SELECTOR, f'a[data-lang={moeda}]').click()
    
  def selecionar_local(self, local):
    self.find_element(By.CSS_SELECTOR, 'input[type=search]').send_keys(local)
    self.find_element(By.CSS_SELECTOR, '.c-autocomplete__list li:first-child').click()
    
    
  def selecionar_datas(self, inicio, termino):
    self.find_element(By.CSS_SELECTOR, '.xp__date-time div').click()
    self.find_element(By.CSS_SELECTOR, f'td[data-date="{inicio}"]').click()
    self.find_element(By.CSS_SELECTOR, f'td[data-date="{termino}"]').click()
    
  def selecionar_quartos(self, num_adults , num_children):
    self.implicitly_wait(10)
    self.find_element(By.CSS_SELECTOR, '.xp__guests').click()
    
    default_adults_value = int(self.find_element(By.CSS_SELECTOR, '.bui-stepper__display').text)
    addAdultButton = self.find_element(By.CSS_SELECTOR,'button[aria-describedby="group_adults_desc"]:nth-child(4)')
    addChildrenButton = self.find_element(By.CSS_SELECTOR,'button[aria-describedby="group_children_desc"]:nth-child(4)')
    
    
    for i in range(num_adults - default_adults_value):
      addAdultButton.click() 
      
    for i in range(num_children):
      addChildrenButton.click() 
    
    
    selectorKids = self.find_elements(By.CSS_SELECTOR,'.sb-group__children__field select')
    for i in range(num_children):
      selectorKids[i].click()
      selectorKids[i].find_element(By.CSS_SELECTOR, 'option:last-child').click()
    
    self.find_element(By.CSS_SELECTOR, '.sb-searchbox__button').click()
    
    
    
    