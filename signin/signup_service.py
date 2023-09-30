from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def main():
  driver = webdriver.Chrome()
  url = "https://fmp.wizigo.tw/fmi/webd"
  driver.get(url)
  # 找到帳號、密碼和登入按鈕的input元素
  login_name_input = driver.find_element(By.ID, 'login_name')
  login_pwd_input = driver.find_element(By.ID, 'login_pwd')
  login_button = driver.find_element(By.ID, 'login_nonguest')

  # 填寫帳號和密碼
  login_name_input.send_keys('032')
  login_pwd_input.send_keys('1111')

  # 點擊登入按鈕
  try:
      login_button.click()
  except NoSuchElementException:
      print('登入異常1')
  else:
      print('登入成功1')
  wait = WebDriverWait(driver, 2)
  print('sdfsdfsdfds')

  first_login_page_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'image.v-widget')))
  second_login_button = first_login_page_buttons[0]
  second_login_button.click()

  time.sleep(2)

  second_login_input = driver.find_element(By.ID, 'login_name')
  second_login_pwd = driver.find_element(By.ID, 'login_pwd')
  second_login_button = driver.find_element(By.ID, 'login_nonguest')

  # 填寫帳號和密碼
  second_login_input.send_keys('032')
  second_login_pwd.send_keys('1111')

  # 點擊登入按鈕
  try:
      second_login_button.click()
  except NoSuchElementException:
      print('登入異常2')
  else:
      print('登入成功2')

  time.sleep(3)

  # 點擊簽到
  inside_buttons = driver.find_elements(By.CLASS_NAME, 'fm-button-container')
  test=driver.find_element(By.ID, 'b0p1o255i0i0r1')
  test.click()
  # to_sign_in_button = inside_buttons[0]
  # print(to_sign_in_button)
  # to_sign_in_button.click()

  time.sleep(3)

  sign_in_button = driver.find_element(By.ID, 'b0p0o44i0i0r1')
  sign_in_button.click()

  time.sleep(3)

  no_button = driver.find_element(By.XPATH, '//span[@class="v-button-caption" and text()="否"]')
  print(no_button)

  time.sleep(3)

  no_button.click()




