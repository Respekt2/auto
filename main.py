from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

list_name_car = []
list_url_car = []
list_model_car = []
url = 'https://autodvc.ru/'
driver = webdriver.Chrome()
x = 0
os.makedirs('auto/data')
try:
    driver.get(url)
    time.sleep(3)
    cars = driver.find_elements(By.CLASS_NAME, 'car-vendor')
    for car in cars:
        name_car = car.find_element(By.TAG_NAME, 'a').text
        url_car = car.find_element(By.TAG_NAME, 'a').get_attribute("href")
        list_name_car.append(name_car)
        list_url_car.append(url_car)
    
    for model_car in list_url_car:
        list_model_car.clear()
        driver.get(model_car)
        time.sleep(1)    
        x += 1
        title = driver.find_elements(By.CLASS_NAME, 'field-content')         
        print(f'{x}/ 110')
        model_car_name = driver.find_element(By.CLASS_NAME, 'title')
        print(model_car_name.text)
        for i in title:
            list_model_car.append(i.text)
            for name in list_name_car:
                with open(f'data/{model_car_name.text}.json', 'w', encoding='utf-8') as file:  # f instead of r
                    json.dump(list_model_car, file, indent=4, ensure_ascii=False)
        
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()