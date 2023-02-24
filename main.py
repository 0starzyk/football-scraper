from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.fifa.com/fifa-world-ranking/men?dateId=id13869')
    elements = driver.find_element(By.ID, 'table_rankingTable__7gmVl')