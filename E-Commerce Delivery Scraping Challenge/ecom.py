import selenium.common.exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

ser = Service("C:\\Users\\Hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

with open('E-commerce URL - input.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        driver.get(row[0])


        # find element that is visible on hover
        hover_element = driver.find_element(By.XPATH, "//div/div[@id='pc-drawer-id-1']")

        # simulate hover event using ActionChains
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()

        # scrape the element
        visible_element = driver.find_element(By.XPATH, '//div/div/div[@data-testid="shopee_drawer_contents"]')
        hover.perform()
        visible_element.click()
        visible_element_html = visible_element.get_attribute('outerHTML')
        shippings = visible_element.find_elements(By.XPATH, '//div[@class="AAaUS1"]')
        shippings_lst = []
        print(visible_element_html)
        for shipping in shippings:
            shippings_lst.append(shipping.text)
        print(shippings_lst)

# close the driver
driver.quit()
