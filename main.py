from selenium import webdriver
from csv import writer
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
driver = webdriver.Chrome("C:\webdivers\chromedriver.exe")

driver.get('https://turbo.az/autos?q%5Bbarter%5D=0&q%5Bcrashed%5D=1&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bfor_spare_parts%5D=0&q%5Bloan%5D=0&q%5Bmake%5D%5B%5D=23&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=946&q%5Bonly_shops%5D=&q%5Bpainted%5D=1&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bregion%5D%5B%5D=&q%5Bsort%5D=&q%5Bused%5D=&q%5Byear_from%5D=&q%5Byear_to%5D=')

with open('turbo.csv', 'w') as turbo_csv:
    csv_writer = writer(turbo_csv)
    csv_writer.writerow(['price', 'year', 'engine', 'distance'])
    while True:
       cars = driver.find_elements(By.CLASS_NAME, 'products-i__bottom')
       for car in cars:
           price = car.find_element(By.CLASS_NAME, 'product-price' ).text
           year, engine, distance = car.find_element(By.CLASS_NAME, 'products-i__attributes' ).text.split(", ")
        
           csv_writer.writerow([price, year, engine, distance])
       try:
           next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
           next_button.click()
           sleep(5)
       except NoSuchElementException:
           driver.quit()